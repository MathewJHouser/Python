import os


def find(path, dir):
    for d in os.listdir(path):
        if d == dir:
            print(os.getcwd(dir))
        sub = os.listdir(d)
        if len(sub) == 0:
            continue
        path += "/" + dir
        find(path, dir)


try:
    find("./tree", "python")
except OSError:
    print("error")