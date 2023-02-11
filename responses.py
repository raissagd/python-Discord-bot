import random

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return "Hey there! How you're doing?"

    if message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return '`This is a help message that will soon be modified.`'

    return "I'm sorry, I don't know that command yet. Try typing !help."