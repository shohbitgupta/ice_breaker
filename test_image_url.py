#!/usr/bin/env python3
"""
Test script to verify that the LinkedIn scraping returns the correct image URL
"""

from dotenv import load_dotenv
from third_parties.linkedin import scrape_linkedin_profile
import json

def test_linkedin_scraping():
    """Test the LinkedIn scraping function directly"""
    load_dotenv()

    print("Testing LinkedIn scraping function...")
    print("=" * 50)

    try:
        # Test with mock data (which should return Eden Marco's profile)
        linkedin_data = scrape_linkedin_profile("dummy_url", mock=True)

        print("LinkedIn data keys:")
        for key in linkedin_data.keys():
            print(f"  - {key}")
        print("-" * 30)

        print(f"Full Name: {linkedin_data.get('firstName', '')} {linkedin_data.get('lastName', '')}")
        print(f"Headline: {linkedin_data.get('headline', 'N/A')}")
        print(f"Photo URL: {linkedin_data.get('photoUrl', 'N/A')}")
        print(f"Photo URL type: {type(linkedin_data.get('photoUrl'))}")
        print(f"Photo URL length: {len(linkedin_data.get('photoUrl', '')) if linkedin_data.get('photoUrl') else 0}")
        print("-" * 30)

        # Test the response format that would be sent to frontend
        response_data = {
            "photo_url": linkedin_data.get("photoUrl"),
            "name": f"{linkedin_data.get('firstName', '')} {linkedin_data.get('lastName', '')}",
            "headline": linkedin_data.get('headline', '')
        }

        print("Sample response data:")
        print(json.dumps(response_data, indent=2))

        # Verify the image URL is valid
        photo_url = linkedin_data.get("photoUrl")
        if photo_url:
            print(f"\n✅ Photo URL found: {photo_url}")
            print(f"   URL starts with https: {photo_url.startswith('https')}")
            print(f"   URL contains linkedin: {'linkedin' in photo_url}")
            return True
        else:
            print("\n❌ No photo URL found in the data")
            return False

    except Exception as e:
        print(f"Error occurred: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_linkedin_scraping()
    if success:
        print("\n✅ Test completed successfully!")
    else:
        print("\n❌ Test failed!")
