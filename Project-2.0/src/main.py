from src.misc import Misc
from src.testengine import testengine


def main():
    misc = Misc()
    the= misc.getThe()
    help = misc.getHelp()

    testEngine= testengine(the)
    testEngine.concat(help)
    # testEngine.zitlerRanks()
    testEngine.runtests()


if __name__ == "__main__":
    main()