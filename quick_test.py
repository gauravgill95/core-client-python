#!/usr/bin/env python3
"""
Quick test script for basic Pydantic v2 compatibility.
Run this first to get a quick overview of any major issues.
"""

def quick_import_test():
    """Quick test of basic imports."""
    print("🔍 Quick import test...")
    
    try:
        # Test basic import
        from core_client import Client
        print("✅ Client import: OK")
        
        # Test model imports
        from core_client.base.models import Error
        print("✅ Error model import: OK")
        
        # Test v3 model imports
        from core_client.base.models.v3 import Metadata, Log
        print("✅ V3 models import: OK")
        
        # Test API import
        from core_client.base.api.v3_cluster_get_list import sync
        print("✅ API import: OK")
        
        print("\n🎉 All basic imports successful!")
        return True
        
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False

def quick_model_test():
    """Quick test of model creation."""
    print("\n🔍 Quick model test...")
    
    try:
        from core_client.base.models import Error
        from core_client.base.models.v3 import Metadata
        
        # Test basic model
        error = Error(message="test", code=400, details=[])
        print("✅ Error model creation: OK")
        
        # Test updated model with data field
        metadata = Metadata(data={"test": "value"})
        print("✅ Metadata model creation: OK")
        
        print("🎉 All basic model tests successful!")
        return True
        
    except Exception as e:
        print(f"❌ Model test failed: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Quick Pydantic v2 Compatibility Test")
    print("=" * 40)
    
    import_ok = quick_import_test()
    model_ok = quick_model_test()
    
    if import_ok and model_ok:
        print("\n🎉 Quick test passed! Run the full test script for comprehensive testing.")
    else:
        print("\n⚠️  Quick test failed. Check the errors above.")
