import argparse

import discord

from looord.commands.commands import execute_command


parser = argparse.ArgumentParser()
parser.add_argument('--token', type=str, help='discord bot token')
args = parser.parse_args()

client = discord.Client()


@client.event
async def on_ready():
    pass


@client.event
async def on_message(message):
    await execute_command(client, message)


if __name__ == '__main__':
    client.close()
    client.run(args.token)
