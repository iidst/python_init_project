
from pkg.ex_bot.bot_factory import create_bot
from config.config import conf


class Ex_Run(object):

    def start(self):
        raise NotImplementedError

    def run_bot(self, ):
        return create_bot(conf().get("runBot")).run(context="context", a=1, b=2, c=3)
