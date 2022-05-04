from helpers.usage_message import usage_message
from helpers.get_location import get_location
import sys
from skills import agility, cooking, fletching, herbing, mining, summoning, woodcutting, smithing


def parse_args(argument):
    if argument in ('-f', '--fletching'):
        module = fletching.fletching
    elif argument in ("-w", "--woodcutting"):
        module = woodcutting.woodcutting
    elif argument in ("-b", "--smithing"):
        module = smithing.smithing
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
    elif argument in ('-p', '--position'):
        module = get_location
    else:
        usage_message()
        sys.exit(2)
    return module
