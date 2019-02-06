from datetime import datetime

import pytz

_bot_start_time = None
_chat_num = 0  # number of chatting after startup (include command)
_command_num = 0  # num of command after startup


def set_bot_start_time():
    global _bot_start_time
    if _bot_start_time is not None:
        return None
    _bot_start_time = datetime.now(tz=pytz.timezone('Asia/Seoul'))
    return None


def get_startup_time_delta():
    global _bot_start_time
    delta = (datetime.now(tz=pytz.timezone('Asia/Seoul')) - _bot_start_time).seconds
    days = delta // (3600 * 24)
    hours = delta % (3600 * 24) // 3600
    minutes = delta % (3600 * 24) % 3600 // 60
    seconds = delta % (3600 * 24) % 3600 % 60
    return days, hours, minutes, seconds


def get_start_time():
    global _bot_start_time
    return _bot_start_time.strftime('%Y.%m.%d %H:%M:%S')


def get_uptime():
    days, hours, minutes, seconds = get_startup_time_delta()
    return '{upt_d}d {upt_h}h {upt_m}m {upt_s}s'.format(
        upt_d=days,
        upt_h=hours,
        upt_m=minutes,
        upt_s=seconds
    )


def find_chat():
    global _chat_num
    _chat_num += 1


def get_num_chat():
    global _chat_num
    return _chat_num


def find_command():
    global _command_num
    _command_num += 1


def get_num_command():
    global _command_num
    return _command_num

