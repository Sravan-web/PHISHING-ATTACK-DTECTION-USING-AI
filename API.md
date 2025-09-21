# Phishing Detection API Documentation

The Phishing Detection API provides REST endpoints for analyzing URLs, text content, and web pages for phishing indicators.

## Base URL

```
http://localhost:5000
```

## Authentication

No authentication required for the MVP version.

## Endpoints

### GET / - API Information

Returns basic API information and available endpoints.

**Response:**
```json
{
  "service": "Phishing Detection API",
  "version": "1.0.0",
  "description": "Real-time phishing detection using ML and advanced analysis",
  "endpoints": {
    "/analyze": "POST - Analyze a URL for phishing indicators",
    "/quick-check": "POST - Quick URL-only analysis",
    "/health": "GET - Health check",
    "/": "GET - This information"
  }
}
```

### GET /health - Health Check

Returns the health status of the API and its services.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": 1699123456.789,
  "services": {
    "url_analyzer": true,
    "text_analyzer": true,
    "content_analyzer": true,
    "classifier": true
  }
}
```

### POST /analyze - Full Analysis

Performs comprehensive phishing analysis including URL, text, and content analysis.

**Request Body:**
```json
{
  "url": "https://example.com",
  "include_content": true,
  "text": "Optional text content to analyze"
}
```

**Parameters:**
- `url` (required): The URL to analyze
- `include_content` (optional): Whether to fetch and analyze webpage content (default: true)
- `text` (optional): Additional text content to analyze

**Response:**
```json
{
  "status": "success",
  "url": "https://example.com",
  "timestamp": 1699123456.789,
  "processing_time_ms": 1250.5,
  "prediction": {
    "prediction": "phishing",
    "risk_score": 75.8,
    "confidence": 85.2,
    "classification": "high",
    "method": "rule_based",
    "component_scores": {
      "url_score": 65,
      "text_score": 80,
      "content_score": 70,
      "boost_factors": 15
    }
  },
  "analysis": {
    "url_analysis": {
      "valid": true,
      "risk_score": 65,
      "features": {
        "url_length": 45,
        "domain_risk": 25,
        "suspicious_patterns": 30,
        "structure_risk": 20,
        "ssl_risk": 15
      },
      "classification": "medium"
    },
    "text_analysis": {
      "valid": true,
      "risk_score": 80,
      "features": {
        "keyword_analysis": {
          "categories": {
            "urgency": 2,
            "security": 3,
            "impersonation": 1
          },
          "total_score": 45
        },
        "sentiment": {
          "polarity": -0.3,
          "subjectivity": 0.8
        }
      },
      "classification": "high"
    },
    "content_analysis": {
      "valid": true,
      "risk_score": 70,
      "features": {
        "page_structure": {
          "suspicious_title_keywords": 2,
          "missing_favicon": true
        },
        "brand_impersonation": {
          "detected_brands": ["paypal"],
          "brand_count": 1
        },
        "form_analysis": {
          "suspicious_input_count": 3
        }
      },
      "classification": "high"
    }
  }
}
```

### POST /quick-check - Quick URL Analysis

Performs fast URL-only analysis without content fetching.

**Request Body:**
```json
{
  "url": "https://example.com"
}
```

**Response:**
```json
{
  "status": "success",
  "url": "https://example.com",
  "timestamp": 1699123456.789,
  "processing_time_ms": 45.2,
  "prediction": {
    "prediction": "legitimate",
    "risk_score": 25.3,
    "confidence": 65.8,
    "classification": "low",
    "method": "rule_based"
  },
  "analysis": {
    "url_analysis": {
      "valid": true,
      "risk_score": 25,
      "classification": "low"
    },
    "text_analysis": null,
    "content_analysis": null
  }
}
```

### POST /batch-analyze - Batch Analysis

Analyzes multiple URLs in a single request.

**Request Body:**
```json
{
  "urls": [
    "https://example1.com",
    "https://example2.com"
  ],
  "include_content": false
}
```

**Parameters:**
- `urls` (required): Array of URLs to analyze (max 10)
- `include_content` (optional): Whether to analyze content (default: false for performance)

**Response:**
```json
{
  "status": "success",
  "batch_size": 2,
  "results": [
    {
      "status": "success",
      "url": "https://example1.com",
      "prediction": {
        "prediction": "legitimate",
        "risk_score": 15.2
      }
    },
    {
      "status": "success", 
      "url": "https://example2.com",
      "prediction": {
        "prediction": "phishing",
        "risk_score": 85.7
      }
    }
  ]
}
```

## Risk Scoring

The API uses a 0-100 risk scoring system:

- **0-29**: Safe (Green)
- **30-49**: Low Risk (Yellow)
- **50-69**: Medium Risk (Orange) 
- **70-100**: High Risk (Red)

## Classifications

- `safe`: Very low risk, likely legitimate
- `low`: Some minor suspicious indicators
- `medium`: Moderate risk, requires caution
- `high`: High risk, likely phishing
- `unknown`: Analysis failed or inconclusive

## Error Responses

### 400 Bad Request
```json
{
  "status": "error",
  "error": "Missing required field: url"
}
```

### 500 Internal Server Error
```json
{
  "status": "error",
  "error": "Internal server error"
}
```

### Analysis Failure
```json
{
  "status": "error",
  "url": "https://example.com",
  "error": "Connection timeout",
  "prediction": {
    "prediction": "unknown",
    "risk_score": 50,
    "classification": "unknown"
  }
}
```

## Rate Limiting

Currently no rate limiting is implemented in the MVP. In production, consider:
- 100 requests per minute per IP
- 10 requests per minute for batch analysis
- Caching for repeated URLs

## Example Usage

### Python
```python
import requests

# Quick check
response = requests.post('http://localhost:5000/quick-check', 
                        json={'url': 'https://suspicious-site.com'})
result = response.json()
print(f"Risk Score: {result['prediction']['risk_score']}")

# Full analysis with text
response = requests.post('http://localhost:5000/analyze', 
                        json={
                            'url': 'https://example.com',
                            'text': 'URGENT! Verify your account now!',
                            'include_content': True
                        })
```

### cURL
```bash
# Quick check
curl -X POST http://localhost:5000/quick-check \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'

# Batch analysis
curl -X POST http://localhost:5000/batch-analyze \
  -H "Content-Type: application/json" \
  -d '{"urls": ["https://site1.com", "https://site2.com"]}'
```

### JavaScript
```javascript
// Quick check
fetch('http://localhost:5000/quick-check', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({url: 'https://example.com'})
})
.then(response => response.json())
.then(data => console.log(data.prediction.risk_score));
```

## Performance Tips

1. Use `/quick-check` for fast URL-only analysis
2. Set `include_content: false` for faster responses
3. Use batch analysis for multiple URLs
4. Cache results on your side for repeated requests
5. Consider async requests for better performance

## Troubleshooting

### Common Issues

1. **Connection Refused**: Make sure API server is running
2. **Timeout Errors**: Some websites may be slow to respond
3. **SSL Errors**: These are normal for suspicious sites
4. **Memory Usage**: Content analysis uses more memory

### Debug Information

The API provides detailed error messages and processing times to help with debugging. Check the `processing_time_ms` field to identify slow operations.