# Testing Guide for Pydantic v2 Compatibility

This guide will help you test that the core-client library is now compatible with Pydantic v2.

## Prerequisites

Make sure you have Pydantic v2.5.2+ installed:
```bash
pip install "pydantic>=2.5.2"
```

## Quick Test (Recommended First Step)

Run the quick test to get a basic overview:
```bash
python quick_test.py
```

This will test basic imports and model creation without running the full test suite.

## Full Compatibility Test

Run the comprehensive test suite:
```bash
python test_pydantic_v2_compatibility.py
```

This will run all tests including:
- ✅ Pydantic version check
- ✅ Module imports
- ✅ Model creation and validation
- ✅ Client initialization
- ✅ API functionality
- ✅ V1 pattern detection

## Install and Test the Package

1. **Install in development mode:**
   ```bash
   pip install -e .
   ```

2. **Test basic functionality:**
   ```python
   from core_client import Client
   
   # This should work without Pydantic v1 errors
   client = Client(base_url="http://localhost:8080")
   print("✅ Client created successfully!")
   ```

## What the Tests Check

### ✅ **Import Tests**
- All modules can be imported without errors
- No Pydantic v1 import patterns remain

### ✅ **Model Tests**
- Models can be created and validated
- RootModel-based models work correctly (replacing `__root__`)
- No validation errors occur

### ✅ **Client Tests**
- Client class can be initialized with Pydantic v2 types
- AnyUrl validation works correctly

### ✅ **API Tests**
- API functions can be imported and called
- No `parse_obj_as` or `validate_arguments` usage remains

### ✅ **Pattern Detection**
- Scans codebase for remaining Pydantic v1 patterns
- Ensures complete migration

## Expected Results

If all tests pass, you should see:
```
🎉 All tests passed! The library is compatible with Pydantic v2.

Next steps:
1. Install the updated package: pip install -e .
2. Test with your actual application
3. Deploy when ready
```

## Troubleshooting

### Common Issues

1. **Import Errors**: Check that all Pydantic v1 patterns were converted
2. **Model Validation Errors**: Ensure RootModel syntax is correct
3. **Type Errors**: Verify AnyUrl usage instead of HttpUrl

### If Tests Fail

1. Check the error messages for specific issues
2. Look for remaining `parse_obj_as` or `__root__` patterns
3. Verify Pydantic v2 is installed and being used
4. Check for syntax errors in converted files

## Next Steps After Testing

1. **Install the package**: `pip install -e .`
2. **Test with your application**: Import and use the library
3. **Verify functionality**: Ensure all features work as expected
4. **Deploy**: When satisfied, deploy the updated version

## Cleanup

After testing, you can remove the test files:
```bash
rm test_pydantic_v2_compatibility.py quick_test.py TESTING_GUIDE.md
rm migrate_pydantic_v2.py fix_pydantic_v2_issues.py fix_remaining_issues.py
```

## Support

If you encounter issues during testing:
1. Check the error messages carefully
2. Verify Pydantic v2 is installed
3. Look for any remaining v1 patterns in the code
4. Test with a minimal example to isolate issues
