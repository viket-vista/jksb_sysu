import hashlib
import base64
import os

import requests
import json

# 企业微信机器人的webhook
web_hook = ''

# 文本形式
def sendBot_text(robot_web_hook: str, mes: str):
    '''
    :param url:   传入企业微信机器人webhoot
    :param robot_web_hook:  微信机器人的webhook
    :param mes:  文本信息
    :return:
    '''
    data = {"msgtype": "text", "text": {"content": mes}}
    data_json = json.dumps(data)
    print('推送的json%s' % data_json)
    prequte = requests.post(robot_web_hook, data=data_json)
    return prequte.text

# markdown形式
def sendBot_markdown(robot_web_hook: str, md: str):
    '''
    :param url:   传入企业微信机器人webhoot
    :param robot_web_hook:  微信机器人的webhook
    :param md:  markdown文本
    :return:
    '''
    data = {"msgtype": "markdown", "markdown": {"content": md}}
    data_json = json.dumps(data)
    print('推送的json%s' % data_json)
    prequte = requests.post(robot_web_hook, data=data_json)
    return prequte.text


def sendBot_image(robot_web_hook: str, image_path: str):
    '''
    :param url:   传入企业微信机器人webhoot
    :param image_path:  本地图片路径
    :return:
    '''
    with open(image_path, "br") as f:
        fcont = f.read()
        # 转化图片的base64
        ls_f = base64.b64encode(fcont)
        # 计算图片的md5
        fmd5 = hashlib.md5(fcont)
    data = {"msgtype": "image", "image": {"base64": ls_f.decode('utf8'), "md5": fmd5.hexdigest()}}
    data_json = json.dumps(data)
    print('推送的json%s' % data_json)
    prequte = requests.post(robot_web_hook, data=data_json)
    return prequte.text

# demo
if __name__ == '__main__':
    # text
    sendBot_text(web_hook, "打卡啦！！！")
    # markdown
    sendBot_markdown(web_hook, "实时新增用户反馈<font color=\"warning\">132例</font>，请相关同事注意。\n \
         >类型:<font color=\"comment\">用户反馈</font>\
         >普通用户反馈:<font color=\"comment\">117例</font>\
         >VIP用户反馈:<font color=\"comment\">15例</font>")
    # markdown
    sendBot_image(web_hook, os.path.join(os.getcwd(), 'daka.png'))
