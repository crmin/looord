from looord.commands import functions
from looord.commands.define import commands, prefix


def get_command_func(message_content):
    msg_chunks = [msg_chunk.lower() for msg_chunk in message_content.split()]
    for comm_func, comm_v in commands.items():
        for comm_msg in comm_v['message']:
            comm_msg = prefix + comm_msg
            try:
                msg_idx = msg_chunks.index(comm_msg)
            except ValueError:
                continue
            param_len = comm_v['parameters']
            parameters = msg_chunks[msg_idx + 1: msg_idx + param_len + 1]
            if len(parameters) < param_len:
                return {
                    'function': functions.bot_help,
                    'parameters': [],
                }
            return {
                'function': getattr(functions, comm_func),
                'parameters': parameters,
            }
    return {
        'function': None,
        'parameters': [],
    }


async def execute_command(client, message):
    if message.author.bot:
        return None
    comm_func = get_command_func(message.content)
    if comm_func['function'] is None:
        return None
    return await comm_func['function'](client, message, comm_func['parameters'])
