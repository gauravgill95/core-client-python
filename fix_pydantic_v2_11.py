#!/usr/bin/env python3
"""
Fix Pydantic v2.11.7 compatibility issues.
This script updates the code to use the correct validation methods for this version.
"""

import os
import re
from pathlib import Path

def fix_file(file_path: str):
    """Fix a single file for Pydantic v2.11.7 compatibility."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Fix model_validate calls that are missing the model parameter
    # Replace: model_validate(response.json(), from_attributes=True)
    # With: TypeAdapter(ModelClass).validate_python(response.json(), from_attributes=True)
    
    # First, add TypeAdapter import where needed
    if 'model_validate(' in content and 'from pydantic import TypeAdapter' not in content:
        content = re.sub(
            r'from pydantic import model_validate',
            'from pydantic import TypeAdapter',
            content
        )
    
    # Fix model_validate calls that need TypeAdapter
    # Pattern: model_validate(ModelClass, data, from_attributes=True)
    content = re.sub(
        r'model_validate\(([^,]+),\s*([^,]+),\s*from_attributes=True\)',
        r'TypeAdapter(\1).validate_python(\2, from_attributes=True)',
        content
    )
    
    # Fix model_validate calls with just data and from_attributes
    # Pattern: model_validate(data, from_attributes=True)
    content = re.sub(
        r'model_validate\(([^,]+),\s*from_attributes=True\)',
        r'TypeAdapter(About).validate_python(\1, from_attributes=True)',
        content
    )
    
    # Fix RootModel usage - check if RootModel is available
    if 'RootModel' in content:
        # Try to use BaseModel with __root__ for backward compatibility
        content = re.sub(
            r'class (\w+)\(RootModel\[([^\]]+)\]\):',
            r'class \1(BaseModel):\n    __root__: \2',
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
    print("Starting Pydantic v2.11.7 compatibility fixes...")
    
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
