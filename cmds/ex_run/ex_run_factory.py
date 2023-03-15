

def create_run(run_type):

    if run_type == '1':
        from cmds.ex_run.run1.run1 import Run1
        return Run1()

    raise




