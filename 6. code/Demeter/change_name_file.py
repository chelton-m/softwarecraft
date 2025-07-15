import os 
import shutil
from googletrans import Translator

def copy_non_fr_po_files(source_dir):
    file_paths = []
    for root, dirs, files in os.walk(source_dir):
        dirs.sort()
        files.sort()
        if 'i18n' in dirs:
            i18n_path = os.path.join(root, 'i18n')
            module_name = os.path.basename(root.rstrip('/'))
            for file_name in os.listdir(i18n_path):
                name_part = file_name.split('.')[0]
                if name_part == module_name:
                    file_path = os.path.join(i18n_path, file_name)
                    file_paths.append(file_path)
    return file_paths
source_dir = '/Users/henrymai/Henry/trobz/demeter16/demeter16/project/'
file_paths = copy_non_fr_po_files(source_dir)
print(file_paths)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

def translate_po_file(file_path):
    translator = Translator()
    print("=====================================")
    with open('/Users/henrymai/Henry/trobz/demeter11/demeter/project/coffreo_connector/i18n/fr.po', 'r') as f:
        fr_lines = f.readlines()
        searched_dct = dict()
        for i in range(len(fr_lines)):
            if fr_lines[i].startswith('msgid'):
                searched_dct[fr_lines[i]] = fr_lines[i+1]

    for file_path in file_paths:
        with open(file_path, 'r') as f:
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
        base_path = os.path.dirname(file_path.rstrip('/'))
        new_path = os.path.join(base_path, 'fr.po')
        with open(new_path, 'w') as f:
            f.writelines(fr_lines)

        print("Updated content written to fr_updated.po")

# translate_po_file(file_paths)
