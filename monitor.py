"""
Performance Monitor for Phishing Detection API
Run this to monitor API performance in VS Code
"""

import time
import requests
import json
from datetime import datetime

API_BASE = "http://localhost:5000"

def test_performance():
    """Test API performance with various endpoints"""
    
    print("🔍 Phishing Detection API - Performance Monitor")
    print("=" * 60)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    # Test cases
    test_cases = [
        {
            "name": "Health Check",
            "method": "GET",
            "url": f"{API_BASE}/health",
            "data": None
        },
        {
            "name": "Quick Check - Safe URL",
            "method": "POST", 
            "url": f"{API_BASE}/quick-check",
            "data": {"url": "https://www.google.com"}
        },
        {
            "name": "Quick Check - Suspicious URL",
            "method": "POST",
            "url": f"{API_BASE}/quick-check", 
            "data": {"url": "http://192.168.1.100/login"}
        },
        {
            "name": "Full Analysis with Text",
            "method": "POST",
            "url": f"{API_BASE}/analyze",
            "data": {
                "url": "https://example.com",
                "text": "URGENT! Verify your account now!",
                "include_content": False
            }
        }
    ]
    
    results = []
    
    for test in test_cases:
        print(f"\n🧪 Testing: {test['name']}")
        
        try:
            start_time = time.time()
            
            if test['method'] == 'GET':
                response = requests.get(test['url'], timeout=10)
            else:
                response = requests.post(test['url'], json=test['data'], timeout=10)
            
            end_time = time.time()
            response_time = (end_time - start_time) * 1000  # Convert to ms
            
            if response.status_code == 200:
                data = response.json()
                
                # Extract relevant info
                status = data.get('status', 'unknown')
                processing_time = data.get('processing_time_ms', 'N/A')
                
                if 'prediction' in data:
                    risk_score = data['prediction'].get('risk_score', 'N/A')
                    classification = data['prediction'].get('classification', 'N/A')
                    print(f"   ✅ Status: {status}")
                    print(f"   📊 Risk Score: {risk_score}")
                    print(f"   🏷️  Classification: {classification}")
                else:
                    print(f"   ✅ Status: {status}")
                
                print(f"   ⏱️  Response Time: {response_time:.2f}ms")
                print(f"   🔧 Processing Time: {processing_time}ms")
                
                results.append({
                    'test': test['name'],
                    'status': 'SUCCESS',
                    'response_time': response_time,
                    'processing_time': processing_time
                })
                
            else:
                print(f"   ❌ HTTP Error: {response.status_code}")
                results.append({
                    'test': test['name'],
                    'status': f'HTTP_ERROR_{response.status_code}',
                    'response_time': response_time
                })
                
        except requests.exceptions.ConnectionError:
            print(f"   ❌ Connection Error: API server not running?")
            results.append({
                'test': test['name'],
                'status': 'CONNECTION_ERROR'
            })
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
            results.append({
                'test': test['name'],
                'status': 'ERROR',
                'error': str(e)
            })
    
    # Summary
    print("\n" + "=" * 60)
    print("📋 PERFORMANCE SUMMARY")
    print("=" * 60)
    
    successful_tests = [r for r in results if r['status'] == 'SUCCESS']
    
    if successful_tests:
        avg_response_time = sum(r['response_time'] for r in successful_tests) / len(successful_tests)
        print(f"✅ Successful Tests: {len(successful_tests)}/{len(results)}")
        print(f"⏱️  Average Response Time: {avg_response_time:.2f}ms")
        
        fastest = min(successful_tests, key=lambda x: x['response_time'])
        slowest = max(successful_tests, key=lambda x: x['response_time'])
        
        print(f"🏃 Fastest: {fastest['test']} ({fastest['response_time']:.2f}ms)")
        print(f"🐌 Slowest: {slowest['test']} ({slowest['response_time']:.2f}ms)")
    else:
        print("❌ No successful tests - check if API server is running")
    
    print("\n💡 Tip: Start the API server with 'python src/api/app.py'")

if __name__ == "__main__":
    test_performance()