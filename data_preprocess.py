#!/usr/bin/env python
# coding: utf-8
from emojiswitch import demojize
import re


def txt_preprocess(content):
    
    # 去除換行符號等
    content = content.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    # 去除某個顯示不出來的emoji編碼與空白
    content = content.replace("\u200d♀", "")
    # 去除底線
    content = content.replace("_","").replace("＿","")
    # 去除超連結
    content = re.sub(r'[a-zA-z]+://[^\s]*', ' ', content)
    content = re.sub(r'[w{3}]+[^\s]*', ' ', content)
    # emoji轉中文
    output = demojize(content, delimiters=("_", "_"), lang="zh")
    
    return output

