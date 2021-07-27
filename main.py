import json

# from psutil import wait_procs
from process_collector import utils
from process_collector import process_operations


def loadConfig():
    confFile = "conf/config.json"
    with open(confFile) as f:
        conf = json.load(f)
        print(conf)


def main():
    loadConfig()
    utils.privilege_check()
    process_operations.create_info_file()


if __name__ == "__main__":
    main()
