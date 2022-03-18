import requests,json
def read_json():
    """
    从config.json读取配置文件
    """
    with open("config.json",'r') as load_f:
      load_dict = json.load(load_f)
    return load_dict
