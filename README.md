# Looord: R6S Discord bot

## Installation

### Selenium web driver
This project selenium web driver (using headless chrome) for `$history` command

If mac or windows, you can download chrome webdriver [here](http://chromedriver.chromium.org/downloads)
and locate driver file to `[project_root]/commands/crawler/webdrivers/`

If you run this project in linux(example for ubuntu server), first download webdriver using:
```bash
$ sudo apt-get install chromium-chromedriver
```
and create link file to `[project_root]/commands/crawler/webdrivers/` using:
```bash
$ ln -s /usr/lib/chromium-browser/chromedriver [webdrivers_dir]
```

### Python packages
If you use pipenv, run install command using:
```bash
$ pipenv install
```
or, if use virtualenv or install to local, run next command in git root directory
```bash
$ pip install -r requirements.txt
```

## Execute
Starts with bot token
```bash
$ python looord_bot.py --token <token> [--dev|--debug]
```

### Flags
This program has some flags which set log level

#### `--dev` flag
If exists `--dev` flag in command line, program run on **foreground** and
display **INFO** level log as stdout and write **INFO** level log as file.

#### `--debug` flag
If exists `--debug` flag in command line, program run on **foreground** and
display **DEBUG** level log as stdout and write **INFO** level log as file.

#### No Flag
If there is not any flag in command line, program run on **background**(daemon) and write **INFO** level log as file only.

*daemonize not implemented yet* 