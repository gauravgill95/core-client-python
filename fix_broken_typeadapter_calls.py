#!/usr/bin/env python3
"""
Fix all broken TypeAdapter calls in the API files.
This script identifies and fixes the pattern: TypeAdapter(response.json().validate_python(...))
"""

import os
import re
from pathlib import Path

def fix_file(file_path: str):
    """Fix broken TypeAdapter calls in a single file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Fix the broken pattern: TypeAdapter(response.json().validate_python(from_attributes=True))
    # This should be: TypeAdapter(ModelName).validate_python(response.json(), from_attributes=True)
    
    # Pattern 1: TypeAdapter(response.json().validate_python(from_attributes=True))
    content = re.sub(
        r'TypeAdapter\(response\.json\(\)\.validate_python\(from_attributes=True\)\)',
        r'TypeAdapter(Process).validate_python(response.json(), from_attributes=True)',
        content
    )
    
    # Pattern 2: TypeAdapter(response.json().validate_python(from_attributes=True))).data
    content = re.sub(
        r'TypeAdapter\(response\.json\(\)\.validate_python\(from_attributes=True\)\)\)\.data',
        r'TypeAdapter(Process).validate_python(response.json(), from_attributes=True).data',
        content
    )
    
    # Pattern 3: TypeAdapter(response.json().validate_python(from_attributes=True) (missing closing parenthesis)
    content = re.sub(
        r'TypeAdapter\(response\.json\(\)\.validate_python\(from_attributes=True\)',
        r'TypeAdapter(Process).validate_python(response.json(), from_attributes=True',
        content
    )
    
    # Now let's try to be more intelligent and detect what model should be used
    # based on the API endpoint name
    
    # Cluster APIs
    if 'cluster' in file_path.lower():
        content = re.sub(
            r'TypeAdapter\(Process\)\.validate_python\(response\.json\(\), from_attributes=True\)',
            r'TypeAdapter(ClusterNodeList).validate_python(response.json(), from_attributes=True)',
            content
        )
    
    # Filesystem APIs
    elif 'fs_' in file_path.lower():
        content = re.sub(
            r'TypeAdapter\(Process\)\.validate_python\(response\.json\(\), from_attributes=True\)',
            r'TypeAdapter(FilesystemList).validate_python(response.json(), from_attributes=True)',
            content
        )
    
    # Config APIs
    elif 'config' in file_path.lower():
        content = re.sub(
            r'TypeAdapter\(Process\)\.validate_python\(response\.json\(\), from_attributes=True\)',
            r'TypeAdapter(Config).validate_python(response.json(), from_attributes=True)',
            content
        )
    
    # Metrics APIs
    elif 'metrics' in file_path.lower():
        content = re.sub(
            r'TypeAdapter\(Process\)\.validate_python\(response\.json\(\), from_attributes=True\)',
            r'TypeAdapter(Metrics).validate_python(response.json(), from_attributes=True)',
            content
        )
    
    # Session APIs
    elif 'session' in file_path.lower():
        content = re.sub(
            r'TypeAdapter\(Process\)\.validate_python\(response\.json\(\), from_attributes=True\)',
            r'TypeAdapter(SessionCollector).validate_python(response.json(), from_attributes=True)',
            content
        )
    
    # Skills APIs
    elif 'skills' in file_path.lower():
        content = re.sub(
            r'TypeAdapter\(Process\)\.validate_python\(response\.json\(\), from_attributes=True\)',
            r'TypeAdapter(Skills).validate_python(response.json(), from_attributes=True)',
            content
        )
    
    # RTMP APIs
    elif 'rtmp' in file_path.lower():
        content = re.sub(
            r'TypeAdapter\(Process\)\.validate_python\(response\.json\(\), from_attributes=True\)',
            r'TypeAdapter(RtmpList).validate_python(response.json(), from_attributes=True)',
            content
        )
    
    # SRT APIs
    elif 'srt' in file_path.lower():
        content = re.sub(
            r'TypeAdapter\(Process\)\.validate_python\(response\.json\(\), from_attributes=True\)',
            r'TypeAdapter(SrtList).validate_python(response.json(), from_attributes=True)',
            content
        )
    
    # Widget APIs
    elif 'widget' in file_path.lower():
        content = re.sub(
            r'TypeAdapter\(Process\)\.validate_python\(response\.json\(\), from_attributes=True\)',
            r'TypeAdapter(Widget).validate_python(response.json(), from_attributes=True)',
            content
        )
    
    # Log APIs
    elif 'log' in file_path.lower():
        content = re.sub(
            r'TypeAdapter\(Process\)\.validate_python\(response\.json\(\), from_attributes=True\)',
            r'TypeAdapter(Log).validate_python(response.json(), from_attributes=True)',
            content
        )
    
    # Metadata APIs
    elif 'metadata' in file_path.lower():
        content = re.sub(
            r'TypeAdapter\(Process\)\.validate_python\(response\.json\(\), from_attributes=True\)',
            r'TypeAdapter(Metadata).validate_python(response.json(), from_attributes=True)',
            content
        )
    
    # Only write if content changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {file_path}")
        return True
    return False

def main():
    """Main fix function."""
    print("Starting to fix broken TypeAdapter calls...")
    
    # Get the current directory
    current_dir = Path.cwd()
    core_client_dir = current_dir / "core_client"
    
    if not core_client_dir.exists():
        print("Error: core_client directory not found!")
        return
    
    # Find all Python files
    python_files = []
    for root, dirs, files in os.walk(core_client_dir):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    
    print(f"Found {len(python_files)} Python files to process...")
    
    fixed_count = 0
    for file_path in python_files:
        if fix_file(file_path):
            fixed_count += 1
    
    print(f"\nFix complete! Fixed {fixed_count} files.")
    print("\nNote: You may need to manually adjust some model names based on the specific API response type.")

if __name__ == "__main__":
    main()
