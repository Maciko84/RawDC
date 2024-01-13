from rawdcparser import Node
from texttoemoji import ConvertToEmoji
import random

@Node("PLAIN_TEXT")
def NODE_PLAIN_TEXT(content: list[str]):
    return '\n'.join(content) + '\n'

@Node("EMOJI_TEXT")
def NODE_EMOJI_TEXT(content: list[str]):
    return ConvertToEmoji('\n'.join(content)) + "\n"

@Node("USER_MENTION")
def NODE_USER_MENTION(content: list[str]):
    msg = []
    for item in content:
        msg.append("<@" + item + ">\n")
    return ''.join(msg)

@Node("ROLE_MENTION")
def NODE_ROLE_MENTION(content: list[str]):
    msg = []
    for item in content:
        msg.append("<@&" + item + ">\n")
    return ''.join(msg)

@Node("CHANNEL")
def NODE_CHANNEL(content: list[str]):
    msg = []
    for item in content:
        msg.append("<#" + item + ">\n")
    return ''.join(msg)

@Node("TITLE")
def NODE_TITLE(content: list[str]):
    msg = []
    for item in content:
        msg.append("# " + item + "\n")
    return ''.join(msg)

@Node("CLAP_MESSAGE")
def NODE_CLAP_MESSAGE(content: list[str]):
    result = []
    for line in content:
        new_line = ''
        for char in line:
            if char == ' ':
                new_line += ' :clap: '
            elif random.random() < 0.1:  # 10% chance to change letter to :clap:
                new_line += ' :clap: '
            else:
                new_line += char.upper() if random.choice([True, False]) else char.lower()
        result.append(new_line)
    return '\n'.join(result) + '\n'
