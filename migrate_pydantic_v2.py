#!/usr/bin/env python3
"""
Migration script to update Pydantic v1 code to v2 compatibility.
This script will update imports, function calls, and model structures.
"""

import os
import re
from pathlib import Path

def update_file(file_path: str):
    """Update a single file for Pydantic v2 compatibility."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Update imports
    content = re.sub(
        r'from pydantic import HttpUrl',
        'from pydantic import AnyUrl',
        content
    )
    
    # Update HttpUrl usage to AnyUrl
    content = re.sub(r'\bHttpUrl\b', 'AnyUrl', content)
    
    # Update parse_obj_as to model_validate
    content = re.sub(
        r'parse_obj_as\(([^,]+),\s*([^)]+)\)',
        r'model_validate(\2, from_attributes=True)',
        content
    )
    
    # Update validate_arguments decorator
    content = re.sub(
        r'@validate_arguments\(\)',
        '# @validate_arguments()  # Removed in Pydantic v2',
        content
    )
    
    # Update __root__ fields to use RootModel
    content = re.sub(
        r'class (\w+)\(BaseModel\):\s*\n\s*__root__:\s*([^:]+)',
        r'from pydantic import RootModel\n\nclass \1(RootModel[\2]):',
        content
    )
    
    # Update .dict() calls to .model_dump()
    content = re.sub(r'\.dict\(\)', '.model_dump()', content)
    
    # Update List[...] to list[...] for Python 3.9+ compatibility
    content = re.sub(r'\bList\[', 'list[', content)
    content = re.sub(r'\bDict\[', 'dict[', content)
    content = re.sub(r'\bUnion\[', 'Union[', content)  # Keep Union as is
    
    # Update ValidationError import if needed
    content = re.sub(
        r'from pydantic import ValidationError as PydanticValidationError',
        'from pydantic import ValidationError as PydanticValidationError',
        content
    )
    
    # Only write if content changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {file_path}")
        return True
    return False

def main():
    """Main migration function."""
    print("Starting Pydantic v1 to v2 migration...")
    
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
    
    updated_count = 0
    for file_path in python_files:
        if update_file(file_path):
            updated_count += 1
    
    print(f"\nMigration complete! Updated {updated_count} files.")
    print("\nIMPORTANT: After migration, you should:")
    print("1. Test the code thoroughly")
    print("2. Update any remaining manual validation logic")
    print("3. Check for any runtime errors")
    print("4. Update tests if necessary")

if __name__ == "__main__":
    main()
