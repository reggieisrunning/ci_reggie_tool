import sys
sys.path.append("..")
import logging
import os
from logging.handlers import TimedRotatingFileHandler


LOG_LEVEL = "INFO"

class LoggerWrapper:

    def __init__(self):
        self.logger = self._gen_logger()

    @staticmethod
    def _get_path():
        path = "../logs/"
        if not os.path.exists(path):
            os.makedirs(path)

        return path

    def _gen_logger(self, log_name="ci_reggie_tool"):
        base_logger = logging.getLogger(log_name)
        base_logger.setLevel(LOG_LEVEL)
        pass
        log_file = "{}/{}.log".format(self._get_path(), log_name)
        ch = TimedRotatingFileHandler(log_file, when='D', encoding="utf-8")
        ch.setLevel(LOG_LEVEL)
        formatter = logging.Formatter('[%(asctime)s][%(levelname)s][%(process)d]%(funcName)s: %(message)s')
        ch.setFormatter(formatter)
        base_logger.addHandler(ch)
        base_logger.propagate = 0
        print("dddd")
        return base_logger

logger = LoggerWrapper().logger
