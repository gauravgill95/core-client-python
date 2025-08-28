#!/usr/bin/env python3
"""
Fix all remaining syntax errors in the API files.
"""

import os
import re
from pathlib import Path

def fix_file(file_path: str):
    """Fix syntax errors in a single file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Fix broken TypeAdapter calls with missing parameters
    # Pattern: TypeAdapter(Model).validate_python(data, from_attributes=True)
    content = re.sub(
        r'TypeAdapter\(([^)]+)\)\.validate_python\(([^,]+),\s*from_attributes=True\)',
        r'TypeAdapter(\1).validate_python(\2, from_attributes=True)',
        content
    )
    
    # Fix broken TypeAdapter calls with missing data parameter
    # Pattern: TypeAdapter(Model).validate_python(, from_attributes=True)
    content = re.sub(
        r'TypeAdapter\(([^)]+)\)\.validate_python\(\s*,\s*from_attributes=True\)',
        r'TypeAdapter(\1).validate_python({}, from_attributes=True)',
        content
    )
    
    # Fix broken TypeAdapter calls with missing model parameter
    # Pattern: TypeAdapter().validate_python(data, from_attributes=True)
    content = re.sub(
        r'TypeAdapter\(\)\.validate_python\(([^,]+),\s*from_attributes=True\)',
        r'TypeAdapter(Error).validate_python(\1, from_attributes=True)',
        content
    )
    
    # Fix broken model_validate calls that weren't converted properly
    # Pattern: model_validate(data, from_attributes=True)
    content = re.sub(
        r'model_validate\(([^,]+),\s*from_attributes=True\)',
        r'TypeAdapter(About).validate_python(\1, from_attributes=True)',
        content
    )
    
    # Fix broken model_validate calls with missing model
    # Pattern: model_validate(Model, data, from_attributes=True)
    content = re.sub(
        r'model_validate\(([^,]+),\s*([^,]+),\s*from_attributes=True\)',
        r'TypeAdapter(\1).validate_python(\2, from_attributes=True)',
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
    print("Starting to fix all syntax errors...")
    
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

if __name__ == "__main__":
    main()
