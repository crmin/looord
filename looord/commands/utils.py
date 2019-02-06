import discord


def get_online_members(channel):
    members = [
        member
        for member in channel.server.members
        if member.status == discord.Status.online and
        not member.bot
    ]
    return members
