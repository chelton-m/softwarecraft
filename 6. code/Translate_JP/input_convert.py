import convert
import requests
import json

# Function to translate Japanese text to English using LibreTranslate API
def translate_japanese_to_english(japanese_text):
    url = "http://localhost:8000/translate"
    payload = {
        "q": japanese_text,
        "source": "ja",  # Source language (Japanese)
        "target": "en",  # Target language (English)
        "format": "text",
        "alternatives": 3,
        "api_key": ""
    }
    headers = { "Content-Type": "application/json" }
    response = requests.post(url, data=json.dumps(payload), headers=headers)    
    # Check if the request was successful
    if response.status_code == 200:
        translated_text = response.json().get('translatedText')
        return translated_text
    else:
        return f"Error: {response.status_code}"

# Function to translate Japanese Hiragana to English using LibreTranslate API def translate_to_english(japanese_text): """Translates Japanese text to English.""" url = "https://libretranslate.de/translate" payload = { "q": japanese_text, "source": "ja", "target": "en", "format": "text" } headers = { "Content-Type": "application/json" } response = requests.post(url, json=payload, headers=headers) response_json = response.json() english_text = response_json["translatedText"] # Debugging: Check intermediate output print(f"Original Japanese text: {japanese_text}") print(f"Translated English text: {english_text}") return english_text
def main():
	while 1:
		romaji = input("Enter a Romaji string: ")
		japanese = convert.romajiToJapanese(romaji.lower())
		print("Japanese equivalent: %s" % japanese)
		translated_text = translate_japanese_to_english(japanese)
		print(f"Translated text: {translated_text}")

main()