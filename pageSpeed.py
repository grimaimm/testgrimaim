import requests

url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"

params = {
    "url": "https://127.0.0.1:5000/dashboard",
    "strategy": "desktop",
    "key": "AIzaSyARfx_A-gCPFd4JwMRb7SCANYote5jgIvE",
    "category": ["performance", "accessibility", "best-practices", "seo"]
}

# Make the GET request
res = requests.get(url, params=params)

    # Parse the JSON response
data = res.json()

# Access the performance score
performance_score = data.get("lighthouseResult", {}).get("categories", {}).get("performance", {}).get("score", 0) * 100
print(f"Performance Score: {performance_score}")

accessibility_score = data.get("lighthouseResult", {}).get("categories", {}).get("accessibility", {}).get("score", 0) * 100
print(f"Accessibility Score: {accessibility_score}")

bestpractices_score = data.get("lighthouseResult", {}).get("categories", {}).get("best-practices", {}).get("score", 0) * 100
print(f"Best Practices Score: {bestpractices_score}")

seo_score = data.get("lighthouseResult", {}).get("categories", {}).get("seo", {}).get("score", 0) * 100
print(f"Seo Score: {seo_score}")


