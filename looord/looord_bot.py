import argparse
from datetime import datetime
import hashlib
import logging

import discord

from looord.commands.commands import execute_command


client = discord.Client()


@client.event
async def on_ready():
    logger.info('Bot loaded')


@client.event
async def on_message(message):
    now_time = datetime.now().strftime('%Y%m%d%H%M%S%f')
    channel_id = str(message.channel.id)
    author_id = str(message.author.id)
    msg_content = message.content.replace('\n', '\\n')
    msg_id = hashlib.md5('{}{}{}{}'.format(now_time, channel_id, author_id, msg_content).encode()).hexdigest()
    logger.info('<{msg_id}> Message received: {author}#{code} ({author_id}) {msg}'.format(
        msg_id=msg_id,
        author=message.author.name,
        code=message.author.discriminator,
        author_id=author_id,
        msg=msg_content
    ))
    await execute_command(client, message, logger, msg_id)
    logger.info('<{msg_id}> process done'.format(msg_id=msg_id))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--token', type=str, help='discord bot token')
    parser.add_argument('--dev', action="store_true", help='If exist this flag, bot run on foreground, not daemon')
    args = parser.parse_args()

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    fmtr = logging.Formatter('[%(levelname)s] %(asctime)s %(message)s')

    file_hdlr = logging.FileHandler('./looord_bot.log')
    file_hdlr.setLevel(logging.INFO)
    file_hdlr.setFormatter(fmtr)
    logger.addHandler(file_hdlr)

    if args.dev:
        stream_hdlr = logging.StreamHandler()
        stream_hdlr.setLevel(logging.INFO)
        stream_hdlr.setFormatter(fmtr)
        logger.addHandler(stream_hdlr)

    logger.info('Program Executed')
    client.run(args.token)
