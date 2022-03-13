from nonebot.dependencies import CustomConfig
from nonebot.permission import SUPERUSER
from nonebot import on_command
from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message
from pprint import pprint
import datetime
import json
import nonebot
import requests
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot import require
import random
import time
import xlsxwriter as xw

# groupList=[]

def xw_toExcel(data, fileName): # xlsxwriter库储存数据到excel
    workbook = xw.Workbook(fileName) # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1") # 创建子表
    worksheet1.activate() # 激活表
    title = ['群号', '群名', '人数'] # 设置表头
    worksheet1.write_row('A1', title) # 从A1单元格开始写入表头
    i = 2 # 从第二行开始写入数据
    for j in range(len(data)):
        insertData = [
            data[j]["group_id"], data[j]["group_name"], data[j]["member_count"]
        ]
        row = 'A' + str(i)
        worksheet1.write_row(row, insertData)
        i += 1
    workbook.close() # 关闭表



group_id_list = [768973940,680787176,830923571,397204493,975489008,984321694,368384017,972152209,230334759,587985749,752832374,
        595700302,838282181,584769166,982015308,793856405,589631009,416352754,747091972,825929430,752778614]
# group_id_list = [768973940]



group = on_keyword(["统计群人数"], priority=2,permission=SUPERUSER)
@group.handle()
async def group_handle(bot: Bot, event: Event):
    groupList = []
    # s = ''
    for group_id in group_id_list:
        groupInfo = await bot.call_api("get_group_info",group_id=group_id)
        pprint(groupInfo)
        # s = s + groupInfo['group_name'] + '目前有: ' + str(groupInfo['member_count']) + '人\n'
        groupList.append(groupInfo)
    
    xw_toExcel(groupList, '../1.xlsx')

    await bot.call_api('upload_group_file',group_id = event.group_id,file = './1.xlsx',name = '1.xlsx')
    # await bot.call_api('upload_group_file',group_id = event.group_id,file = './1.txt',name = '1.txt')
    # time.sleep(3)
    # await group.finish(Message(s))
    # id = 312329114
    # id = event.group_id
    # await group.finish(Message(str(id)))
    # await bot.send_msg(
    #     message_type="group",
    #     group_id=int(id),
    #     message=MessageSegment.image(file = './1.txt')           
    # )
 


