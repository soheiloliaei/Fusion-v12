# Fusion Release Process Guide

This document outlines the standardized process for releasing new versions of Fusion. Follow these steps for every release to ensure consistency and completeness.

## 1. Launch Command File Update

### Required Updates
- [ ] Update features to match new version
- [ ] Make launcher fully self-contained
- [ ] Ensure dependency-free setup
- [ ] Add/update mode selection
- [ ] Add/update chain templates

### Verification
- [ ] Test self-contained execution
- [ ] Verify all dependencies are handled
- [ ] Test all execution modes
- [ ] Validate chain templates
- [ ] Check error handling

## 2. ChatGPT Upload Package

### Package Creation
- [ ] Create `ChatGPT_Upload_vX.X` directory
- [ ] Update master prompt with new features
- [ ] Add/update configuration files
- [ ] Select and verify essential files
- [ ] Create upload instructions

### Required Files
```
ChatGPT_Upload_vX.X/
├── MASTER_PROMPT.md
├── README.md
├── UPLOAD_CHECKLIST.md
├── requirements.txt
├── fusion_vX.X_config.json
├── core/
│   ├── pattern_base.py
│   ├── pattern_safety.py
│   ├── prompt_patterns.py
│   └── prompt_pattern_registry.py
├── agents/
│   ├── agent_chain.py
│   └── evaluator_metrics.py
├── system/
│   ├── memory_registry.py
│   ├── pattern_stats.py
│   └── fusion_cli.py
└── chain_templates/
    ├── provocation_loop.json
    ├── critique_strategy.json
    └── rewrite_evolution.json
```

### Verification Steps
- [ ] Test file upload order
- [ ] Verify all imports resolve
- [ ] Test each component
- [ ] Check configuration
- [ ] Validate templates

## 3. GitHub Updates

### Repository Updates
- [ ] Push all code changes
- [ ] Update documentation
- [ ] Tag new version
- [ ] Create release notes
- [ ] Package ChatGPT upload files

### File Management
- [ ] List new files added
- [ ] List files updated
- [ ] List files deprecated/removed
- [ ] Update import references
- [ ] Check dependency changes

### Release Notes Template
```markdown
# Fusion vX.X Release

## New Features
- Feature 1
- Feature 2
...

## Updates
- Update 1
- Update 2
...

## File Changes
### Added
- file1.py: Description
- file2.py: Description

### Updated
- file3.py: Changes made
- file4.py: Changes made

### Removed
- file5.py: Reason for removal
- file6.py: Reason for removal

## Migration Guide
Steps to update from previous version...

## ChatGPT Package
Instructions for ChatGPT upload...
```

## Release Checklist

1. **Pre-Release**
   - [ ] Update version numbers
   - [ ] Run all tests
   - [ ] Update documentation
   - [ ] Check dependencies

2. **Launch Command**
   - [ ] Update features
   - [ ] Test self-contained
   - [ ] Verify modes
   - [ ] Check templates

3. **ChatGPT Package**
   - [ ] Create directory
   - [ ] Update files
   - [ ] Test upload
   - [ ] Verify functionality

4. **GitHub**
   - [ ] Push changes
   - [ ] Create tag
   - [ ] Write release notes
   - [ ] Upload package

5. **Post-Release**
   - [ ] Verify downloads
   - [ ] Test installations
   - [ ] Check documentation
   - [ ] Update roadmap

## Version Numbering

- Major.Minor.Patch (e.g., v12.0.1)
- Major: Significant changes
- Minor: New features
- Patch: Bug fixes

## Support Files

Each release should include:
1. Updated launch command
2. ChatGPT upload package
3. Release notes
4. Migration guide
5. Test files
6. Example templates

## Quality Standards

1. **Code Quality**
   - All tests passing
   - No linter errors
   - Documentation updated
   - Examples working

2. **Package Quality**
   - All files present
   - Dependencies resolved
   - Instructions clear
   - Tests included

3. **Documentation Quality**
   - Features documented
   - Examples provided
   - Changes explained
   - Migration steps clear

## Emergency Fixes

If emergency fixes are needed:
1. Create hotfix branch
2. Fix issue
3. Update patch version
4. Create release notes
5. Update ChatGPT package
6. Push changes
7. Tag release 