
from src.misc import Misc
from src.testengine import testengine
def main():
    misc = Misc()
    the= misc.getThe()
    help = misc.getHelp()

    testEngine= testengine()
    testEngine.concat(help)
    testEngine.runtests(the)


    



if __name__ == "__main__":
    main()