from helpers.usage_message import usage_message
import sys
from skills import agility, cooking, fletching, herbing, mining, summoning, woodcutting


def parse_args(argument):
    module = None
    if argument in ('-f', '--fletching'):
        module = fletching.fletching
    elif argument in ("-w", "--woodcutting"):
        module = woodcutting.woodcutting
    elif argument in ('-s', '--summoning'):
        module = summoning.summoning
    elif argument in ('-c', '--cooking'):
        module = cooking.cooking
    elif argument in ('-m', '--mining'):
        module = mining.mining
    elif argument in ('-h', '--herbing'):
        module = herbing.herbing
    elif argument in ('-a', '--agility'):
        module = agility.agility
    else:
        usage_message()
        sys.exit(2)
    return module
