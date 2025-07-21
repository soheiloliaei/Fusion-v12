from typing import Dict, Optional, List
import re
import json
from pathlib import Path
from datetime import datetime
import os
from datetime import timedelta

FUSION_TODO_DIR = Path("_fusion_todo")
SAFETY_LOG_PATH = FUSION_TODO_DIR / "safety_log.json"

class PatternSafety:
    """Pattern safety system"""
    _safety_rules = {
        "special_tokens": {
            "{": "{{",
            "}": "}}",
            "###": "\\#\\#\\#",
            "---": "\\-\\-\\-",
            "\n\n\n+": "\n\n"  # Collapse multiple newlines
        },
        "blocked_patterns": [
            r"<script.*?>.*?</script>",  # Script tags
            r"<.*?onload=.*?>",          # onload handlers
            r"data:.*?base64",           # base64 data
            r"javascript:",              # javascript: URLs
            r"eval\(",                   # eval()
            r"system\(",                 # system()
            r"exec\(",                   # exec()
            r"require\(",                # require()
            r"import\s+['\"].*?['\"]"    # import statements
        ],
        "max_length": 10000,  # Maximum output length
        "max_newlines": 100   # Maximum number of newlines
    }
    
    _safety_log: List[Dict] = []
    
    @classmethod
    def load_safety_log(cls):
        """Load safety log"""
        if SAFETY_LOG_PATH.exists():
            with open(SAFETY_LOG_PATH, 'r') as f:
                cls._safety_log = json.load(f)
        else:
            cls._safety_log = []
            
    @classmethod
    def save_safety_log(cls):
        """Save safety log"""
        os.makedirs(FUSION_TODO_DIR, exist_ok=True)
        with open(SAFETY_LOG_PATH, 'w') as f:
            json.dump(cls._safety_log, f, indent=2)
            
    @classmethod
    def log_safety_event(
        cls,
        pattern_name: str,
        rule_triggered: str,
        original_text: str,
        modified_text: str
    ):
        """Log a safety rule application"""
        event = {
            "timestamp": datetime.now().isoformat(),
            "pattern": pattern_name,
            "rule": rule_triggered,
            "original_length": len(original_text),
            "modified_length": len(modified_text),
            "preview": original_text[:200] + "..." if len(original_text) > 200 else original_text
        }
        cls._safety_log.append(event)
        cls.save_safety_log()
        
    @classmethod
    def apply_safety_rules(cls, text: str, pattern_name: str) -> str:
        """Apply all safety rules to text"""
        original = text
        modified = text
        
        # Check length
        if len(modified) > cls._safety_rules["max_length"]:
            modified = modified[:cls._safety_rules["max_length"]]
            cls.log_safety_event(
                pattern_name=pattern_name,
                rule_triggered="max_length",
                original_text=original,
                modified_text=modified
            )
            
        # Check newlines
        newlines = modified.count('\n')
        if newlines > cls._safety_rules["max_newlines"]:
            modified = re.sub(r'\n{2,}', '\n\n', modified)
            cls.log_safety_event(
                pattern_name=pattern_name,
                rule_triggered="max_newlines",
                original_text=original,
                modified_text=modified
            )
            
        # Replace special tokens
        for old, new in cls._safety_rules["special_tokens"].items():
            if old in modified:
                modified = modified.replace(old, new)
                cls.log_safety_event(
                    pattern_name=pattern_name,
                    rule_triggered=f"special_token_{old}",
                    original_text=original,
                    modified_text=modified
                )
                
        # Remove blocked patterns
        for pattern in cls._safety_rules["blocked_patterns"]:
            matches = re.findall(pattern, modified, re.I | re.M)
            if matches:
                modified = re.sub(pattern, '', modified, flags=re.I | re.M)
                cls.log_safety_event(
                    pattern_name=pattern_name,
                    rule_triggered=f"blocked_pattern_{pattern}",
                    original_text=original,
                    modified_text=modified
                )
                
        return modified
        
    @classmethod
    def get_recent_events(cls, minutes: int = 5) -> List[Dict]:
        """Get recent safety events"""
        cutoff = (datetime.now() - timedelta(minutes=minutes)).isoformat()
        return [e for e in cls._safety_log if e["timestamp"] > cutoff] 