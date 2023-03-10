import logging
import sys
import os
import settings


def _get_logger():
    # 获取log对象
    log = logging.getLogger('log')
    # 设置级别
    log.setLevel(logging.INFO)

    # 格式化
    formatter = logging.Formatter('[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d] - %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')

    # 控制台handle
    console_handle = logging.StreamHandler(sys.stdout)
    console_handle.setFormatter(formatter)

    # 文件handler
    if not os.path.isdir("logs"):
        os.makedirs("logs")
    file_handler = logging.FileHandler(os.path.join(settings.CURR_PATH, "logs", "run.log"))
    file_handler.setFormatter(formatter)

    log.addHandler(console_handle)
    log.addHandler(file_handler)
    return log


# 日志句柄
logger = _get_logger()
