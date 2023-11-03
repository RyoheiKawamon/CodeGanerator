import json

def multiply_string(value):
    if isinstance(value, str):
        return value * 10
    elif isinstance(value, dict):
        return {k: multiply_string(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [multiply_string(v) for v in value]
    else:
        return value
    
def multiply_json(value):
    input_dict = json.loads(value)
    output_dict = multiply_string(input_dict)
    return json.dumps(output_dict, ensure_ascii=False)


input = ""
with open("input/input.json") as f:
    input = f.read()

output_json = multiply_json(input)

with open('output/multiplied_output.json', mode='w') as f:
    f.write(output_json)
    