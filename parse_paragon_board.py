import os
import json


def do_something_with_(data):

        
    return data

def process_json_files():
    input_file_path = "D4_Paragon_Testing/d4_data_reformatted.json"
    
    if os.path.exists(input_file_path):
        with open(input_file_path, 'r') as input_file:
            data = json.load(input_file)


        # Process Data
        new_data = do_something_with_(data)
        
    

if __name__ == "__main__":
    process_json_files()
