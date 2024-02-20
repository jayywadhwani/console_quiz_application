import sys,subprocess
def clear_screen():
    print()
    input("Press enter to exit...")
    operating_system = sys.platform
    if operating_system=="win32":
        subprocess.run("cls",shell=True)
    elif operating_system=="linux":
        subprocess.run("clear",shell=True)