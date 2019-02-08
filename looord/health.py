from datetime import datetime
import time

import pytz

_start_time = None


def write_now_datetime():
    now = datetime.now(tz=pytz.timezone('Asia/Seoul'))
    now_str = now.strftime('%Y-%m-%d %H:%M:%S.%f')
    with open('./healthcheck.txt', 'w') as f:
        f.write(
            'Health checker executed at: {}\n'.format(_start_time)
            'Last checked: {}'.format(now_str)
        )
    return None


def run_heath_check(*args, **kwargs):
    global _start_time
    _start_time =  datetime.now(tz=pytz.timezone('Asia/Seoul')).strftime('%Y-%m-%d %H:%M:%S.%f')
    while True:
        write_now_datetime()
        time.sleep(10)
