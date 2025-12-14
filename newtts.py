import requests
import time

# 1. URL Setup
url = "https://yousmind.com/api/tts/generate"

# 2. Cookies (Aapke naye code se li gayi)
cookies = {
    'cf_clearance': '0RSwBieFJlD7m53L35bbZc6Mips6qQH57YbbThGyJe4-1765714584-1.2.1.1-ui5uJbd7Fl8euCugYCOUTlW3akRCnSsD4GOrUzLHhIf339y3SHdNEd.scIX.rHe409PraUd7M1pEaahtqAHezMW3S7HXbBgy8sqLonwheg3FK0xjrq8rGBJunWt2MXoGUvBzeR0Oew5fYhE1p3raf.90X78MEi9VBYdOFUNuqGdgfZAk_dUeN_n4xJgeGEf0G2Bast1zD4ehxTAelo9NUwtBdUybDhHMdn.cPNhrZIY',
}

# 3. Headers (Aapke naye code se)
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ3YXFhc2phbWFsNTIyQGdtYWlsLmNvbSIsImV4cCI6MTc2NjMxNDU5MX0.ZPPOUPgeLmXX4LMTrk004k2Siwr_8dWkCvNhCAQXkgw',
    'content-type': 'application/json',
    'origin': 'https://yousmind.com',
    'referer': 'https://yousmind.com/app/tts',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
}

# 4. Input Lena
print("--- Text to Speech ---")
text = input("Kya bulwana hai? : ")
if not text: text = "Testing audio generation."

# 5. Data Packet
json_data = {
    'text': text,
    'voice_name': 'en-US-AndrewNeural',
    'rate': 1,
    'pitch': 0,
    'volume': 0,
}

print("Connecting to server...")

# 6. Request Bhejna (Sirf ek baar)
response = requests.post(url, cookies=cookies, headers=headers, json=json_data)

# 7. Result Check Karna
print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    # Check karein data aaya ya nahi
    file_size = len(response.content)
    print(f"File Size Received: {file_size} bytes")

    if file_size > 1000: # Agar file 1KB se badi hai to audio hogi
        filename = f"audio_{int(time.time())}.mp3"
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"✅ Success! Audio file save ho gayi: {filename}")
    else:
        print("⚠️ File bahut choti hai, shayad error message hai:")
        print(response.text)
else:
    print("❌ Error aaya! Token expire ya headers galat hain.")
    print(response.text)
