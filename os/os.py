import os

program = "python"
arguments = ["hello.py"]

args_list = list(arguments)

run = str(program) + str(args_list)
print(os.execvp(run))