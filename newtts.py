import requests
import json

# URL jahan request jayegi
url = "https://yousmind.com/api/tts/generate"

# Headers (Browser ki settings aur Login Token)
headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    # Note: Ye aapka secret token hai, isse kisi ke sath share na karein
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ3YXFhc2phbWFsNTIyQGdtYWlsLmNvbSIsImV4cCI6MTc2NjMxNDU5MX0.ZPPOUPgeLmXX4LMTrk004k2Siwr_8dWkCvNhCAQXkgw",
    "content-type": "application/json",
    "origin": "https://yousmind.com",
    "referer": "https://yousmind.com/app/tts",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
    # Cloudflare clearance cookie
    "Cookie": "cf_clearance=0RSwBieFJlD7m53L35bbZc6Mips6qQH57YbbThGyJe4-1765714584-1.2.1.1-ui5uJbd7Fl8euCugYCOUTlW3akRCnSsD4GOrUzLHhIf339y3SHdNEd.scIX.rHe409PraUd7M1pEaahtqAHezMW3S7HXbBgy8sqLonwheg3FK0xjrq8rGBJunWt2MXoGUvBzeR0Oew5fYhE1p3raf.90X78MEi9VBYdOFUNuqGdgfZAk_dUeN_n4xJgeGEf0G2Bast1zD4ehxTAelo9NUwtBdUybDhHMdn.cPNhrZIY"
}

# Data (Jo text aap bulwana chahte hain)
payload = {
    "text": "If your self-worth depends on society's praise, they can destroy you by cancelling you.\n\n",
    "voice_name": "en-US-AndrewNeural",
    "rate": 1,
    "pitch": 0,
    "volume": 0
}

print("Request bhej raha hu...")

# Request bhejna
response = requests.post(url, json=payload, headers=headers)

# Response check karna
if response.status_code == 200:
    print("Success! Audio generate ho gayi hai.")
    
    # Audio ko file me save karna
    # Note: Extension check kar lena, mostly .mp3 ya .wav hoti hai
    with open("output_audio.mp3", "wb") as file:
        file.write(response.content)
    print("File 'output_audio.mp3' naam se save ho gayi hai.")
else:
    print(f"Error aaya: {response.status_code}")
    print(response.text)
