from pkg.ex_bot.bot import Bot


class Bot1(Bot):
    def __init__(self):
        self.name = "bot1"

    def run(self, context=None, *args, **kwargs):
        print(self.name,"Starting...")
        print("context".format(context))
        print("args:{}".format(args, ))
        print("kwargs:{}".format(kwargs, ))
