from config.config import conf
from cmds.ex_run.ex_run_factory import create_run
from common.log import logger

if __name__ == '__main__':

    try:
        r = create_run(conf().get("run"))
        r.start()
    except Exception as e:
        logger.error("faied:{}".format(str(e)))
        raise Exception(str(e))
