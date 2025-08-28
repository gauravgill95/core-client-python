#!/usr/bin/env python3
"""
Comprehensive fix for Pydantic v2 compatibility issues.
This script fixes the remaining problems after the initial migration.
"""

import os
import re
from pathlib import Path

def fix_file(file_path: str):
    """Fix a single file for Pydantic v2 compatibility."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Fix broken parse_obj_as calls that weren't properly converted
    content = re.sub(
        r'model_validate\(response\.json\(\),\s*from_attributes=True\)',
        r'model_validate(ClusterNodeList, response.json(), from_attributes=True)',
        content
    )
    
    # Fix broken parse_obj_as calls with missing model parameter
    content = re.sub(
        r'model_validate\(([^,]+),\s*([^)]+),\s*from_attributes=True\)',
        r'model_validate(\1, \2, from_attributes=True)',
        content
    )
    
    # Fix any remaining parse_obj_as calls that weren't converted
    content = re.sub(
        r'parse_obj_as\(([^,]+),\s*([^)]+)\)',
        r'model_validate(\1, \2, from_attributes=True)',
        content
    )
    
    # Fix broken model_validate calls with missing model parameter
    content = re.sub(
        r'model_validate\(([^,]+),\s*from_attributes=True\)',
        r'model_validate(\1, from_attributes=True)',
        content
    )
    
    # Fix any remaining __root__ patterns that weren't converted
    content = re.sub(
        r'class (\w+)\(BaseModel\):\s*\n\s*__root__:\s*([^:]+)',
        r'from pydantic import RootModel\n\nclass \1(RootModel[\2]):\n    pass',
        content
    )
    
    # Fix broken RootModel syntax
    content = re.sub(
        r'class (\w+)\(RootModel\[([^\]]+)\s*\n\s*\]\):',
        r'class \1(RootModel[\2]):\n    pass',
        content
    )
    
    # Remove duplicate imports
    content = re.sub(
        r'from pydantic import BaseModel\nfrom pydantic import RootModel',
        r'from pydantic import RootModel',
        content
    )
    
    # Fix any remaining syntax issues with model_validate
    content = re.sub(
        r'model_validate\(([^,]+),\s*([^)]+),\s*from_attributes=True\)',
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
    print("Starting comprehensive Pydantic v2 compatibility fixes...")
    
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
    print("\nNext steps:")
    print("1. Test the code to ensure it works")
    print("2. Install the updated package")
    print("3. Run your application to verify compatibility")

if __name__ == "__main__":
    main()
