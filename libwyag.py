import argparse
import json
import logging
import os

from hashlib import sha256
from pathlib import Path

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def read_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("command")
    args = parser.parse_args()
    return args


def cmd_init():
    execution_path = Path(os.getcwd())
    if not ( execution_path/ "_tracker.json").exists():
        logger.info("Initializing repo and tracking files")

        hash_dict = {}
        with open(execution_path / "_tracker.json", "w") as f:
            json.dump(hash_dict, f)

        logger.info("Created tracker file")

        Path(execution_path / "__backup").mkdir(parents=True, exist_ok=True)

        logger.info(f"Initialized repo")

    else:
        logger.info(f"Repo already initialized")


def cmd_status():
    pass



def main():
    args = read_args()
    command = args.command

    match command:
        case "init":
            cmd_init()
        case "status":
            pass
        case _:
            print("No command specified")

