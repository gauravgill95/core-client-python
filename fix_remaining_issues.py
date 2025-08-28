#!/usr/bin/env python3
"""
Fix remaining Pydantic v1 issues that weren't caught by the migration script.
"""

import os
import re
from pathlib import Path

def fix_parse_obj_as_imports(file_path: str):
    """Fix parse_obj_as imports and usage in a single file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Fix imports - replace parse_obj_as with model_validate
    content = re.sub(
        r'from pydantic import parse_obj_as, validate_arguments',
        'from pydantic import model_validate',
        content
    )
    
    # Fix imports - replace just parse_obj_as
    content = re.sub(
        r'from pydantic import parse_obj_as',
        'from pydantic import model_validate',
        content
    )
    
    # Fix validate_arguments decorator usage
    content = re.sub(
        r'@validate_arguments\(\)',
        '# @validate_arguments()  # Removed in Pydantic v2',
        content
    )
    
    # Fix parse_obj_as function calls
    content = re.sub(
        r'parse_obj_as\(([^,]+),\s*([^)]+)\)',
        r'model_validate(\1, \2, from_attributes=True)',
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
    print("Starting to fix remaining parse_obj_as issues...")
    
    # Get the current directory
    current_dir = Path.cwd()
    core_client_dir = current_dir / "core_client"
    
    if not core_client_dir.exists():
        print("Error: core_client directory not found!")
        return
    
    # Find all Python files that still have parse_obj_as
    python_files = []
    for root, dirs, files in os.walk(core_client_dir):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    if 'parse_obj_as' in f.read():
                        python_files.append(file_path)
    
    print(f"Found {len(python_files)} Python files with parse_obj_as to fix...")
    
    fixed_count = 0
    for file_path in python_files:
        if fix_parse_obj_as_imports(file_path):
            fixed_count += 1
    
    print(f"\nFix complete! Fixed {fixed_count} files.")
    print("\nNext steps:")
    print("1. Test the code to ensure it works")
    print("2. Install the updated package")
    print("3. Run your application to verify compatibility")

if __name__ == "__main__":
    main()
