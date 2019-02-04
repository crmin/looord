import discord


def get_online_members(client):
    members = [
        member
        for member in client.get_all_members()
        if member.status == discord.Status.online and
        not member.bot
    ]
    return members
