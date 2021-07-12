from getopt import getopt, GetoptError
import sys
import time
from helpers.usage_message import usage_message
from helpers.parse_args import parse_args

def main(inputArg):
    times_to_run = 1  # set times to run
    times_ran = 0  # times the program has run --this should NOT need to be changed--
    time.sleep(1.5)  # time to get back into your game window
    try:
        opts, args = getopt(inputArg, "fwscmha", ["fletching",
                                            "woodcutting",
                                            "summoning",
                                            "cooking",
                                            "mining,",
                                            "herbing",
                                            "agility"])
    except GetoptError as err:
        print(err)
        usage_message()
        sys.exit(2)
    for o, a in opts:
        skill_to_train = parse_args(o)
        while times_to_run > times_ran:
            times_ran += 1
            print("Run number: ", times_ran)
            skill_to_train()


if __name__ == "__main__":
    main(sys.argv[1:])
