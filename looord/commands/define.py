"""
parameters는 명령어 뒤에 따라나오는 parameter의 개수를 나타냅니다
    * 0: 없음
    * -1: 1 이상
    * 1~: parameter 개수
"""


prefix = '$'
commands = {
    'bot_help': {
        'parameters': 0,
        'check_method': 'in',
        'message': ['도움', 'ㄷㅇ', 'help'],
        'help': '명령어 목록과 사용법을 확인합니다'
    },
    'leader': {
        'parameters': 0,
        'check_method': 'in',
        'message': ['분대장', 'ㅂㄷㅈ', 'leader'],
        'help': '오늘의 분대장 선택 (현재 online인 멤버 중에서 랜덤으로 선택합니다)'
    },
    'ack': {
        'parameters': 0,
        'check_method': 'in',
        'message': ['ack'],
        'help': '봇의 연결 상태를 확인합니다. TCP 3 way handshake'
    },
    'history': {
        'parameters': 1,
        'check_method': 'in',
        'message': ['전적', 'ㅈㅈ', 'ㅉ', 'history', 'hist'],
        'help': 'r6stats에 기록되어있는 전적 요약을 가져옵니다'
    },
    'random_ops': {
        'parameters': 0,
        'check_method': 'in',
        'message': ['랜덤', 'ㄹㄷ', 'random', 'rand'],
        'help': '공격팀, 방어팀에서 랜덤하게 3개의 오퍼를 선택해서 보여줍니다'
    },
    'muzzle': {
        'parameters': 1,
        'check_method': 'in',
        'message': ['머즐', 'ㅁㅈ', 'muzzle', 'muz'],
        'help': '총구 부착물 추천 참고: https://www.reddit.com/comments/9dk0pm'
    },
}
