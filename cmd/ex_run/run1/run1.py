from cmd.ex_run.ex_run import Ex_Run


class Run1(Ex_Run):

    def start(self):
        print("Run1 Starting...")
        super().run_bot()
