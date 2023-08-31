import os

def check_directory(name):
    if not os.path.exists(f'logs/{name}'):
        os.mkdir(f'logs/{name}')
        return False
    else:
        return True

def check_logs(name):
    
    dir_path = f'logs/{name}'
    i = 0

    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            i += 1
    
    return i

def get_logs(name):
    names = []
    for path in os.listdir(f'logs/{name}'):
        names.append(path)

    return names
