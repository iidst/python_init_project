from pkg.ex_bot.bot import Bot


class Bot2(Bot):
    def __init__(self):
        self.name = "bot2"

    def run(self, context=None, *args, **kwargs):
        print(self.name, "Starting...")
        print("->context".format(context))
        print("->args:{}".format(args, ))
        print("=>kwargs:{}".format(kwargs, ))

