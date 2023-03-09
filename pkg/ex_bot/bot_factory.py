

def create_bot(bot_type):

    if bot_type == '1':
        from pkg.ex_bot.bot1.bot1 import Bot1
        return Bot1()

    elif bot_type == '2':
        from pkg.ex_bot.bot2.bot2 import Bot2
        return Bot2()

    raise
