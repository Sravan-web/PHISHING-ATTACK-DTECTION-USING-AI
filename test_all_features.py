"""
Comprehensive Feature Test Script
Tests all phishing detection features with clear output
"""

import requests
import json
import time
from datetime import datetime

API_BASE = "http://localhost:5000"

def print_separator(title):
    print("\n" + "="*60)
    print(f"🧪 {title}")
    print("="*60)

def print_result(test_name, response):
    print(f"\n📋 {test_name}")
    print("-" * 40)
    
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Status: {data.get('status', 'N/A')}")
        
        if 'prediction' in data:
            pred = data['prediction']
            print(f"🎯 Prediction: {pred.get('prediction', 'N/A')}")
            print(f"📊 Risk Score: {pred.get('risk_score', 'N/A')}/100")
            print(f"🏷️  Classification: {pred.get('classification', 'N/A')}")
            print(f"⚡ Method: {pred.get('method', 'N/A')}")
            
            if 'component_scores' in pred:
                scores = pred['component_scores']
                print(f"📈 Component Scores:")
                print(f"   🔗 URL Score: {scores.get('url_score', 'N/A')}")
                print(f"   📝 Text Score: {scores.get('text_score', 'N/A')}")
                print(f"   🌐 Content Score: {scores.get('content_score', 'N/A')}")
                print(f"   🚀 Boost Factors: {scores.get('boost_factors', 'N/A')}")
        
        if 'processing_time_ms' in data:
            print(f"⏱️  Processing Time: {data['processing_time_ms']}ms")
            
    else:
        print(f"❌ HTTP Error: {response.status_code}")
        print(f"Response: {response.text}")

def test_all_features():
    print("🛡️  PHISHING DETECTION SYSTEM - FEATURE TESTING")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Test 1: Health Check
    print_separator("HEALTH CHECK")
    try:
        response = requests.get(f"{API_BASE}/health")
        data = response.json()
        print(f"✅ API Status: {data.get('status', 'Unknown')}")
        print(f"🕐 Timestamp: {datetime.fromtimestamp(data.get('timestamp', 0))}")
        print("🔧 Services Status:")
        services = data.get('services', {})
        for service, status in services.items():
            status_icon = "✅" if status else "❌"
            print(f"   {status_icon} {service}: {'Online' if status else 'Offline'}")
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return
    
    # Test 2: Safe URLs
    print_separator("SAFE URL DETECTION")
    safe_urls = [
        "https://www.google.com",
        "https://github.com", 
        "https://stackoverflow.com",
        "https://www.wikipedia.org"
    ]
    
    for url in safe_urls:
        try:
            response = requests.post(
                f"{API_BASE}/quick-check",
                json={"url": url}
            )
            print_result(f"Safe URL: {url}", response)
        except Exception as e:
            print(f"❌ Error testing {url}: {e}")
    
    # Test 3: Suspicious URLs
    print_separator("SUSPICIOUS URL DETECTION")
    suspicious_urls = [
        {
            "url": "http://192.168.1.100/login",
            "reason": "IP Address instead of domain"
        },
        {
            "url": "https://payp4l-secure.tk/verify",
            "reason": "Typosquatting + suspicious TLD"
        },
        {
            "url": "https://amaz0n-update-urgent.click/account",
            "reason": "Multiple red flags"
        },
        {
            "url": "https://bit.ly/suspicious123",
            "reason": "URL shortener"
        }
    ]
    
    for item in suspicious_urls:
        try:
            response = requests.post(
                f"{API_BASE}/quick-check",
                json={"url": item["url"]}
            )
            print_result(f"Suspicious URL: {item['url']} ({item['reason']})", response)
        except Exception as e:
            print(f"❌ Error testing {item['url']}: {e}")
    
    # Test 4: Text Analysis
    print_separator("PHISHING TEXT DETECTION")
    phishing_texts = [
        {
            "text": "URGENT! Your PayPal account has been SUSPENDED! Click here immediately to verify your account or it will be permanently closed!",
            "description": "PayPal Phishing with urgency"
        },
        {
            "text": "Security Alert: Your bank account shows suspicious activity. Login now to prevent unauthorized access.",
            "description": "Banking phishing with security alert"
        },
        {
            "text": "Microsoft Account: Unusual sign-in activity detected. Confirm your identity immediately to avoid account suspension.",
            "description": "Microsoft impersonation"
        }
    ]
    
    for item in phishing_texts:
        try:
            response = requests.post(
                f"{API_BASE}/analyze",
                json={
                    "url": "https://example.com",
                    "text": item["text"],
                    "include_content": False
                }
            )
            print_result(f"Phishing Text: {item['description']}", response)
        except Exception as e:
            print(f"❌ Error testing text: {e}")
    
    # Test 5: Legitimate Text
    print_separator("LEGITIMATE TEXT DETECTION")
    legitimate_texts = [
        {
            "text": "Welcome to our newsletter! Click unsubscribe to stop receiving emails.",
            "description": "Newsletter unsubscribe"
        },
        {
            "text": "Your order has been shipped. Track your package using the link below.",
            "description": "Shipping notification"
        },
        {
            "text": "Thank you for your purchase. Your receipt is attached to this email.",
            "description": "Purchase receipt"
        }
    ]
    
    for item in legitimate_texts:
        try:
            response = requests.post(
                f"{API_BASE}/analyze",
                json={
                    "url": "https://example.com", 
                    "text": item["text"],
                    "include_content": False
                }
            )
            print_result(f"Legitimate Text: {item['description']}", response)
        except Exception as e:
            print(f"❌ Error testing text: {e}")
    
    # Test 6: Content Analysis
    print_separator("CONTENT ANALYSIS")
    try:
        response = requests.post(
            f"{API_BASE}/analyze",
            json={
                "url": "https://httpbin.org/html",
                "include_content": True
            }
        )
        print_result("Content Analysis: Safe test site", response)
    except Exception as e:
        print(f"❌ Error testing content analysis: {e}")
    
    # Test 7: Batch Analysis
    print_separator("BATCH ANALYSIS")
    try:
        response = requests.post(
            f"{API_BASE}/batch-analyze",
            json={
                "urls": [
                    "https://www.google.com",
                    "https://github.com", 
                    "http://192.168.1.1/login",
                    "https://suspicious-site.tk"
                ],
                "include_content": False
            }
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Batch Status: {data.get('status')}")
            print(f"📊 Batch Size: {data.get('batch_size')} URLs")
            print("\n📋 Individual Results:")
            
            for i, result in enumerate(data.get('results', []), 1):
                print(f"   {i}. {result.get('url', 'Unknown URL')}")
                if 'prediction' in result:
                    pred = result['prediction']
                    print(f"      🎯 {pred.get('prediction', 'N/A')} (Score: {pred.get('risk_score', 'N/A')})")
                else:
                    print(f"      ❌ {result.get('error', 'Unknown error')}")
    except Exception as e:
        print(f"❌ Error testing batch analysis: {e}")
    
    # Summary
    print_separator("TESTING COMPLETE")
    print("🎉 All feature tests completed!")
    print("💡 Tips:")
    print("   • Scores 0-29: Safe (Green)")
    print("   • Scores 30-49: Low Risk (Yellow)")  
    print("   • Scores 50-69: Medium Risk (Orange)")
    print("   • Scores 70-100: High Risk (Red)")
    print("\n🔧 Next Steps:")
    print("   • Install browser extension for real-time protection")
    print("   • Customize detection rules in analyzer files")
    print("   • Add more training data for better accuracy")

if __name__ == "__main__":
    test_all_features()