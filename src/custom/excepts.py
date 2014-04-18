# Exceptions


class BreakNestedLoop(Exception):
    """
    Raise in a try-except to easily exit a Nested Loop
    """
    pass


class TimeoutError(Exception):
    """
    Raise in a try-except with Timeout()
    """
    pass
