import os

from numpy import random

from looord.commands import constants
from looord.commands import msg_frame
from looord.commands.crawler import r6stats
from looord.commands.define import commands, prefix
from looord.commands.utils import get_online_members


async def bot_help(client, message, params, *args, **kwargs):
    msg_lst = []
    for comm_func, comm_v in commands.items():
        msg_lst.append('**{prefix}({commands})**: {desc}'.format(
            prefix=prefix,
            commands='|'.join(comm_v['message']),
            desc=comm_v['help']
        ))
    return await client.send_message(message.channel, '\n'.join(msg_lst))


async def leader(client, message, params, *args, **kwargs):
    online_members = get_online_members(client)
    today_leader = random.choice(online_members)
    return await client.send_message(message.channel, '오늘의 분대장은 ||{}||'.format(today_leader.mention))


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
    def_sample = ', '.join(constants.defenders[:3])
    atk_sample = ', '.join(constants.attackers[:3])
    msg = msg_frame.random_ops.format(
        atk_ops=atk_sample,
        def_ops=def_sample
    )
    return await client.send_message(message.channel, msg)


async def muzzle(client, message, params, *args, **kwargs):
    gun_name = params[0]
    gun_list = []
    for gun, attachment in constants.gun2attachment.items():
        if gun_name.lower() in gun.lower():
            gun_list.append(
                '{gun}: {att} ({att_kor})'.format(
                    gun=gun,
                    att=attachment,
                    att_kor=constants.attachment_kor[attachment]
                )
            )
    msg = '\n'.join(gun_list)
    if not msg:
        msg = '{}가 포함되는 총기를 찾을 수 없습니다'.format(gun_name)
    return await client.send_message(message.channel, msg)
