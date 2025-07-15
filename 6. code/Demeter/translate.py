from googletrans import Translator

translator = Translator()

print("=====================================")
with open('/Users/henrymai/Henry/trobz/demeter11/demeter/project/coffreo_connector/i18n/fr.po', 'r') as f:
    fr_lines = f.readlines()
    searched_dct = dict()
    for i in range(len(fr_lines)):
        if fr_lines[i].startswith('msgid'):
            searched_dct[fr_lines[i]] = fr_lines[i+1]
path = '/Users/henrymai/Henry/trobz/demeter16/demeter16/project/demeter_web/i18n/fr.po'
with open(path, 'r') as f:
    fr_lines = f.readlines()
    for i in range(len(fr_lines)-1):
        if fr_lines[i].startswith('msgid'):
            msgid = fr_lines[i]
            if fr_lines[i] in searched_dct:
                fr_lines[i+1] = searched_dct[fr_lines[i]]
            else:
                try:
                    translated = translator.translate(fr_lines[i][6:], src='en', dest='fr').text
                    fr_lines[i+1] = f'msgstr {translated}'
                except Exception as e:
                    print(f"Translation error for {msgid}: {e}")
                    fr_lines[i+1] = 'msgstr ""\n'
        
# Write the updated content back to a new file
with open(path, 'w') as f:
    f.writelines(fr_lines)

print("Updated content written to fr_updated.po")
