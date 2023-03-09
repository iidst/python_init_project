import os

import os
from common.log import logger
import yaml
import settings

config = {}


def load_config():
    global config

    config_path = os.path.join(settings.CURR_PATH, "conf.yaml")

    if not os.path.exists(config_path):
        raise Exception('配置文件不存在，请在程序根目录根据创建conf.yaml文件')

    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.load(f.read(), Loader=yaml.FullLoader)

    logger.info("[INIT] load config: {}".format(config))



def conf():
    if not config:
        load_config()
    return config


if __name__ == '__main__':
    print(conf())
