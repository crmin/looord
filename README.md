# Looord: R6S Discord bot

![Looord](https://i.imgur.com/EvGDuz0.png)
타찬카 버프좀

## Installation

### Selenium web driver
이 프로젝트는 (headless chrome을 사용하는) `$history` 명령어를 위해 chrome web driver가 필요합니다.

macOS나 Windows 환경에서는 [여기](http://chromedriver.chromium.org/downloads)에서 Chrome Webdriver를 다운로드 하실 수 있습니다.
chromedriver 파일은 `[project_root]/commands/crawler/webdrivers/`에 위치해주시면 됩니다.

만약, 이 프로젝트를 Linux(예시에서는 Ubuntu)에서 실행하기 위해서는 먼저 다음 명령어를 이용해서 webdriver를 다운로드 하셔야합니다.
```bash
$ sudo apt-get install chromium-chromedriver
```
그리고 Symbolic link를 이용해서 webdriver 파일의 링크 파일을 `[project_root]/commands/crawler/webdrivers/`에 생성합니다.
 ```bash
$ ln -s /usr/lib/chromium-browser/chromedriver [webdrivers_dir]
```

### Python packages
만약 Pipenv를 이용하신다면 다음 명령어를 이용하시면 됩니다.
```bash
$ pipenv install
```
virtualenv나 로컬 python에 설치하시는 경우 git root directory에서 다음을 실행해주시면 됩니다. 
```bash
$ pip install -r requirements.txt
```

### Python Version Compatibility
본 프로젝트는 Python 3.7을 기준으로 작성되었습니다.
2019년 2월 7일 기준으로 Python 3.7 버전에 대해 아래 세 package의 호환성 문제가 있습니다.

Python 3.7에서는 `async`와 `await`가 keyword로 등록되었습니다.
[What’s New In Python 3.7 | Changes in Python Behavior](https://docs.python.org/3/whatsnew/3.7.html#changes-in-python-behavior)

> async and await names are now reserved keywords.
Code using these names as identifiers will now raise a SyntaxError.
(Contributed by Jelle Zijlstra in [bpo-30406](https://bugs.python.org/issue30406).)

`discord`, `aiohttp`, `websockets` 세 package에서 호환성 문제가 발견되었으며,
에러가 발생하는 부분은 모두 아래와 같이 `asycio.async`를 호출하는 부분입니다.

```python
try:
    create_task = asyncio.ensure_future
except AttributeError:
    create_task = asyncio.async
```

이 방법은 `async`가 이제 keyword로 지정되어 사용이 불가능하므로, 에러가 발생하는 부분을 찾아서 아래와 같이 수정해주시면 됩니다.
```python
try:
    create_task = asyncio.ensure_future
except AttributeError:
    create_task = getattr(asyncio, 'async')
```

## Execution
Bot token과 함께 실행할 수 있습니다.
```bash
$ python looord_bot.py --token <token> [--dev|--debug]
```

`--token`은 `-t`로 줄여서 사용할 수 있습니다.

### Flags
이 프로그램에는 log level을 설정하기 위한 몇가지 flag들이 있습니다.

#### `--dev` flag
실행시 `--dev` flag를 준다면, 프로그램은 **foreground**로 실행되고,
**INFO** level의 로그를 stdout으로 보여줍니다. 로그 파일에는 **INFO** level의 로그가 기록됩니다.

#### `--debug` flag
실행시 `--debug` flag를 준다면, 프로그램은 **foreground**로 실행되고,
**DEBUG** level의 로그를 stdout으로 보여줍니다. 로그 파일에는 **INFO** level의 로그가 기록됩니다.

#### No Flag
실행시 flag를 지정하지 않으신다면, 프로그램은 **background**(daemon)로 실행되고,
stdout 없이 로그 파일에만 **INFO** level의 로그가 기록됩니다.

*daemonize는 아직 구현되지 않았습니다. background에서 실행을 원하시면 아래 명령어로 실행해주시기 바랍니다.*

```bash
$ nohup python looord_bot.py --token <token> [--dev|--debug] &
``` 
또는, pipenv를 이용해서

```bash
$ nohup pipenv run python looord_bot.py --token <token> [--dev|--debug] &
``` 