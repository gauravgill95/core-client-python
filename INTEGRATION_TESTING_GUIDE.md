# Integration Testing Guide

This guide explains how to run integration tests against your actual Restreamer instance to validate that the Pydantic v2 migration is working correctly.

## 🎯 **What We're Testing**

The integration tests validate:
- ✅ **Client Creation** - Both sync and async clients work
- ✅ **Authentication** - Login with your credentials works
- ✅ **All API Endpoints** - Every API function can be called successfully
- ✅ **Response Parsing** - Pydantic models correctly parse API responses
- ✅ **Error Handling** - Proper error handling for failed requests

## 🚀 **Quick Start**

### **Option 1: Quick Connectivity Test (Recommended First)**

Run a basic connectivity test to verify your setup:

```bash
python quick_integration_test.py
```

Choose option 1 for the quick test. This will:
1. Test client creation
2. Test authentication
3. Test basic API calls (About, Ping)
4. Give you immediate feedback on connectivity

### **Option 2: Test Specific APIs**

If you want to test specific endpoints:

```bash
python quick_integration_test.py
```

Choose option 2, then select which API to test:
- Cluster list
- Configuration
- Filesystem
- Processes
- Metrics

### **Option 3: Full Integration Test Suite**

Run the comprehensive test suite:

```bash
python integration_test.py
```

This tests **all** available APIs and provides detailed results.

## 🔧 **Prerequisites**

1. **Virtual Environment Activated**: Make sure you're in the virtual environment
2. **Package Installed**: Install the package in development mode:
   ```bash
   pip install -e .
   ```
3. *

## 📋 **Test Configuration**

The tests are configured with your credentials:

```python
RESTREAMER_URL = ""
CREDENTIALS = {
    "username": "",
    "password": ""
}
```

## 🧪 **What Each Test Validates**

### **Authentication Test**
- Client creation with Pydantic v2 `AnyUrl` type
- Login process with username/password
- Token retrieval and validation

### **Basic APIs Test**
- **About API**: Server information and capabilities
- **Ping API**: Basic connectivity check

### **Cluster APIs Test**
- Cluster node management
- Node list retrieval

### **Configuration APIs Test**
- Server configuration retrieval
- Configuration validation

### **Filesystem APIs Test**
- File system operations
- Directory listing

### **Process APIs Test**
- Process management
- Process status monitoring

### **Metrics APIs Test**
- Performance metrics
- System statistics

### **Session APIs Test**
- Active session management
- Session monitoring

### **Skills APIs Test**
- Server capabilities
- Feature detection

### **RTMP APIs Test**
- RTMP stream management
- RTMP configuration

### **SRT APIs Test**
- SRT stream management
- SRT configuration

### **Async APIs Test**
- Asynchronous client functionality
- Async API calls

## 📊 **Understanding Test Results**

### **Success Indicators**
- ✅ **PASS**: Test completed successfully
- Response received and parsed correctly
- No Pydantic validation errors

### **Failure Indicators**
- ❌ **FAIL**: Test failed
- Check the error details below each failure
- Common issues: network, authentication, or API endpoint problems

### **Test Summary**
After all tests complete, you'll see:
- Total tests run
- Number of passed/failed tests
- Success rate percentage
- Duration of test suite
- Detailed failure information

## 🚨 **Troubleshooting Common Issues**

### **Authentication Failures**
- Verify credentials are correct
- Check if Restreamer requires different authentication method
- Ensure the server is accessible

### **Network Errors**
- Check firewall settings
- Verify SSL certificate is valid

### **API Endpoint Errors**
- Some endpoints might not be available in your Restreamer version
- Check Restreamer documentation for available endpoints
- Some endpoints might require specific permissions

### **Pydantic Validation Errors**
- These indicate the migration wasn't complete
- Check the specific error message
- Verify the model definitions are correct

## 🔄 **Running Tests Multiple Times**

You can run the tests multiple times to:
- Verify consistency of results
- Test different scenarios
- Monitor for intermittent issues

## 📈 **Performance Monitoring**

The test suite measures:
- **Duration**: Total time to complete all tests
- **Response Times**: Individual API response times
- **Success Rate**: Percentage of tests that pass

## 🚀 **Next Steps After Testing**

1. **All Tests Pass**: 🎉 Your library is ready for production!
2. **Some Tests Fail**: Review failures and fix any remaining issues
3. **Many Tests Fail**: Check network connectivity and Restreamer configuration

## 📞 **Getting Help**

If you encounter issues:
1. Check the error messages carefully
2. Verify your Restreamer instance is running
3. Check network connectivity
4. Review the troubleshooting section above

## 🎯 **Expected Results**

With a properly configured Restreamer instance, you should see:
- **100% success rate** on all tests
- **Fast response times** (typically under 5 seconds total)
- **Proper authentication** with valid tokens
- **All API endpoints** responding correctly

---

**Happy Testing! 🚀**

Your Pydantic v2 migration is complete, and these tests will validate that everything works correctly in production.
