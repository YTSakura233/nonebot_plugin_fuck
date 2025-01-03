<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>

<div align="center">

# nonebot_plugin_fuck

_✨ NoneBot 机器人攻击群友插件 ✨_

</div>

<p align="center">
  <a href="https://raw.githubusercontent.com/cscs181/QQ-Github-Bot/master/LICENSE">
    <img src="https://img.shields.io/github/license/cscs181/QQ-Github-Bot.svg" alt="license">
  </a>
  <a href="https://pypi.python.org/pypi/nonebot-plugin-analysis-bilibili">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-analysis-bilibili.svg" alt="pypi">
  </a>
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">
</p>

## 使用方式

* 直接在群里正常聊天，即可随机被机器人骂
* 发送“骂我”，直接被机器人骂
* 发送“插入脏话XXX”可向文件中插入脏话

## 额外配置项(可选)

在配置文件中加入(需要什么加什么)

```
# 是否开启本插件
fuck = true # 默认为False
# 100%攻击对象（发送消息必攻击）
fuck_user = [''] 
# 开启群组
fuck_group = []
# 随机概率
random = #默认0.10(1%)
```

## 安装


1. 使用 pip 安装和更新，初次安装需要手动添加入口 （新版默认不带 bot.py 文件）

```
pip install --upgrade nonebot_plugin_fuck
```

pip 安装后在 Nonebot2 入口文件（例如 bot.py ）增加：

```python
nonebot.load_plugin("nonebot_plugin_fuck")
```