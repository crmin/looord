import pytest
from commands.commands import get_command_func
from commands import functions


@pytest.mark.parametrize('msg,func,params', [
    ('$머즐', functions.muzzle, []),
    ('$분대장이 누구야', None, []),
    ('$분대장', functions.leader, []),
    ('$도움', functions.bot_help, []),
    ('$전적 Rakia. Leaky_ReLU', functions.history, ['rakia.']),
    ('testtest $도움 $분대장 $전적 Rakia.', functions.bot_help, []),
    ('$muz mp9 ak', functions.muzzle, ['mp9']),
    ('testest', None, []),
])
def test_get_command_func(msg, func, params):
    res = get_command_func(msg)
    assert (func, params) == (res['function'], res['parameters'])
