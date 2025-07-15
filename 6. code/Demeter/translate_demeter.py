from googletrans import Translator

def read_po_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return lines

def build_searched_dict(lines):
    searched_dct = {}
    i = 0
    while i < len(lines):
        if lines[i].startswith('msgid'):
            msgid = lines[i].strip()
            msgstr = lines[i+1].strip()
            # Handle multi-line msgid and msgstr
            while not lines[i+1].startswith('msgstr'):
                i += 1
                msgid += lines[i].strip()
            while not lines[i+1].startswith('msgid') and not lines[i+1].startswith('msgstr'):
                i += 1
                msgstr += lines[i].strip()
            searched_dct[msgid] = msgstr
        i += 1
    return searched_dct

def update_translations(lines, searched_dct, translator):
    i = 0
    while i < len(lines):
        if lines[i].startswith('msgid'):
            msgid = lines[i].strip()
            msgstr_index = i + 1
            if msgid in searched_dct:
                lines[msgstr_index] = searched_dct[msgid] + '\n'
            else:
                original_msgstr = lines[msgstr_index].strip().strip('"')
                if original_msgstr:
                    try:
                        translated = translator.translate(original_msgstr, src='en', dest='fr').text
                        lines[msgstr_index] = f'msgstr "{translated}"\n'
                    except Exception as e:
                        print(f"Translation error for {msgid}: {e}")
                        lines[msgstr_index] = 'msgstr ""\n'
        i += 1
    return lines

print("=====================================")
translator = Translator()

# Read and build the dictionary from the first file
fr_lines_11 = read_po_file('/Users/henrymai/Henry/trobz/demeter11/demeter/project/coffreo_connector/i18n/fr.po')
searched_dct = build_searched_dict(fr_lines_11)

# Read the second file and update translations
fr_lines_16 = read_po_file('/Users/henrymai/Henry/trobz/demeter16/demeter16/project/demeter_association/i18n/fr.po')
updated_lines = update_translations(fr_lines_16, searched_dct, translator)

# Write the updated content back to a new file
with open('/Users/henrymai/Henry/trobz/demeter16/demeter16/project/coffreo_connector/i18n/fr_updated.po', 'w') as f:
    f.writelines(updated_lines)

print("Updated content written to fr_updated.po")