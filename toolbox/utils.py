from datetime import datetime


def msg_formatter(s):
    return f'[{datetime.now().isoformat()}]: {s}'
