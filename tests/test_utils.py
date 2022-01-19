from toolbox import msg_formatter


def test_msg_formatter():
    assert '[toolbox]: test' in msg_formatter('test')
