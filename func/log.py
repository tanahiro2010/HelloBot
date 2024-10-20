import time


class Logger:
    def __init__(self):
        import time
        # 代表的な色
        self.INFO_BLUE = '\033[94m'
        self.INFO_GREEN = '\033[92m'
        self.WARN = '\033[93m'
        self.ERR = '\033[91m'

        # フォントスタイル
        self.MARKER = '\033[7m'
        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'

        # 末尾制御
        self._END = '\033[0m'
        pass

    def error(self, message) -> None:
        localtime = time.localtime()
        print('{}[Error time:{}]{} {}'.format(self.ERR, '{}-{}/{}-{}:{}:{}'.format(localtime.tm_year, localtime.tm_mon, localtime.tm_mday, localtime.tm_hour, localtime.tm_min, localtime.tm_sec), self._END, message))
        return None

    def success(self, message) -> None:
        localtime = time.localtime()
        print('{}[Success time:{}]{} {}'.format(self.INFO_GREEN, '{}-{}/{}-{}:{}:{}'.format(localtime.tm_year, localtime.tm_mon, localtime.tm_mday, localtime.tm_hour, localtime.tm_min, localtime.tm_sec), self._END, message))
        return None

    def warn(self, message) -> None:
        localtime = time.localtime()
        print('{}[Warnig time:{}]{} {}'.format(self.WARN, '{}-{}/{}-{}:{}:{}'.format(localtime.tm_year, localtime.tm_mon, localtime.tm_mday, localtime.tm_hour, localtime.tm_min, localtime.tm_sec), self._END, message))
        return None

    def log(self, message) -> None:
        localtime = time.localtime()
        print('{}[Log time:{}]{} {}'.format(self.INFO_BLUE, '{}-{}/{}-{}:{}:{}'.format(localtime.tm_year, localtime.tm_mon, localtime.tm_mday, localtime.tm_hour, localtime.tm_min, localtime.tm_sec), self._END, message))
        return None