#!/usr/bin/env python3
"""
Quick integration test for basic connectivity and authentication.
Run this first to verify basic connectivity before running the full test suite.
"""

import traceback
from core_client import Client

# Configuration
RESTREAMER_URL = "https://stream.cataloghub.in"
CREDENTIALS = {
    "username": "admin",
    "password": "datarhei"
}

def test_basic_connectivity():
    """Test basic connectivity and authentication."""
    print("🚀 Quick Integration Test")
    print("=" * 40)
    print(f"Target: {RESTREAMER_URL}")
    print(f"Username: {CREDENTIALS['username']}")
    print("=" * 40)
    
    try:
        # Test 1: Client Creation
        print("\n🔧 Test 1: Creating client...")
        client = Client(
            base_url=RESTREAMER_URL,
            username=CREDENTIALS["username"],
            password=CREDENTIALS["password"]
        )
        print(f"✅ Client created successfully: {client.base_url}")
        
        # Test 2: Authentication
        print("\n🔐 Test 2: Testing authentication...")
        token = client.login()
        if token.access_token:
            print(f"✅ Authentication successful!")
            print(f"   Access token: {token.access_token[:30]}...")
            print(f"   Refresh token: {token.refresh_token[:30] if token.refresh_token else 'None'}...")
            print(f"   Expires at: {token.expires_at if hasattr(token, 'expires_at') else 'Unknown'}")
        else:
            print("❌ Authentication failed: No access token received")
            return False
        
        # Test 3: Basic API Call
        print("\n🌐 Test 3: Testing basic API call...")
        from core_client.base.api.about import sync as about_sync
        about_response = about_sync(client)
        if about_response:
            print("✅ About API call successful!")
            if hasattr(about_response, 'auths'):
                print(f"   Available auth methods: {about_response.auths}")
        else:
            print("❌ About API call failed")
            return False
        
        # Test 4: Ping API
        print("\n🏓 Test 4: Testing ping API...")
        from core_client.base.api.ping import sync as ping_sync
        ping_response = ping_sync(client)
        if ping_response:
            print("✅ Ping API call successful!")
            print(f"   Response: {ping_response}")
        else:
            print("❌ Ping API call failed")
            return False
        
        print("\n" + "=" * 40)
        print("🎉 All basic tests passed!")
        print("✅ Client creation: OK")
        print("✅ Authentication: OK")
        print("✅ About API: OK")
        print("✅ Ping API: OK")
        print("\nReady to run the full integration test suite!")
        return True
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        traceback.print_exc()
        return False

def test_specific_api(api_name, api_module, api_function):
    """Test a specific API endpoint."""
    try:
        print(f"\n🔍 Testing {api_name}...")
        
        client = Client(
            base_url=RESTREAMER_URL,
            username=CREDENTIALS["username"],
            password=CREDENTIALS["password"]
        )
        
        # Authenticate first
        client.login()
        
        # Import and test the API
        module = __import__(api_module, fromlist=[api_function])
        func = getattr(module, api_function)
        
        response = func(client)
        if response:
            print(f"✅ {api_name} successful!")
            if hasattr(response, 'data'):
                print(f"   Data length: {len(response.data) if response.data else 0}")
            return True
        else:
            print(f"❌ {api_name} failed: No response")
            return False
            
    except Exception as e:
        print(f"❌ {api_name} failed: {e}")
        return False

def main():
    """Main function."""
    print("Choose test mode:")
    print("1. Quick connectivity test (recommended first)")
    print("2. Test specific API endpoints")
    print("3. Run full integration test suite")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        test_basic_connectivity()
    elif choice == "2":
        print("\nAvailable API tests:")
        print("1. Cluster list")
        print("2. Configuration")
        print("3. Filesystem")
        print("4. Processes")
        print("5. Metrics")
        
        api_choice = input("Enter API test number (1-5): ").strip()
        
        api_tests = {
            "1": ("Cluster List", "core_client.base.api.v3_cluster_get_list", "sync"),
            "2": ("Configuration", "core_client.base.api.v3_config_get", "sync"),
            "3": ("Filesystem", "core_client.base.api.v3_fs_get_list", "sync"),
            "4": ("Processes", "core_client.base.api.v3_process_get_list", "sync"),
            "5": ("Metrics", "core_client.base.api.v3_metrics_get", "sync"),
        }
        
        if api_choice in api_tests:
            name, module, func = api_tests[api_choice]
            test_specific_api(name, module, func)
        else:
            print("Invalid choice!")
            
    elif choice == "3":
        print("\nRunning full integration test suite...")
        from integration_test import main as run_full_tests
        run_full_tests()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
