def commandDecoder(message):
    separator = '𓂸'
    command = message.split(separator)
    return command

def commandEncoder(command):
    separator = '𓂸'
    message = separator.join(command)
    return message
