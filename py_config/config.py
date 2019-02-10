import json

PATH_PROXY = 'config/proxy.txt'
PATH_UNIT = 'config/personium_unit.txt'
PATH_CELL_LIST = 'config/personium_cell_list.txt'


def update_config_proxy(data):

    with open(PATH_PROXY, 'r') as f:
        json_contents = json.load(f)
    json_contents['http']['host']['host'] = data['http_host']
    json_contents['http']['host']['port'] = data['http_port']
    json_contents['http']['user']['user'] = data['http_user']
    json_contents['http']['user']['password'] = data['http_password']
    json_contents['https']['host']['host'] = data['https_host']
    json_contents['https']['host']['port'] = data['https_port']
    json_contents['https']['user']['user'] = data['https_user']
    json_contents['https']['user']['password'] = data['https_password']
    with open(PATH_PROXY, 'w') as f:
        json.dump(json_contents, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ' : '))
    return json_contents

def update_config_unit(data):
    with open(PATH_UNIT, 'r') as f:
        json_contents = json.load(f)
    json_contents['unit_name'] = data
    with open(PATH_UNIT, 'w') as f:
        json.dump(json_contents, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ' : '))
    return json_contents

def get_config_cell_list():
    return 

def add_config_cell_list():
    return
def update_config_cell_list():
    return

def get_config_cell_account(cell_name):
    with open(PATH_CELL_LIST, 'r') as f:
        json_contents = json.load(f)
    return json_contents[cell_name]

def get_config_unit():
    with open(PATH_UNIT, 'r') as f:
        json_contents = json.load(f)
    return json_contents["unit_name"]
    