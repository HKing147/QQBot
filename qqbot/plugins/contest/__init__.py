from nonebot.plugin import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message
import requests
from urllib import request
from pprint import pprint
from lxml import etree #首先导入lxml库的etree模块

url = "http://algcontest.rainng.com/"
ojs = ["CodeForces", "AtCoder","NowCoder"]


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

contest = on_command('contest', priority=1)

@contest.handle()
async def contest_handle(bot: Bot, event: Event):
    contestList = getcontest()
    ATCcontestList = get_ATC_contest()
    for each in ATCcontestList:
        contestList.append(each)
    s = f"[CQ:at,qq={event.get_user_id()}]" + "找到最近的" + str(
        len(contestList)) + "场比赛：\n"
    for each in contestList:
        s += "比赛名称：" + each["name"] + '\n'
        s += "比赛时间：" + each["startTime"] + '\n'
        s += "比赛链接：" + each["link"] + '\n'
    await contest.finish(Message(s))

############# CodeForces #############
CF = on_command('cf', priority=1)

@CF.handle()
async def CF_handle(bot: Bot, event: Event):
    contestList = getcontest()
    CFcontestList = []
    for each in contestList:
        if each['oj'] == 'CodeForces':
            CFcontestList.append(each)
    s = f"[CQ:at,qq={event.get_user_id()}]" + "找到CodeForces最近的" + str(
        len(CFcontestList)) + "场比赛：\n"
    for each in CFcontestList:
        s += "比赛名称：" + each["name"] + '\n'
        s += "比赛时间：" + each["startTime"] + '\n'
        s += "比赛链接：" + each["link"] + '\n'
    await CF.finish(Message(s))


############# AtCoder #############

def get_ATC_contest():
    url = "https://atcoder.jp/contests/"
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    res = requests.get(url=url, headers=headers)
    html = etree.HTML(res.content.decode('utf-8'))
    table = html.xpath('//*[@id="contest-table-upcoming"]/div/div/table')[0]
    # table = html.xpath(
    # '/html/body/div[1]/div/div[1]/div[3]/div[2]/div/div/table')[0]
    timeList = table.xpath(
        ".//td[1]//text()") # 获取当前tr标签下的第一个td标签，并用text()方法获取文本内容，赋值给p
    Names = table.xpath(".//td[2]//text()")
    Links = table.xpath(".//td[2]//a//@href")
    # pprint(Links)
    baseURL = 'https://atcoder.jp'
    LinkList = []
    for each in Links:
        LinkList.append(baseURL + each)
    # pprint(LinkList)
    NameList = []
    for i in range(len(Names)):
        if i % 7 == 5:
            NameList.append(Names[i])

    duration = table.xpath(".//td[3]//text()")
    # pprint(duration)
    # pprint(timeList)
    # pprint(NameList)

    contestList = []
    for i in range(len(NameList)):
        contest = {}
        contest['name'] = NameList[i]
        contest['startTime'] = timeList[i][:-5]
        contest['link'] = LinkList[i]
        # pprint(contest)
        contestList.append(contest)

    pprint(contestList)
    return contestList

ATC = on_command('atc', priority=1)

@ATC.handle()
async def ATC_handle(bot: Bot, event: Event):
    contestList = get_ATC_contest()
    s = f"[CQ:at,qq={event.get_user_id()}]" + "找到AtCoder最近的" + str(
        len(contestList)) + "场比赛：\n"
    for each in contestList:
        s += "比赛名称：" + each["name"] + '\n'
        s += "比赛时间：" + each["startTime"] + '\n'
        s += "比赛链接：" + each["link"] + '\n'
    await ATC.finish(Message(s))
 

 
############# NowCoder #############
NC = on_command('nc', priority=1)

@NC.handle()
async def NC_handle(bot: Bot, event: Event):
    contestList = getcontest()
    NCcontestList = []
    for each in contestList:
        if each['oj'] == 'NowCoder':
            NCcontestList.append(each)
    s = f"[CQ:at,qq={event.get_user_id()}]" + "找到NowCoder最近的" + str(
        len(NCcontestList)) + "场比赛：\n"
    for each in NCcontestList:
        s += "比赛名称：" + each["name"] + '\n'
        s += "比赛时间：" + each["startTime"] + '\n'
        s += "比赛链接：" + each["link"] + '\n'
    await NC.finish(Message(s))


