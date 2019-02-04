# Looord: R6S Discord bot

Starts with bot token
```bash
$ python looord_bot.py --token <token> [--dev|--debug]
```

## Flags
This program has some flags which set log level

### `--dev` flag
If exists `--dev` flag in command line, program run on **foreground** and
display **INFO** level log as stdout and write **INFO** level log as file.

### `--debug` flag
If exists `--debug` flag in command line, program run on **foreground** and
display **DEBUG** level log as stdout and write **INFO** level log as file.

### No Flag
If there is not any flag in command line, program run on **background**(daemon) and write **INFO** level log as file only.

*daemonize not implemented yet* 