import os
import json

def remove_localized_keys(obj):
    if isinstance(obj, dict):
        return {
            key: remove_localized_keys(value)
            for key, value in obj.items()
            if "localized" not in key.lower()
        }
    elif isinstance(obj, list):
        return [remove_localized_keys(item) for item in obj]
    else:
        return obj

def convert_structure(data):
    properties = {
        'Legendary': {},
        'Paragon (Board)': {},
        'Paragon (Glyph)': {},
        'Paragon (Node)': {},
        'Skill Tree': {},
        'Unique': {},
    }
    classes = {}

    for _class_ in data.keys():
        classes[_class_] = {}

    reformatted_structure = properties

    for _class_ in classes:
        for _property_ in properties:
            if not (_class_ in data and _property_ in data[_class_] and data[_class_][_property_]):
                continue
            class_property = data[_class_][_property_]
            reformatted_structure[_property_][_class_] = class_property

    return reformatted_structure

def parse_paragon_board(data):
    for _class_ in data["Paragon (Board)"]:
        for _board_ in data["Paragon (Board)"][_class_]:
            board_arr = []
            for _string_ in data["Paragon (Board)"][_class_][_board_]['data']:
                board_arr.append(_string_.split(','))
            data["Paragon (Board)"][_class_][_board_] = board_arr
        
    return data

def process_json_files():
    input_file_path = "D4_Paragon_Testing/d4_data.json"
    output_file_no_localized = "D4_Paragon_Testing/d4_data_no_localized.json"  
    output_file_reformatted = "D4_Paragon_Testing/d4_data_reformatted.json" 
    output_file_parsed_paragon = "D4_Paragon_Testing/d4_data_parsed_paragon.json"
    
    if os.path.exists(input_file_path):
        with open(input_file_path, 'r') as input_file:
            data = json.load(input_file)

        # Remove localized keys and save to output_file_no_localized
        modified_data = remove_localized_keys(data)
        with open(output_file_no_localized, 'w') as output_file:
            json.dump(modified_data, output_file, indent=4)
        print(f"Modified JSON (no localized keys) written to {output_file_no_localized}")

        # Convert the structure and save to output_file_reformatted
        new_data = convert_structure(modified_data)
        with open(output_file_reformatted, 'w') as output_file:
            json.dump(new_data, output_file, indent=4)
        print(f"Modified JSON (reformatted) written to {output_file_reformatted}")
        
        # Parse the new structure's paragon boards and save to output_file_parsed_paragon
        parsed_data = parse_paragon_board(new_data)

        with open(output_file_parsed_paragon, 'w') as output_file:
            json.dump(parsed_data, output_file, indent=4)
        print(f"Modified JSON (parsed paragon boards) written to {output_file_parsed_paragon}")
        
        
        # Remove placeholder files because I'm too lazy to just carry data between functions
        os.remove("D4_Paragon_Testing/d4_data_no_localized.json")
        print(f"Removed _no_localized file")
        os.remove("D4_Paragon_Testing/d4_data_reformatted.json" )
        print(f"Removed _reformatted file")
    else:
        print(f"Input file {input_file_path} does not exist.")

if __name__ == "__main__":
    process_json_files()
