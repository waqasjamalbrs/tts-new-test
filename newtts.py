import requests
import time

# 1. URL Setup
url = "https://yousmind.com/api/tts/generate"

# 2. Headers (Aapke login session ki details)
headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ3YXFhc2phbWFsNTIyQGdtYWlsLmNvbSIsImV4cCI6MTc2NjMxNDU5MX0.ZPPOUPgeLmXX4LMTrk004k2Siwr_8dWkCvNhCAQXkgw",
    "content-type": "application/json",
    "origin": "https://yousmind.com",
    "referer": "https://yousmind.com/app/tts",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
    "Cookie": "cf_clearance=0RSwBieFJlD7m53L35bbZc6Mips6qQH57YbbThGyJe4-1765714584-1.2.1.1-ui5uJbd7Fl8euCugYCOUTlW3akRCnSsD4GOrUzLHhIf339y3SHdNEd.scIX.rHe409PraUd7M1pEaahtqAHezMW3S7HXbBgy8sqLonwheg3FK0xjrq8rGBJunWt2MXoGUvBzeR0Oew5fYhE1p3raf.90X78MEi9VBYdOFUNuqGdgfZAk_dUeN_n4xJgeGEf0G2Bast1zD4ehxTAelo9NUwtBdUybDhHMdn.cPNhrZIY"
}

# --- YAHAN CHANGE KIYA HAI (INPUT SYSTEM) ---
print("--- Text to Speech Generator ---")
user_text = input("Jo text bulwana hai yahan likhein: ")

# Agar user ne kuch nahi likha to default text
if not user_text:
    user_text = "Hello, you did not enter any text."

# 3. Data Packet banana
payload = {
    "text": user_text,   # Yahan aapka likha hua text jayega
    "voice_name": "en-US-AndrewNeural",
    "rate": 1,
    "pitch": 0,
    "volume": 0
}

print("Audio generate ho rahi hai, please wait...")

# 4. Request bhejna
try:
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        # File ka naam unique banane ke liye timestamp use kar rahe hain
        filename = f"audio_{int(time.time())}.mp3"
        
        with open(filename, "wb") as file:
            file.write(response.content)
        
        print(f"\nSuccess! ✅")
        print(f"Aapki file save ho gayi hai: {filename}")
    else:
        print(f"\nError aaya: {response.status_code}")
        print("Sayad Token expire ho gaya hai ya text bahut lamba hai.")
        print(response.text)

except Exception as e:
    print(f"Koi gadbad ho gayi: {e}")
