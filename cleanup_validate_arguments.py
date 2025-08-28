#!/usr/bin/env python3
"""
Clean up all remaining validate_arguments decorators and RootModel patterns.
"""

import os
import re
from pathlib import Path

def fix_file(file_path: str):
    """Fix a single file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Remove all validate_arguments decorators
    content = re.sub(
        r'# # @validate_arguments\(\)  # Removed in Pydantic v2  # Removed in Pydantic v2\n',
        '',
        content
    )
    
    # Remove any remaining validate_arguments decorators
    content = re.sub(
        r'# @validate_arguments\(\)  # Removed in Pydantic v2\n',
        '',
        content
    )
    
    # Remove any remaining RootModel patterns
    content = re.sub(
        r'RootModel pattern',
        'data field pattern',
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
    print("Starting to clean up validate_arguments decorators...")
    
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
