import os

# get path

pwd = os.getcwd()
print(pwd)


# cambiar directorio

def current_path():
    print("Current working directory before")
    print(os.getcwd())
    print()


current_path()
os.chdir('../')
current_path()
