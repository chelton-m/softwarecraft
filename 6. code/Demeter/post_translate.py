import re
import os 
import shutil
import change_name_file

file_pot_paths = change_name_file.copy_non_fr_po_files('/Users/henrymai/Henry/trobz/demeter16/demeter16/project/')

# 1. After traslate, add space between msgstr and next line
def add_space_between_msgstr_and_comment(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    updated_lines = []
    for i, line in enumerate(lines):
        updated_lines.append(line)
        if line.startswith('msgstr') and i + 1 < len(lines) and lines[i + 1].startswith('#.'):
            updated_lines.append('\n')

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(updated_lines)

#2. Duplicate msgstr, find the position of the duplicate msgstr and the block of the duplicate msgstr from the file 
def get_pos_duplicate(fr_file):
    saved_index = []
    count_msgstr = 0

    with open(fr_file, 'r', encoding='utf-8') as file:
        for i, line in enumerate(file):
            if line == 'msgstr ""\n':
                count_msgstr += 1
            if line == '\n':
                count_msgstr = 0
            if count_msgstr == 2:
                saved_index.append(i+1)
                count_msgstr = 0
    return saved_index

def get_pos_block(fr_file):
    with open(file=fr_file, mode='r', encoding='utf-8') as file:
        lines = file.readlines()

    pos_block = []
    start_index = None

    for i, line in enumerate(lines):
        if line.startswith('#.'):
            if start_index is None:
                start_index = i+1
        if line.startswith('msgstr') and i + 1 < len(lines) and lines[i+1] == '\n':
            if start_index is not None:
                pos_block.append((start_index, i+1))
                start_index = None
    return pos_block

# ============= Test the functions =============



def filter_tuple_by_numbers(tuples_list, numbers):
    result = []
    for start, end in tuples_list:
        if any(start <= num <= end for num in numbers):
            result.append((start, end))
    return result


def revert_to_original(source_file, dest_file, filtered_tuples):
    # Read lines from the source file
    with open(source_file, 'r', encoding='utf-8') as src:
        lines = src.readlines()

    # Open the destination file to write the modified content
    with open(dest_file, 'r', encoding='utf-8') as dest:
        dest_lines = dest.readlines()

    # Prepare a new list for the destination file's lines after modification
    updated_lines = []

    # Track the lines we want to copy from the source file
    for idx, line in enumerate(dest_lines):
        copied = False

        # Check if the current line falls in any of the ranges from filtered_tuples
        for start, end in filtered_tuples:
            if start <= idx + 1 <= end:  # 1-based index
                # Copy the corresponding line from the source file
                updated_lines.append(lines[idx])
                copied = True
                break  # Exit the loop as we've handled this line

        # If the line is not in the range, just keep it as is
        if not copied:
            updated_lines.append(line)

    # Write the updated content back to the destination file
    with open(dest_file, 'w', encoding='utf-8') as dest:
        dest.writelines(updated_lines)

# ============= Test the functions =============
new_pot_file = file_pot_paths.pop(0)
new_pot_file = file_pot_paths.pop(len(file_pot_paths)-3)
new_pot_file = file_pot_paths.pop(-1)
fr_file = '/Users/henrymai/Henry/trobz/demeter16/demeter16/project/demeter_web/i18n/fr.po'
file_path = '/Users/henrymai/Henry/trobz/demeter16/demeter16/project/demeter_web/i18n/demeter_web.pot'
# for file_path in file_pot_paths:
# base_path = os.path.dirname(file_path.rstrip('/'))
# fr_file = os.path.join(base_path, 'fr.po')
add_space_between_msgstr_and_comment(fr_file)             

pos_dup = get_pos_duplicate(fr_file)
pos_block = get_pos_block(fr_file)
filtered_tuples = filter_tuple_by_numbers(pos_block, pos_dup)
revert_to_original(file_path, fr_file, filtered_tuples)