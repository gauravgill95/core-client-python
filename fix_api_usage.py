#!/usr/bin/env python3
"""
Fix API usage to work with the updated model fields.
"""

import os
import re
from pathlib import Path

def fix_file(file_path: str):
    """Fix API usage in a single file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Fix .__root__ references to .data
    content = re.sub(r'\.__root__', '.data', content)
    
    # Fix dict()["__root__"] references to dict()["data"]
    content = re.sub(r'dict\(\)\["__root__"\]', 'dict()["data"]', content)
    
    # Only write if content changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {file_path}")
        return True
    return False

def main():
    """Main fix function."""
    print("Starting to fix API usage...")
    
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
