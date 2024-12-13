

#User-Define Exception
class InvalidRollNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg    #msg = "roll number should not be negative"


class InvalidNameError(Exception):
    def __init__(self, msg):
        self.msg = msg


class InvalidPercentageError(Exception):
    def __init__(self, msg):
        self.msg = msg
