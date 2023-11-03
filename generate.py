'''
input/input.jsonにjsonオブジェクトを入力します。
以下のコマンドを実行します。

python3 generate.py

output/freezed_output.dartにfreezedのモデルが出力されます。

output/freezed_output.dartにfreezedのモデルが出力されます。
'''

from generate_freezed_model import generate_freezed_model
from generate_josn_mock import multiply_json


input = ""
with open("input/input.json") as f:
    input = f.read()

output_json = multiply_json(input)
dart_model = generate_freezed_model(input)

with open('output/multiplied_output.json', mode='w') as f:
    f.write(output_json)

with open('output/freezed_output.dart', mode='w') as f:
    f.write(dart_model)