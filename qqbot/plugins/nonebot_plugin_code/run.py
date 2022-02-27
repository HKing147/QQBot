# python3
# -*- coding: utf-8 -*-
# @Time    : 2021/11/22 14:17
# @Author  : yzyyz
# @Email   :  youzyyz1384@qq.com
# @File    : run.py
# @Software: PyCharm
import re

import httpx

codeType = {
    'py': ['python', 'py'],
    'cpp': ['cpp', 'cpp'],
    'java': ['java', 'java'],
    'php': ['php', 'php'],
    'js': ['javascript', 'js'],
    'c': ['c', 'c'],
    'c#': ['csharp', 'cs'],
    'go': ['go', 'go'],
    'asm': ['assembly', 'asm']
}


async def run(strcode):
    strcode = strcode.replace('&amp;', '&').replace('&#91;',
                                                    '[').replace('&#93;', ']')
    print("=" * 30)
    print(strcode)
    print("=" * 30)
    strcode = strcode.lstrip("\n")
    firstline = ""
    a = []
    try:
        # a = re.findall(
        #     r'(py|php|java|cpp|js|c#|c|go|asm)\s?(-i)?\s?(\w*)?(\n|\r)((?:.|\n)+)',
        #     strcode)[0]
        # print(a)
        firstline = strcode.split('\n')[0]
        print(firstline)
        a = firstline.split(" ")
        print(a)
    except:
        return "输入有误汪\n目前仅支持c/cpp/c#/py/php/go/java/js"
    # if "-i" in strcode:
    if "-i" in a:
        lang = a[1]
        print(lang)
        stdin = firstline[9 + len(lang):]
        code = strcode[len(firstline):]
        # lang, code = a[1], a[4]
        dataJson = {
            "files": [{
                "name": f"main.{codeType[lang][1]}",
                "content": code
            }],
            "stdin": stdin,
            "command": ""
        }
    else:
        lang = a[1]
        code = strcode[len(firstline):]
        # lang, code = a[0], a[4]
        dataJson = {
            "files": [{
                "name": f"main.{codeType[lang][1]}",
                "content": code
            }],
            "stdin": "",
            "command": ""
        }
    headers = {
        "Authorization": "Token 0123456-789a-bcde-f012-3456789abcde",
        "content-type": "application/"
    }
    async with httpx.AsyncClient() as client:
        res = (await client.post(
            url=f'https://glot.io/run/{codeType[lang][0]}?version=latest',
            headers=headers,
            json=dataJson))
    print(dataJson)
    print("语言：", lang)
    print("类型：", codeType[lang])
    if res.status_code == 200:
        if res.json()['stdout'] != "":
            if len(repr(res.json()['stdout'])) < 1000:
                return res.json()['stdout']
            else:
                return "返回字符过长呐~~~"
        else:
            return res.json()['stderr'].strip()
