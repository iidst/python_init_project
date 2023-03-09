import logging
import sys
import os
import  settings



def _get_logger():
    log = logging.getLogger('log')

    log.setLevel(logging.INFO)

    formatter = logging.Formatter('[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d] - %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')

    console_handle = logging.StreamHandler(sys.stdout)
    console_handle.setFormatter(formatter)

    file_handler = logging.FileHandler(os.path.join(settings.CURR_PATH,"logs", "run.log"))
    file_handler.setFormatter(formatter)

    log.addHandler(console_handle)
    log.addHandler(file_handler)
    return log


# 日志句柄
logger = _get_logger()
