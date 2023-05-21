# -*- encoding: utf-8 -*-
'''
@File    :   preprocess_wx.py   
@Contact :   13105350231@163.com
@License :   (C)Copyright 2022-2025
@Desciption : 预处理微信聊天记录

@Modify Time      @Author    @Version   
------------      -------    --------   
2023/5/20 20:01   fxk        1.0         
'''
import pandas as pd
import os

# 朋友或者群聊的id
TALKER = "43261986283@chatroom"
# 聊天记录csv文件的地址
MESSAGES_PATH = "F:\\miui\\20230520_165436\\message.csv"


def readCsv(url):
    df = pd.read_csv(url, encoding="gbk", encoding_errors="ignore")
    return df


if __name__ == '__main__':
    messages = readCsv(MESSAGES_PATH)
    messages = messages[messages['talker'] == TALKER]
    messages = messages[messages["content"].str.len() < 20]
    messages = messages["content"]
    print(messages.info)
    messages.to_csv('1_wx.txt', sep='\t', index=False)
