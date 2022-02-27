from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message
# import getcontest

import requests
from urllib import request
from pprint import pprint

url = "http://algcontest.rainng.com/"
ojs = ["CodeForces", "AtCoder"]


def getcontest():
    re = requests.get(url=url)
    data = re.json()
    # pprint(data)
    res = []
    for each in data:
        if each["oj"] in ojs:
            # pprint(each)
            res.append(each)

    pprint(res)
    return res


contest = on_keyword(['contest', '比赛'], priority=1)


@contest.handle()
async def contest_handle(bot: Bot, event: Event):
    contestList = getcontest()
    s = f"[CQ:at,qq={event.get_user_id()}]" + "找到最近的" + str(
        len(contestList)) + "场比赛：\n"
    for each in contestList:
        s += "比赛名称：" + each["name"] + '\n'
        s += "比赛时间：" + each["startTime"] + '\n'
        s += "比赛链接：" + each["link"] + '\n'
    await contest.finish(Message(s))
    # await contest.finish(
    #     Message(
    #         f'[CQ:at,qq={event.get_user_id()}]您今日的幸运指数是{lucknum}/100（越低越好），为"{luck_simple(lucknum)}"'
    #     ))
