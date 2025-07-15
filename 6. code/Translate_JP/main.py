# Simple dictionary for Romaji to Hiragana conversion
romaji_to_hiragana_dict = {
    'a': 'あ', 'i': 'い', 'u': 'う', 'e': 'え', 'o': 'お',
    'ka': 'か', 'ki': 'き', 'ku': 'く', 'ke': 'け', 'ko': 'こ',
    'sa': 'さ', 'shi': 'し', 'su': 'す', 'se': 'せ', 'so': 'そ',
    'ta': 'た', 'chi': 'ち', 'tsu': 'つ', 'te': 'て', 'to': 'と',
    'na': 'な', 'ni': 'に', 'nu': 'ぬ', 'ne': 'ね', 'no': 'の',
    'ha': 'は', 'hi': 'ひ', 'fu': 'ふ', 'he': 'へ', 'ho': 'ほ',
    'ma': 'ま', 'mi': 'み', 'mu': 'む', 'me': 'め', 'mo': 'も',
    'ya': 'や', 'yu': 'ゆ', 'yo': 'よ',
    'ra': 'ら', 'ri': 'り', 'ru': 'る', 're': 'れ', 'ro': 'ろ',
    'wa': 'わ', 'wo': 'を', 'n': 'ん'
}

def romaji_to_hiragana(romaji_text):
    hiragana_text = ''
    i = 0
    while i < len(romaji_text):
        if i+1 < len(romaji_text) and romaji_text[i:i+2] in romaji_to_hiragana_dict:
            hiragana_text += romaji_to_hiragana_dict[romaji_text[i:i+2]]
            i += 2
        elif romaji_text[i] in romaji_to_hiragana_dict:
            hiragana_text += romaji_to_hiragana_dict[romaji_text[i]]
            i += 1
        else:
            hiragana_text += '*'
            i += 1

    print(f"Original Romaji text: {romaji_text}")
    print(f"Converted Japanese Hiragana text: {hiragana_text}")
    return hiragana_text

# Main functionality
if __name__ == "__main__":
    romaji_text = input("Enter Romaji text: ")  # e.g., "arigato"
    hiragana_text = romaji_to_hiragana(romaji_text)
    print(f"Converted Japanese Hiragana text: {hiragana_text}")
