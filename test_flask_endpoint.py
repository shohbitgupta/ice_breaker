#!/usr/bin/env python3
"""
Test script to verify the Flask endpoint returns the correct image URL
"""

import requests
import json

def test_flask_endpoint():
    """Test the Flask /ice_breaker endpoint"""
    
    print("Testing Flask /ice_breaker endpoint...")
    print("=" * 50)
    
    # Test data
    test_data = {
        "name": "Eden Marco",
        "technology": "Python, AI, Machine Learning",
        "company": "Google"
    }
    
    try:
        # Make request to the Flask endpoint
        response = requests.post(
            "http://127.0.0.1:8080/ice_breaker",
            json=test_data,
            headers={"Content-Type": "application/json"},
            timeout=60  # Give it time to process
        )
        
        print(f"Request data: {json.dumps(test_data, indent=2)}")
        print(f"Response status code: {response.status_code}")
        print("-" * 30)
        
        if response.status_code == 200:
            data = response.json()
            print("Response data:")
            print(json.dumps(data, indent=2))
            print("-" * 30)
            
            # Check if photo_url is present
            photo_url = data.get("photo_url")
            if photo_url:
                print(f"✅ Photo URL found: {photo_url}")
                print(f"   URL length: {len(photo_url)}")
                print(f"   URL starts with https: {photo_url.startswith('https')}")
                
                # Check if summary is present
                summary = data.get("summary")
                if summary:
                    print(f"✅ Summary found: {summary.get('summary', 'N/A')[:100]}...")
                    print(f"✅ Facts found: {len(summary.get('facts', []))} facts")
                    return True
                else:
                    print("❌ No summary found in response")
                    return False
            else:
                print("❌ No photo_url found in response")
                return False
        else:
            print(f"❌ Request failed with status {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Request error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_flask_endpoint()
    if success:
        print("\n✅ Flask endpoint test completed successfully!")
    else:
        print("\n❌ Flask endpoint test failed!")
