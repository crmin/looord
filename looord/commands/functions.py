import os

import discord
from numpy import random

from commands import constants
from commands import msg_frame
from commands.crawler import r6stats, server_stat
from commands.define import commands, prefix
from commands.utils import get_online_members


async def bot_help(client, message, params, *args, **kwargs):
    embed = discord.Embed(
        title='**How to use looord bot?**',
        color=0x93263f
    )
    for comm_func, comm_v in commands.items():
        embed.add_field(
            name='{prefix}({commands})'.format(prefix=prefix, commands='|'.join(comm_v['message'])),
            value='{desc}'.format(desc=comm_v['help']),
            inline=False
        )
    return await client.send_message(message.channel, embed=embed)


async def leader(client, message, params, *args, **kwargs):
    online_members = get_online_members(message.channel)
    today_leader = random.choice(online_members)
    embed = discord.Embed(
        title='오늘의 분대장은?',
        description='{}'.format(today_leader.mention),
        color=0x93263f
    )
    return await client.send_message(message.channel, embed=embed)


async def ack(client, message, params, *args, **kwargs):
    return await client.send_message(message.channel, 'ack')


async def history(client, message, params, *args, **kwargs):
    path = r6stats.save_history(params[0])
    await client.send_file(message.channel, path)
    os.remove(path)
    return None


async def random_ops(client, message, params, *args, **kwargs):
    random.shuffle(constants.defenders)
    random.shuffle(constants.attackers)
    def_sample = '\n'.join(['* {}'.format(each) for each in constants.defenders[:3]])
    atk_sample = '\n'.join(['* {}'.format(each) for each in constants.attackers[:3]])
    embed = discord.Embed(
        title='Random Ops',
        description='*아래 오퍼 중 순서대로 골라주세요. 앞에 있는 오퍼의 우선순위가 높습니다.*',
        color=0x93263f
    )
    embed.add_field(name='Attacker :gun:', value='{}'.format(atk_sample), inline=True)
    embed.add_field(name='Defender :shield:', value='{}'.format(def_sample), inline=True)
    return await client.send_message(message.channel, embed=embed)


async def muzzle(client, message, params, *args, **kwargs):
    gun_name = params[0]
    is_found = False
    embed = discord.Embed(
        title='총구 부착물 :gun:',
        description='{}이(가) 포함되는 총에 대한 부착물을 보여줍니다'.format(gun_name),
        color=0x93263f
    )
    if len(gun_name) < 2:
        embed.add_field(
            name='Error: Too short gun name',
            value='두 글자 이상 검색해주세요'.format(gun_name),
            inline=False
        )
    else:
        for gun, attachment in constants.gun2attachment.items():
            if gun_name.lower() in gun.lower():
                embed.add_field(
                    name=gun,
                    value='{att} ({att_kor})'.format(att=attachment, att_kor=constants.attachment_kor[attachment]),
                    inline=True
                )
                is_found = True
        if not is_found:
            embed.add_field(
                name='Error: Not found',
                value='{}가 포함되는 총기를 찾을 수 없습니다'.format(gun_name),
                inline=False
            )
    return await client.send_message(message.channel, embed=embed)


async def magical_conch(client, message, params, *args, **kwargs):
    pick_item = random.choice(params)
    embed = discord.Embed(
        title='마법의 소라고둥님',
        description='{} 중 어떤걸 선택할까요?'.format(', '.join(params)),
        color=0x93263f
    )
    embed.add_field(name='마법의 소라고둥께서 말하시길', value='||{}||'.format(pick_item), inline=False)
    embed.set_thumbnail(url='https://i.imgur.com/U6BsF6K.png')
    return await client.send_message(message.channel, embed=embed)


async def server_status(client, message, *args, **kwargs):
    error_num = server_stat.get_error_num()
    normal, warning, error = 0x17a2b8, 0xffc107, 0xdc3545
    status = normal
    if error_num >= 5:
        status = error
    elif error_num >= 3:
        status = warning
    embed = discord.Embed(
        title='r6s server status',
        description='{} (Reports in last 20 minutes)'.format(error_num),
        url='https://outage.report/rainbow-six',
        color=status
    )
    return await client.send_message(message.channel, embed=embed)
