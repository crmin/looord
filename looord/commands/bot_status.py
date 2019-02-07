from datetime import datetime

import pytz

_bot_start_time = {}
_chat_num = {}  # number of chatting after startup (include command)
_command_num = {}  # num of command after startup


def set_bot_start_time(server=None, client=None):
    global _bot_start_time
    if server is None:  # set about all servers
        for server in client.servers:
            set_bot_start_time(server)
    else:
        if server.id in _bot_start_time:
            return None
        # is not exist
        _bot_start_time[server.id] = datetime.now(tz=pytz.timezone('Asia/Seoul'))
    return None


def get_startup_time_delta(server):
    global _bot_start_time
    if server.id not in _bot_start_time:
        _bot_start_time[server.id] = None
    delta = (datetime.now(tz=pytz.timezone('Asia/Seoul')) - _bot_start_time[server.id]).seconds
    days = delta // (3600 * 24)
    hours = delta % (3600 * 24) // 3600
    minutes = delta % (3600 * 24) % 3600 // 60
    seconds = delta % (3600 * 24) % 3600 % 60
    return days, hours, minutes, seconds


def get_start_time(server):
    global _bot_start_time
    if server.id not in _bot_start_time:
        _bot_start_time[server.id] = None
    return _bot_start_time[server.id].strftime('%Y.%m.%d %H:%M:%S')


def get_uptime(server):
    days, hours, minutes, seconds = get_startup_time_delta(server)
    return '{upt_d}d {upt_h}h {upt_m}m {upt_s}s'.format(
        upt_d=days,
        upt_h=hours,
        upt_m=minutes,
        upt_s=seconds
    )


def find_chat(channel):
    global _chat_num
    if channel.server.id not in _chat_num:
        _chat_num[channel.server.id] = 0
    _chat_num[channel.server.id] += 1


def get_num_chat(channel):
    global _chat_num
    if channel.server.id not in _chat_num:
        _chat_num[channel.server.id] = 0
    return _chat_num[channel.server.id]


def find_command(channel):
    global _command_num
    if channel.server.id not in _command_num:
        _command_num[channel.server.id] = 0
    _command_num[channel.server.id] += 1


def get_num_command(channel):
    global _command_num
    if channel.server.id not in _command_num:
        _command_num[channel.server.id] = 0
    return _command_num[channel.server.id]

