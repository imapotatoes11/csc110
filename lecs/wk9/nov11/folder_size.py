import os
def folder_size(path: str) -> int:
    total = 0
    for name in os.listdir(path):
        full_name = os.path.join(path, name)
        if os.path.isfile(full_name):
            #total += os.path.getsize(full_name)
            total += 1
        else:
            total += folder_size(full_name)
    return total

os.system('tree | grep -c "└"')
print(folder_size("."))
