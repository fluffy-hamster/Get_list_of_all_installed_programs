import subprocess
import time
import os
import sys
import shutil
import re

"""
This script attempts to make a table of names, versions of all 32 and 64 bit installed programs and then merge them into a "software release note" .docx file.
"""

### HELPER FUNCTIONS ...
def combine_32_64_to_string(file1, file2):
        
        with open(file1, 'r') as f:
                string_1 = f.read()
                
        with open(file2, 'r') as f:
                string_2 = f.read()

        if string_1 == string_2: 
            error_msg = """
                        \n
                        DisplayName    : 000) WARNING! 32 and 64 bit files were identical.  
                        DisplayVersion : Manual Check of this table is required!
                        \n
                        """
        else:
            error_msg = ""

        return error_msg + string_1 + "\n" + string_2

def create_markdown_table(file, key_val_pairs):

	with open(file, 'w') as f:
		# markdown table header.
		f.write("| Name | Version |\n|---------------|----------|\n")        
		
		for key in sorted(key_val_pairs.keys()):
			f.write("| {} | {} |\n".format(key, key_val_pairs[key]))

def build_name_vals_dictionary(string):
    """
    >>> s = "
            DisplayName    : \nabc\n
            DisplayVersion : 1.0\n
            \n
            \n
            \n
            DisplayName      : xyz \n
            DisplayVersion   :\n
            "
    >>> build_name_vals_dictionary(s)
    {'abc': '1.0', 'xyz': 'N/A'}
    """
        
    names_with_versions_dict = {}
        
    s = re.split("DisplayName +:", string)
    split_data = [ re.split("DisplayVersion +:", i) for i in s]

    for name_version_pair in split_data:
            if len(name_version_pair) == 2:
                    name = name_version_pair[0].replace("\n", " ").strip()
                    version = name_version_pair[1].replace("\n", " ").strip()
                    if len(name) >= 1:     
                            if name not in names_with_versions_dict or (name in names_with_versions_dict and names_with_versions_dict[name] == ""):
                                    names_with_versions_dict[name] = version if version != "" else "N/A"

    return names_with_versions_dict


def delete_multiple_files(*args):
    for file in args:
        try:
            os.remove(file)
        except Exception as e:
            print("deleting {} produced the following error: {}".format(file, e))
            pass 

def create_installed_programs_list(output_path, nbits):
    assert nbits in [32,64], "ERROR: incorrect input." 
    
    print("--Attempting to call {} powershell script...".format(nbits))
    filename = os.path.join(output_path, "installed_programs_{}.md".format(nbits))
    command_string = 'powershell -ExecutionPolicy Bypass ./get_installed_programs_{program_version}.ps1 "{file}"'.format(program_version = nbits,
                                                                                                                         file = filename.replace(" ", "` "))
    subprocess.call(command_string)
    time.sleep(3)
    return filename
    
def create_software_table_as_file(output_path):
    filename_32 = create_installed_programs_list(output_path, 32)
    filename_64 = create_installed_programs_list(output_path, 64)

    text = combine_32_64_to_string(filename_32, filename_64)
    names_and_versions_dict = build_name_vals_dictionary(text)

    filename_table = "Software_Version_Table.md"
    fullpath = os.path.join(output_path, filename_table)
    create_markdown_table(fullpath, names_and_versions_dict)

    delete_multiple_files(filename_32, filename_64)

if __name__ == "__main__":

    print("######################## Gathering Installed Programs List ########################")

    output_folder = os.path.join(os.getcwd(), "results")
    create_software_table_as_file(output_folder)
    
    print("Script completed")
    
