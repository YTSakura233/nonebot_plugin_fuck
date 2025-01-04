import nonebot
from nonebot import on_command, on_regex
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Message, MessageSegment
from nonebot.params import EventMessage, CommandArg, EventToMe

import random

config = nonebot.get_driver().config
FUCK = getattr(config, 'fuck', False)
FUCK_USER = getattr(config, 'fuck_user', [''])
FUCK_GROUP = getattr(config, 'fuck_group', [])
RANDOM = getattr(config, 'random', 0.10)

def active() -> bool:
    return True if FUCK else False

FUCK_PATH = "./text.txt"

fuck = on_regex(r"[\s\S]*", priority=20, rule=active)
fuck1 = on_command("骂我", priority=20, rule=active)
fuck2 = on_command('骂他', aliases={'骂她', '骂它'}, priority=20, rule=active)
insert = on_command("插入脏话", priority=20, rule=active)

# 进行随机
def random_unit(p):
    if p == 0:  # 概率为0，直接返回False
        return False
    if p == 1:  # 概率为1，直接返回True
        return True
    p_digits = len(str(p).split(".")[1])
    interval_begin = 1
    interval__end = pow(10, p_digits)
    R = random.randint(interval_begin, interval__end)
    if float(R)/interval__end < p:
        return True
    else:
        return False

def get_word():
    fuck_file = open(FUCK_PATH, "r", encoding="utf-8")
    fuck_lines = fuck_file.readlines()
    fuck_file.close()
    fuck_words = [line for line in fuck_lines]
    word = random.choice(fuck_words)
    if "xxx" in word:
        word.replace('xxx', '你')
    return word

@fuck.handle()
async def _(event: GroupMessageEvent, message: Message = EventMessage()):
    if event.group_id in FUCK_GROUP:
        if event.get_user_id() in FUCK_USER:
            await fuck.send([MessageSegment.reply(event.message_id), MessageSegment.text(get_word())])
        elif event.is_tome():
            await fuck.send([MessageSegment.reply(event.message_id), MessageSegment.text(get_word())])
        else:
            # 设置随机概率
            p = RANDOM
            R = random_unit(p)
            if R:
                await fuck.send([MessageSegment.reply(event.message_id), MessageSegment.text(get_word())])

@fuck1.handle()
async def _(event: GroupMessageEvent, message: Message = EventMessage()):
    if event.group_id in FUCK_GROUP:
        await fuck1.send([MessageSegment.reply(event.message_id), MessageSegment.text(get_word())])

@fuck2.handle()
async def _(event: GroupMessageEvent, message: Message = CommandArg()):
    if event.group_id in FUCK_GROUP:
        a = str(message)
        qq = re.search(r"qq=(\d+)", a).group(1)
        await fuck2.send([MessageSegment.at(qq), MessageSegment.text(f"{get_word()}")])

@insert.handle()
async def _(event: GroupMessageEvent, message: Message = CommandArg()):
    if event.group_id in FUCK_GROUP:
        new = str(message)
        try:
            with open(FUCK_PATH, 'a', encoding="utf-8") as f:
                f.write('\n')
                f.write(new)
                f.close()
            await insert.send([MessageSegment.reply(event.message_id), MessageSegment.text("插入成功")])
        except Exception as e:
            await insert.send([MessageSegment.reply(event.message_id), MessageSegment.text(f"插入失败，请联系机修:{e}")])

