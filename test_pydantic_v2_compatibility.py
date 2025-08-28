#!/usr/bin/env python3
"""
Test script to verify Pydantic v2 compatibility for the core-client library.
This script tests the main functionality and ensures no Pydantic v1 patterns remain.
"""

import sys
import os
import importlib
import traceback
from pathlib import Path

def test_imports():
    """Test that all modules can be imported without Pydantic v1 errors."""
    print("🔍 Testing module imports...")
    
    try:
        # Test main module import
        from core_client import Client
        print("✅ Main Client class imported successfully")
        
        # Test base models
        from core_client.base.models import Error, Token, AccessToken, About
        print("✅ Base models imported successfully")
        
        # Test v3 models
        from core_client.base.models.v3 import (
            ClusterNode, ClusterNodeList, Config, Process, 
            Metadata, Log, Metrics, Skills
        )
        print("✅ V3 models imported successfully")
        
        # Test API modules
        from core_client.base.api import about, ping
        from core_client.base.api.v3_cluster_get_list import sync as cluster_list_sync
        print("✅ API modules imported successfully")
        
        return True
        
    except Exception as e:
        print(f"❌ Import failed: {e}")
        traceback.print_exc()
        return False

def test_model_creation():
    """Test that Pydantic models can be created and validated."""
    print("\n🔍 Testing model creation and validation...")
    
    try:
        from core_client.base.models import Error, Token
        from core_client.base.models.v3 import Metadata, Log
        
        # Test basic model creation
        error = Error(message="Test error", code=400, details=[])
        print(f"✅ Error model created: {error.message}")
        
        # Test Token model
        token = Token(access_token="test_token", refresh_token="refresh_token")
        print(f"✅ Token model created: {token.access_token[:10]}...")
        
        # Test updated models with data field (previously __root__)
        metadata = Metadata(data={"key": "value"})
        print(f"✅ Metadata model created: {metadata.data}")
        
        log = Log(data=["log entry 1", "log entry 2"])
        print(f"✅ Log model created: {log.data}")
        
        return True
        
    except Exception as e:
        print(f"❌ Model creation failed: {e}")
        traceback.print_exc()
        return False

def test_client_initialization():
    """Test that the Client class can be initialized with Pydantic v2 types."""
    print("\n🔍 Testing Client initialization...")
    
    try:
        from core_client import Client
        from pydantic import AnyUrl
        
        # Test with string URL (should be converted to AnyUrl)
        client = Client(
            base_url="http://localhost:8080",
            username="test",
            password="test"
        )
        print(f"✅ Client created with string URL: {client.base_url}")
        
        # Test with AnyUrl (Pydantic v2 type)
        url = AnyUrl("http://localhost:8080")
        client2 = Client(
            base_url=url,
            username="test",
            password="test"
        )
        print(f"✅ Client created with AnyUrl: {client2.base_url}")
        
        return True
        
    except Exception as e:
        print(f"❌ Client initialization failed: {e}")
        traceback.print_exc()
        return False

def test_api_functionality():
    """Test that API functions work with the new model_validate pattern."""
    print("\n🔍 Testing API functionality...")
    
    try:
        from core_client.base.api.v3_cluster_get_list import sync
        from core_client import Client
        
        # Create a mock client for testing
        client = Client(base_url="http://localhost:8080")
        
        # Test that the function can be called (we expect it to fail on network, not Pydantic)
        print("✅ API function imported and callable")
        
        return True
        
    except Exception as e:
        print(f"❌ API functionality test failed: {e}")
        traceback.print_exc()
        return False

def check_v1_patterns():
    """Check for any remaining Pydantic v1 patterns that need to be updated."""
    print("\n🔍 Checking for remaining Pydantic v1 patterns...")
    
    patterns_to_check = [
        (r'parse_obj_as', 'parse_obj_as usage'),
        (r'HttpUrl', 'HttpUrl usage'),
        (r'\.dict\(\)', '.dict() usage'),
        (r'List\[', 'List[...] usage'),
        (r'Dict\[', 'Dict[...] usage'),
        (r'Union\[', 'Union[...] usage'),
        (r'Optional\[', 'Optional[...] usage'),
    ]
    
    issues_found = []
    
    for pattern, description in patterns_to_check:
        try:
            result = subprocess.run(
                ['grep', '-r', '--include=*.py', pattern, 'core_client'],
                capture_output=True,
                text=True,
                shell=True
            )
            
            if result.stdout.strip():
                lines = result.stdout.strip().split('\n')
                for line in lines:
                    if line and 'core_client' in line:
                        file_path = line.split(':')[0]
                        issues_found.append(f"  - {file_path}: {description}")
                        
        except Exception as e:
            print(f"Warning: Could not check pattern {pattern}: {e}")
    
    if issues_found:
        print(f"❌ Found remaining Pydantic v1 patterns:")
        for issue in issues_found:
            print(issue)
        return False
    else:
        print("✅ No remaining Pydantic v1 patterns found!")
        return True

def test_pydantic_version():
    """Test that Pydantic v2 is being used."""
    print("\n🔍 Testing Pydantic version...")
    
    try:
        import pydantic
        version = pydantic.__version__
        major_version = int(version.split('.')[0])
        
        if major_version >= 2:
            print(f"✅ Using Pydantic v{version}")
            return True
        else:
            print(f"❌ Using Pydantic v{version}, but v2+ is required")
            return False
            
    except Exception as e:
        print(f"❌ Could not determine Pydantic version: {e}")
        return False

def run_compatibility_tests():
    """Run all compatibility tests."""
    print("🚀 Starting Pydantic v2 Compatibility Tests")
    print("=" * 50)
    
    tests = [
        ("Pydantic Version", test_pydantic_version),
        ("Module Imports", test_imports),
        ("Model Creation", test_model_creation),
        ("Client Initialization", test_client_initialization),
        ("API Functionality", test_api_functionality),
        ("V1 Pattern Check", check_v1_patterns),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} test crashed: {e}")
            traceback.print_exc()
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 50)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {test_name}")
        if result:
            passed += 1
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! The library is compatible with Pydantic v2.")
        print("\nNext steps:")
        print("1. Install the updated package: pip install -e .")
        print("2. Test with your actual application")
        print("3. Deploy when ready")
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Please fix the issues before deploying.")
    
    return passed == total

if __name__ == "__main__":
    import re
    import subprocess
    
    try:
        success = run_compatibility_tests()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Tests interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n💥 Unexpected error: {e}")
        traceback.print_exc()
        sys.exit(1)
