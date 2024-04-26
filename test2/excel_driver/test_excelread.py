import openpyxl
import json
from test2.excel_driver.api_key import Api

excel_file = openpyxl.load_workbook('../data/api_cases.xlsx')
sheet = excel_file['Sheet1']
r = 0
ak = Api()

for value in sheet.values:
    r += 1
    data = value[5]
    assert_result = value[7]
    expect_result = value[8]
    print("Value[4]:", value[4])  # Print out the value before parsing
    try:
        dict_data = {
            'url': value[1] + value[2],
            'headers': json.loads(value[4]),  # Parse headers as JSON
            'params': json.loads(data)  # Parse params as JSON
        }
    except json.JSONDecodeError as e:
        print("Error parsing JSON:", e)
        dict_data = None
    print(dict_data)
    #... Continue executing test cases...

   #使用反射模拟请求
    if value[3] == 'get':
        result = ak.get(**dict_data)
    elif value[3] == 'post':
        result = ak.post(**dict_data)
    else:
        print("请求方法错误")