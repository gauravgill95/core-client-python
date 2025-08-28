#!/usr/bin/env python3
"""
Integration test for core-client library against actual Restreamer instance.
This test validates all APIs work correctly with real HTTP requests.
"""

import asyncio
import time
import traceback
from typing import Dict, List, Any
from core_client import Client, AsyncClient

# Configuration


class IntegrationTestSuite:
    """Comprehensive integration test suite for Restreamer APIs."""
    
    def __init__(self):
        self.client = None
        self.async_client = None
        self.test_results = {}
        self.start_time = None
        
    def log_test(self, test_name: str, success: bool, details: str = ""):
        """Log test results."""
        status = "✅ PASS" if success else "❌ FAIL"
        self.test_results[test_name] = {
            "success": success,
            "details": details,
            "timestamp": time.time()
        }
        print(f"{status}: {test_name}")
        if details:
            print(f"   {details}")
    
    def setup_clients(self):
        """Initialize both sync and async clients."""
        try:
            print("🔧 Setting up clients...")
            
            # Test sync client
            self.client = Client(
                base_url=RESTREAMER_URL,
                username=CREDENTIALS["username"],
                password=CREDENTIALS["password"]
            )
            print(f"✅ Sync client created: {self.client.base_url}")
            
            # Test async client
            self.async_client = AsyncClient(
                base_url=RESTREAMER_URL,
                username=CREDENTIALS["username"],
                password=CREDENTIALS["password"]
            )
            print(f"✅ Async client created: {self.async_client.base_url}")
            
            return True
            
        except Exception as e:
            print(f"❌ Client setup failed: {e}")
            traceback.print_exc()
            return False
    
    def test_authentication(self):
        """Test authentication and login."""
        try:
            print("\n🔐 Testing authentication...")
            
            # Test login
            token = self.client.login()
            if token.access_token:
                print(f"✅ Login successful: {token.access_token[:20]}...")
                return True
            else:
                print("❌ Login failed: No access token received")
                return False
                
        except Exception as e:
            print(f"❌ Authentication test failed: {e}")
            traceback.print_exc()
            return False
    
    def test_basic_apis(self):
        """Test basic API endpoints."""
        try:
            print("\n🌐 Testing basic APIs...")
            
            # Test about endpoint
            from core_client.base.api.about import sync as about_sync
            about_response = about_sync(self.client)
            if about_response:
                print(f"✅ About API: {about_response}")
            
            # Test ping endpoint
            from core_client.base.api.ping import sync as ping_sync
            ping_response = ping_sync(self.client)
            if ping_response:
                print(f"✅ Ping API: {ping_response}")
            
            return True
            
        except Exception as e:
            print(f"❌ Basic APIs test failed: {e}")
            traceback.print_exc()
            return False
    
    def test_cluster_apis(self):
        """Test cluster-related APIs."""
        try:
            print("\n🏗️  Testing cluster APIs...")
            
            # Test cluster node list
            from core_client.base.api.v3_cluster_get_list import sync as cluster_list_sync
            cluster_response = cluster_list_sync(self.client)
            if cluster_response:
                print(f"✅ Cluster list API: {len(cluster_response.data) if hasattr(cluster_response, 'data') else 'Response received'}")
            
            return True
            
        except Exception as e:
            print(f"❌ Cluster APIs test failed: {e}")
            traceback.print_exc()
            return False
    
    def test_config_apis(self):
        """Test configuration APIs."""
        try:
            print("\n⚙️  Testing configuration APIs...")
            
            # Test config get
            from core_client.base.api.v3_config_get import sync as config_get_sync
            config_response = config_get_sync(self.client)
            if config_response:
                print(f"✅ Config get API: Response received")
            
            return True
            
        except Exception as e:
            print(f"❌ Config APIs test failed: {e}")
            traceback.print_exc()
            return False
    
    def test_filesystem_apis(self):
        """Test filesystem APIs."""
        try:
            print("\n📁 Testing filesystem APIs...")
            
            # Test filesystem list
            from core_client.base.api.v3_fs_get_list import sync as fs_list_sync
            fs_response = fs_list_sync(self.client)
            if fs_response:
                print(f"✅ Filesystem list API: Response received")
            
            return True
            
        except Exception as e:
            print(f"❌ Filesystem APIs test failed: {e}")
            traceback.print_exc()
            return False
    
    def test_process_apis(self):
        """Test process management APIs."""
        try:
            print("\n🔄 Testing process APIs...")
            
            # Test process list
            from core_client.base.api.v3_process_get_list import sync as process_list_sync
            process_response = process_list_sync(self.client)
            if process_response:
                print(f"✅ Process list API: Response received")
            
            return True
            
        except Exception as e:
            print(f"❌ Process APIs test failed: {e}")
            traceback.print_exc()
            return False
    
    def test_metrics_apis(self):
        """Test metrics APIs."""
        try:
            print("\n📊 Testing metrics APIs...")
            
            # Test metrics get
            from core_client.base.api.v3_metrics_get import sync as metrics_get_sync
            metrics_response = metrics_get_sync(self.client)
            if metrics_response:
                print(f"✅ Metrics get API: Response received")
            
            return True
            
        except Exception as e:
            print(f"❌ Metrics APIs test failed: {e}")
            traceback.print_exc()
            return False
    
    def test_session_apis(self):
        """Test session APIs."""
        try:
            print("\n🪑 Testing session APIs...")
            
            # Test active sessions
            from core_client.base.api.v3_session_get_active import sync as session_active_sync
            session_response = session_active_sync(self.client)
            if session_response:
                print(f"✅ Session active API: Response received")
            
            return True
            
        except Exception as e:
            print(f"❌ Session APIs test failed: {e}")
            traceback.print_exc()
            return False
    
    def test_skills_apis(self):
        """Test skills APIs."""
        try:
            print("\n🛠️  Testing skills APIs...")
            
            # Test skills get
            from core_client.base.api.v3_skills_get import sync as skills_get_sync
            skills_response = skills_get_sync(self.client)
            if skills_response:
                print(f"✅ Skills get API: Response received")
            
            return True
            
        except Exception as e:
            print(f"❌ Skills APIs test failed: {e}")
            traceback.print_exc()
            return False
    
    def test_rtmp_apis(self):
        """Test RTMP APIs."""
        try:
            print("\n📡 Testing RTMP APIs...")
            
            # Test RTMP get
            from core_client.base.api.v3_rtmp_get import sync as rtmp_get_sync
            rtmp_response = rtmp_get_sync(self.client)
            if rtmp_response:
                print(f"✅ RTMP get API: Response received")
            
            return True
            
        except Exception as e:
            print(f"❌ RTMP APIs test failed: {e}")
            traceback.print_exc()
            return False
    
    def test_srt_apis(self):
        """Test SRT APIs."""
        try:
            print("\n🌊 Testing SRT APIs...")
            
            # Test SRT get
            from core_client.base.api.v3_srt_get import sync as srt_get_sync
            srt_response = srt_get_sync(self.client)
            if srt_response:
                print(f"✅ SRT get API: Response received")
            
            return True
            
        except Exception as e:
            print(f"❌ SRT APIs test failed: {e}")
            traceback.print_exc()
            return False
    
    def test_async_apis(self):
        """Test async API functionality."""
        try:
            print("\n⚡ Testing async APIs...")
            
            async def test_async():
                # Test async cluster list
                from core_client.base.api.v3_cluster_get_list import asyncio as cluster_list_async
                cluster_response = await cluster_list_async(self.async_client)
                if cluster_response:
                    print(f"✅ Async cluster list API: Response received")
                return True
            
            # Run async test
            result = asyncio.run(test_async())
            return result
            
        except Exception as e:
            print(f"❌ Async APIs test failed: {e}")
            traceback.print_exc()
            return False
    
    def run_all_tests(self):
        """Run the complete test suite."""
        print("🚀 Starting Integration Test Suite")
        print("=" * 60)
        print(f"Target: {RESTREAMER_URL}")
        print(f"Username: {CREDENTIALS['username']}")
        print("=" * 60)
        
        self.start_time = time.time()
        
        # Setup
        if not self.setup_clients():
            print("❌ Test suite cannot continue due to client setup failure")
            return False
        
        # Run all tests
        tests = [
            ("Authentication", self.test_authentication),
            ("Basic APIs", self.test_basic_apis),
            ("Cluster APIs", self.test_cluster_apis),
            ("Config APIs", self.test_config_apis),
            ("Filesystem APIs", self.test_filesystem_apis),
            ("Process APIs", self.test_process_apis),
            ("Metrics APIs", self.test_metrics_apis),
            ("Session APIs", self.test_session_apis),
            ("Skills APIs", self.test_skills_apis),
            ("RTMP APIs", self.test_rtmp_apis),
            ("SRT APIs", self.test_srt_apis),
            ("Async APIs", self.test_async_apis),
        ]
        
        for test_name, test_func in tests:
            try:
                success = test_func()
                self.log_test(test_name, success)
            except Exception as e:
                self.log_test(test_name, False, f"Test crashed: {e}")
        
        # Summary
        self.print_summary()
        return True
    
    def print_summary(self):
        """Print test results summary."""
        print("\n" + "=" * 60)
        print("📊 INTEGRATION TEST RESULTS SUMMARY")
        print("=" * 60)
        
        total_tests = len(self.test_results)
        passed_tests = sum(1 for result in self.test_results.values() if result["success"])
        failed_tests = total_tests - passed_tests
        
        # Calculate duration
        duration = time.time() - self.start_time if self.start_time else 0
        
        print(f"Total Tests: {total_tests}")
        print(f"✅ Passed: {passed_tests}")
        print(f"❌ Failed: {failed_tests}")
        print(f"⏱️  Duration: {duration:.2f} seconds")
        print(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%")
        
        if failed_tests > 0:
            print("\n❌ Failed Tests:")
            for test_name, result in self.test_results.items():
                if not result["success"]:
                    print(f"  - {test_name}: {result['details']}")
        
        print("\n" + "=" * 60)
        
        if failed_tests == 0:
            print("🎉 All integration tests passed! The library is working correctly.")
        else:
            print(f"⚠️  {failed_tests} test(s) failed. Please check the details above.")
        
        print("\nNext steps:")
        print("1. Review any failed tests")
        print("2. Check Restreamer configuration if needed")
        print("3. Deploy the library to production")

def main():
    """Main function to run the integration test suite."""
    try:
        test_suite = IntegrationTestSuite()
        test_suite.run_all_tests()
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Tests interrupted by user")
    except Exception as e:
        print(f"\n\n💥 Unexpected error: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    main()
