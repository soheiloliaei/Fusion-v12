#!/usr/bin/env python3
"""
Fusion v11 Project Deployment Script
Applies Fusion v11 to any project (new or existing) with complete automation.

Usage:
    python deploy_fusion_v11_to_projects.py --new "ProjectName" --type "design_innovation"
    python deploy_fusion_v11_to_projects.py --existing "/path/to/project"
    python deploy_fusion_v11_to_projects.py --batch projects_list.json
"""

import argparse
import json
import os
import shutil
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional

# Import your foundation system
try:
    sys.path.append(os.path.join(os.path.dirname(__file__), "01_Core_Infrastructure"))
    from fusion_v11_foundation import FusionV11Foundation, ProjectScaffolding
except ImportError:
    print("❌ Could not import fusion_v11_foundation. Make sure it's in your Python path.")
    print("    Expected location: 01_Core_Infrastructure/fusion_v11_foundation.py")
    sys.exit(1)


class FusionV11Deployer:
    """Deploy Fusion v11 to any project with complete automation."""
    
    def __init__(self):
        self.source_v11_path = Path("01_Core_Infrastructure/Fusion_v11_Complete_10_Files")
        self.deployments_log = []
        
    def deploy_to_new_project(self, project_name: str, project_type: str = "design_innovation", 
                             target_directory: Optional[str] = None) -> Dict[str, Any]:
        """Deploy Fusion v11 to a new project."""
        
        print(f"\n🚀 CREATING NEW PROJECT: {project_name}")
        print(f"📋 Type: {project_type}")
        print("-" * 50)
        
        try:
            # Use target directory if provided, otherwise use default
            if target_directory:
                original_cwd = os.getcwd()
                os.chdir(target_directory)
            
            # Create foundation
            foundation = ProjectScaffolding.create_new_fusion_v11_project(
                project_name=project_name,
                project_type=project_type
            )
            
            # Validate system
            health = foundation.validate_system_health()
            
            # Get upload package info
            upload_info = foundation.get_chatgpt_upload_package()
            
            # Generate report
            report = foundation.generate_project_report()
            
            # Log deployment
            deployment_result = {
                "project_name": project_name,
                "project_type": project_type,
                "deployment_type": "new_project",
                "status": "success",
                "health_check": health,
                "upload_package": upload_info,
                "setup_report": report
            }
            
            self.deployments_log.append(deployment_result)
            
            print(f"✅ SUCCESS: {project_name} created with full Fusion v11 infrastructure")
            print(f"📁 Location: Projects/{project_name}")
            print(f"🤖 ChatGPT Package: {upload_info['source_location']}")
            
            if target_directory:
                os.chdir(original_cwd)
                
            return deployment_result
            
        except Exception as e:
            print(f"❌ ERROR: Failed to create {project_name}: {str(e)}")
            return {"project_name": project_name, "status": "failed", "error": str(e)}
    
    def deploy_to_existing_project(self, project_path_str: str, project_type: str = "design_innovation") -> Dict[str, Any]:
        """Deploy Fusion v11 to an existing project."""
        
        project_path = Path(project_path_str)
        project_name = project_path.name
        
        print(f"\n🔄 UPGRADING EXISTING PROJECT: {project_name}")
        print(f"📂 Path: {project_path}")
        print(f"📋 Type: {project_type}")
        print("-" * 50)
        
        try:
            # Validate project exists
            if not project_path.exists():
                raise ValueError(f"Project path does not exist: {project_path}")
            
            # Create Core Infrastructure directory
            core_infra_path = project_path / "01_Core_Infrastructure"
            core_infra_path.mkdir(exist_ok=True)
            
            # Copy Fusion v11 Complete 10 Files
            v11_target_path = core_infra_path / "Fusion_v11_Complete_10_Files"
            if self.source_v11_path.exists():
                shutil.copytree(self.source_v11_path, v11_target_path, dirs_exist_ok=True)
                print(f"✅ Copied Fusion v11 Complete system to {v11_target_path}")
            else:
                print(f"⚠️  Warning: Source v11 files not found at {self.source_v11_path}")
            
            # Initialize foundation
            foundation = FusionV11Foundation(project_name, project_type)
            
            # Create project configuration
            config_path = project_path / "project_config.json"
            with open(config_path, 'w') as f:
                json.dump(foundation.v11_config, f, indent=2)
            print(f"✅ Created configuration: {config_path}")
            
            # Generate setup guide
            setup_guide_path = project_path / f"{project_name}_FUSION_V11_SETUP.md"
            with open(setup_guide_path, 'w') as f:
                f.write(foundation.generate_project_report())
            print(f"✅ Created setup guide: {setup_guide_path}")
            
            # Create upgrade script
            upgrade_script_path = project_path / "fusion_v11_upgrade.py"
            upgrade_script_content = f'''"""
Fusion v11 Upgrade Script for {project_name}
Generated automatically by deployment system.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fusion_v11_foundation import FusionV11Foundation

# Initialize foundation for this project
foundation = FusionV11Foundation("{project_name}", "{project_type}")

# Validate system health
health = foundation.validate_system_health()
print("System Health Check:")
for check, status in health.items():
    print(f"{{status}} {{check}}")

# Get ChatGPT upload package
upload_info = foundation.get_chatgpt_upload_package()
print(f"\\n📁 ChatGPT Upload Package: {{upload_info['source_location']}}")
print("Upload these 10 files to ChatGPT:")
for file in upload_info['upload_sequence']:
    print(f"✅ {{file}}")

print("\\n🚀 {project_name} is now Fusion v11 ready!")
'''
            
            with open(upgrade_script_path, 'w') as f:
                f.write(upgrade_script_content)
            print(f"✅ Created upgrade script: {upgrade_script_path}")
            
            # Validate system
            health = foundation.validate_system_health()
            upload_info = foundation.get_chatgpt_upload_package()
            
            # Log deployment
            deployment_result = {
                "project_name": project_name,
                "project_path": str(project_path),
                "project_type": project_type,
                "deployment_type": "existing_project",
                "status": "success",
                "health_check": health,
                "upload_package": upload_info,
                "files_created": [
                    str(config_path),
                    str(setup_guide_path),
                    str(upgrade_script_path)
                ]
            }
            
            self.deployments_log.append(deployment_result)
            
            print(f"✅ SUCCESS: {project_name} upgraded to Fusion v11")
            print(f"🤖 ChatGPT Package: {upload_info['source_location']}")
            
            return deployment_result
            
        except Exception as e:
            print(f"❌ ERROR: Failed to upgrade {project_name}: {str(e)}")
            return {"project_name": project_name, "status": "failed", "error": str(e)}
    
    def batch_deploy(self, projects_config: List[Dict[str, str]]) -> List[Dict[str, Any]]:
        """Deploy Fusion v11 to multiple projects."""
        
        print(f"\n🚀 BATCH DEPLOYMENT: {len(projects_config)} PROJECTS")
        print("=" * 60)
        
        results = []
        
        for project in projects_config:
            if project.get("existing_path"):
                # Existing project
                result = self.deploy_to_existing_project(
                    project["existing_path"],
                    project.get("type", "design_innovation")
                )
            else:
                # New project
                result = self.deploy_to_new_project(
                    project["name"],
                    project.get("type", "design_innovation"),
                    project.get("target_directory")
                )
            
            results.append(result)
        
        # Summary
        successful = [r for r in results if r.get("status") == "success"]
        failed = [r for r in results if r.get("status") == "failed"]
        
        print(f"\n📊 BATCH DEPLOYMENT SUMMARY:")
        print(f"✅ Successful: {len(successful)}")
        print(f"❌ Failed: {len(failed)}")
        
        if failed:
            print("\nFailed deployments:")
            for failure in failed:
                print(f"❌ {failure['project_name']}: {failure.get('error', 'Unknown error')}")
        
        return results
    
    def generate_deployment_report(self) -> str:
        """Generate comprehensive deployment report."""
        
        if not self.deployments_log:
            return "No deployments recorded."
        
        successful = [d for d in self.deployments_log if d.get("status") == "success"]
        failed = [d for d in self.deployments_log if d.get("status") == "failed"]
        
        report = f"""
# 🚀 FUSION V11 DEPLOYMENT REPORT

## 📊 DEPLOYMENT SUMMARY
- **Total Projects**: {len(self.deployments_log)}
- **Successful**: {len(successful)}
- **Failed**: {len(failed)}
- **Success Rate**: {len(successful)/len(self.deployments_log)*100:.1f}%

## ✅ SUCCESSFUL DEPLOYMENTS
"""
        
        for deployment in successful:
            report += f"""
### {deployment['project_name']}
- **Type**: {deployment['project_type']}
- **Deployment**: {deployment['deployment_type']}
- **Status**: {deployment['status']}
- **System Health**: {deployment['health_check']['system_readiness']}
- **ChatGPT Package**: {deployment['upload_package']['source_location']}
"""
        
        if failed:
            report += f"""

## ❌ FAILED DEPLOYMENTS
"""
            for failure in failed:
                report += f"""
### {failure['project_name']}
- **Error**: {failure.get('error', 'Unknown error')}
"""
        
        report += f"""

## 🎯 NEXT STEPS
1. **Upload to ChatGPT**: Each project has 10-file package ready
2. **Activate Agents**: Use provided activation prompts
3. **Test Integration**: Validate with test prompts
4. **Begin Work**: Start using Fusion v11 for design excellence

## 💪 CAPABILITIES ENABLED
- **Design Excellence**: 4-dimensional tracking across all projects
- **Strategic Innovation**: 7 frameworks + 5 personality perspectives
- **ChatGPT Ready**: Optimized for 10-file upload limit
- **Production Ready**: Professional-grade quality assurance

**All projects now operate at Fusion v11 excellence standards!**
"""
        
        return report


def main():
    """Main CLI interface for Fusion v11 deployment."""
    
    parser = argparse.ArgumentParser(
        description="Deploy Fusion v11 to any project (new or existing)"
    )
    
    parser.add_argument("--new", help="Create new project with this name")
    parser.add_argument("--type", default="design_innovation", 
                       help="Project type (design_innovation, product_innovation, etc.)")
    parser.add_argument("--existing", help="Path to existing project to upgrade")
    parser.add_argument("--batch", help="JSON file with list of projects to deploy")
    parser.add_argument("--target-dir", help="Target directory for new projects")
    parser.add_argument("--report", action="store_true", help="Generate deployment report")
    
    args = parser.parse_args()
    
    deployer = FusionV11Deployer()
    
    if args.new:
        # New project
        result = deployer.deploy_to_new_project(args.new, args.type, args.target_dir)
        
    elif args.existing:
        # Existing project
        result = deployer.deploy_to_existing_project(args.existing, args.type)
        
    elif args.batch:
        # Batch deployment
        with open(args.batch, 'r') as f:
            projects_config = json.load(f)
        
        results = deployer.batch_deploy(projects_config)
        
    else:
        # Interactive mode
        print("\n🚀 FUSION V11 DEPLOYMENT SYSTEM")
        print("=" * 40)
        print("1. New project")
        print("2. Existing project")
        print("3. Batch deployment")
        print("4. Exit")
        
        choice = input("\nSelect option (1-4): ")
        
        if choice == "1":
            name = input("Project name: ")
            project_type = input("Project type (design_innovation): ") or "design_innovation"
            result = deployer.deploy_to_new_project(name, project_type)
            
        elif choice == "2":
            path = input("Path to existing project: ")
            project_type = input("Project type (design_innovation): ") or "design_innovation"
            result = deployer.deploy_to_existing_project(path, project_type)
            
        elif choice == "3":
            config_file = input("Path to projects config JSON: ")
            with open(config_file, 'r') as f:
                projects_config = json.load(f)
            results = deployer.batch_deploy(projects_config)
            
        else:
            print("👋 Goodbye!")
            return
    
    # Generate and save report
    if args.report or deployer.deployments_log:
        report = deployer.generate_deployment_report()
        
        report_file = "fusion_v11_deployment_report.md"
        with open(report_file, 'w') as f:
            f.write(report)
        
        print(f"\n📄 Deployment report saved: {report_file}")
        print("\n" + "=" * 60)
        print("🎯 FUSION V11 DEPLOYMENT COMPLETE")
        print("All projects now have design excellence capabilities!")


if __name__ == "__main__":
    main() 