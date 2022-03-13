from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message

# import requests
# from urllib import request
# from pprint import pprint

url = "http://algcontest.rainng.com/"
ojs = ["CodeForces", "AtCoder"]


help = on_command('help', priority=1)


@help.handle()
async def help_handle(bot: Bot, event: Event):
    
    # s = f"[CQ:at,qq={event.get_user_id()}]" + "找到最近的" + str(
    #     len(contestList)) + "场比赛：\n"
    #  '随机猫图: 来个猫猫\n' + \
    s = '每日一题: div1 / div2\n' + \
        '近期比赛: contest\n' + \
        'CF比赛: cf\n' + \
        'ATC比赛: atc\n' + \
        'NowCoder比赛: nc\n' + \
        'emoji合成: 🐶+🐵\n' + \
        '头像表情包: 摸+@user/图片\n' + \
        '表情包制作: 表情包制作\n' + \
        '群聊词云: (我的)今日词云\n' + \
        '人生重开: @bot remake\n' + \
        '今日人品: 今日人品/jrrp\n' + \
        '在线运行代码: code py/cpp [-i]\n'
        
    await help.finish(Message(s))
    # await contest.finish(
    #     Message(
    #         f'[CQ:at,qq={event.get_user_id()}]您今日的幸运指数是{lucknum}/100（越低越好），为"{luck_simple(lucknum)}"'
    #     ))
