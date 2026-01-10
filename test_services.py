#!/usr/bin/env python3
"""
Quick test script to verify both services are connected correctly.
Replace the URLs with your actual Railway domains.
"""

import requests
import json

# ⚠️ REPLACE THESE WITH YOUR ACTUAL RAILWAY DOMAINS
ML_SERVICE_URL = "https://your-ml-service.up.railway.app"
EXPLANATION_SERVICE_URL = "https://your-explanation-service.up.railway.app"

def test_ml_service_health():
    """Test ML service health endpoint"""
    print("Testing ML Service Health...")
    try:
        response = requests.get(f"{ML_SERVICE_URL}/health", timeout=5)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response.status_code == 200 and response.json().get("model_loaded") == True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_explanation_service_health():
    """Test explanation service health endpoint"""
    print("\nTesting Explanation Service Health...")
    try:
        response = requests.get(f"{EXPLANATION_SERVICE_URL}/health", timeout=5)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_prediction_with_explanation():
    """Test end-to-end prediction with explanation"""
    print("\nTesting Prediction with Explanation...")
    test_data = {
        "transactionAmount": 150.50,
        "transactionAmountDeviation": 0.25,
        "timeAnomaly": 0.3,
        "locationDistance": 25.0,
        "merchantNovelty": 0.2,
        "transactionFrequency": 5
    }
    
    try:
        response = requests.post(
            f"{ML_SERVICE_URL}/predict",
            json=test_data,
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        print(f"Status Code: {response.status_code}")
        result = response.json()
        print(f"Response: {json.dumps(result, indent=2)}")
        
        if result.get("explanation"):
            print("\n✅ SUCCESS! Explanation is present - Services are connected!")
            return True
        else:
            print("\n❌ WARNING: Explanation is missing or null")
            print("Check that EXPLANATION_SERVICE_URL environment variable is set in ML service")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("Testing Fraudguard-AI Services")
    print("=" * 60)
    
    ml_ok = test_ml_service_health()
    exp_ok = test_explanation_service_health()
    
    if ml_ok and exp_ok:
        test_prediction_with_explanation()
    else:
        print("\n❌ One or more services are not healthy. Fix health checks first.")
    
    print("\n" + "=" * 60)
