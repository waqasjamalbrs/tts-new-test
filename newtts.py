import requests

url = "https://yousmind.com/api/tts/generate"

headers = {
    "accept": "*/*",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ3YXFhc2phbWFsNTIyQGdtYWlsLmNvbSIsImV4cCI6MTc2NjMxNDU5MX0.ZPPOUPgeLmXX4LMTrk004k2Siwr_8dWkCvNhCAQXkgw",
    "content-type": "application/json",
    "origin": "https://yousmind.com",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
}

payload = {
    "text": "Hello testing",
    "voice_name": "en-US-AndrewNeural",
    "rate": 1,
    "pitch": 0,
    "volume": 0
}

response = requests.post(url, json=payload, headers=headers)

print("--- SERVER RESPONSE CHECK ---")
print(f"Status Code: {response.status_code}")
print("Response ke shuru ke 200 characters:")
print(response.text[:200])  # Ye line batayegi ki andar kya hai
