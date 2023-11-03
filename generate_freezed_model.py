import json
from typing import Union

def capitalize_first_letter(s: str) -> str:
    return s[0].upper() + s[1:] if s else ""


def generate_freezed_model(json_data: Union[dict, str], model_name: str = "MyModel") -> str:
    if isinstance(json_data, str):
        json_data = json.loads(json_data)

    fields = ""
    nested_models = ""

    for key, value in json_data.items():
        dart_type = ""
        defalut_value = ""
        capitalized_key = capitalize_first_letter(key)
        if isinstance(value, str):
            dart_type = "String"
            defalut_value = "@Default('')"
        elif isinstance(value, int):
            dart_type = "int"
            defalut_value = "@Default(0)"
        elif isinstance(value, float):
            dart_type = "double"
            defalut_value = "@Default(0.0)"
        elif isinstance(value, bool):
            dart_type = "bool"
            defalut_value = "@Default(false)"
        elif isinstance(value, list):
            defalut_value = "@Default([])"
            if value:  # Check if the list is not empty
                list_item = value[0]
                if isinstance(list_item, dict):
                    nested_model_name = f"{capitalized_key}"
                    nested_model = generate_freezed_model(list_item, nested_model_name)
                    nested_models += nested_model
                    dart_type = f"List<{nested_model_name}>"
                elif isinstance(list_item, str):
                    dart_type = "List<String>"
                elif isinstance(list_item, int):
                    dart_type = "List<int>"
                elif isinstance(list_item, float):
                    dart_type = "List<double>"
                elif isinstance(list_item, bool):
                    dart_type = "List<bool>"
                else:
                    dart_type = "List<dynamic>"
            else:
                dart_type = "List<dynamic>"
        elif isinstance(value, dict):
            nested_model_name = f"{capitalized_key}"
            nested_model = generate_freezed_model(value, nested_model_name)
            nested_models += nested_model
            dart_type = nested_model_name
        else:
            continue
        nullable = "" if defalut_value else "?"
        fields += f"  {defalut_value} {dart_type}{nullable} {key},\n"
    
    model = f"""
@freezed
 class {model_name} with _${model_name} {{
  const {model_name}._();  
    
  @JsonSerializable(explicitToJson: true)  
  const factory {model_name}({{
{fields.rstrip()}
  }}) = _{model_name};
  
  factory {model_name}.fromJson(Map<String, dynamic> json) => _${model_name}FromJson(json);
}}
"""

    return nested_models + model

input = ""
with open("input/input.json") as f:
    input = f.read()
dart_model = generate_freezed_model(input)
print(dart_model)

with open('output/freezed_output.dart', mode='w') as f:
    f.write(dart_model)