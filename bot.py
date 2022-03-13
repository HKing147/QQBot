#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nonebot
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter
from nonebot.adapters.mirai2 import Adapter as MIRAI2_Adapter

# Custom your logger
#
# from nonebot.log import logger, default_format
# logger.add("error.log",
#            rotation="00:00",
#            diagnose=False,
#            level="ERROR",
#            format=default_format)

# You can pass some keyword args config to init function
nonebot.init()
# nonebot.init(custom_config1="config in env file")
# nonebot.init(_env_file=".env.dev")

app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)

nonebot.load_builtin_plugins("echo")
nonebot.load_plugin("nonebot_plugin_emojimix") # emoji合并
nonebot.load_plugin("nonebot_plugin_remake") # 人生重开器remake
nonebot.load_plugin("nonebot_plugin_wordcloud") # 词云
nonebot.load_plugin("nonebot_plugin_status") # 服务器状态
nonebot.load_plugin("nonebot_plugin_web") # 网页端监控机器人（可以监控到消息，但不能发送消息）// modify
nonebot.load_plugin("nonebot_plugin_setu") # 涩图 // modify
nonebot.load_plugin("nonebot_plugin_withdraw") # 机器人消息撤回
nonebot.load_plugin("nonebot_plugin_petpet") # 表情包制作（摸头...）
nonebot.load_plugin("nonebot_plugin_memes") # 表情包制作（狂粉...）
nonebot.load_plugin("nonebot_plugin_antiflash") # 群聊自动反闪照
# nonebot.load_plugin("random_cat_gif") # 随机猫猫 （pip安装）pip3 install random_cat_gif
nonebot.load_plugin("nonebot_plugin_apscheduler") # 定时任务
# nonebot.load_plugin("nonebot_plugin_autohelp") # help功能
nonebot.load_plugins("./qqbot/plugins") # 本地插件

# nonebot.load_plugin("nonebot_plugin_code")
# nonebot.load_plugin("nonebot_plugin_chess")
# nonebot.load_plugin("haruka_bot")
# nonebot.load_plugin("nonebot_plugin_code")
# nonebot.load_plugin("nonebot_plugin_setu2")
# nonebot.load_plugin("nonebot_plugin_setu")
# Please DO NOT modify this file unless you know what you are doing!
# As an alternative, you should use command `nb` or modify `pyproject.toml` to load plugins
# nonebot.load_from_toml("pyproject.toml")

# Modify some config / config depends on loaded configs
#
# config = driver.config
# do something...

if __name__ == "__main__":
    nonebot.logger.warning(
        "Always use `nb run` to start the bot instead of manually running!")
    nonebot.run(app="__mp_main__:app")
