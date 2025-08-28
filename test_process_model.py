#!/usr/bin/env python3
"""
Test script to verify the Process model can handle the API response after our fixes.
"""

from core_client.base.models.v3 import Process

def test_process_model():
    """Test if the Process model can handle the API response."""
    try:
        print("🧪 Testing Process model with API response data...")
        
        # Simulate the API response that was causing validation errors
        api_response = {
            "id": "5498e0edcbf04dca8837dc3ea3814c37",
            "waitfor_seconds": 0
        }
        
        print(f"API Response: {api_response}")
        
        # Try to create a Process instance from the API response
        process = Process(**api_response)
        print(f"✅ Process model created successfully!")
        print(f"   ID: {process.id}")
        print(f"   Wait for seconds: {getattr(process, 'waitfor_seconds', 'Not set')}")
        
        return True
        
    except Exception as e:
        print(f"❌ Process model test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_process_model()
