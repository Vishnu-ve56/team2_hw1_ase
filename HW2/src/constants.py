
constants = {
    'help': str("script.lua : an example script with help text and a test suite\n"
                    "(c)2022, Tim Menzies <timm@ieee.org>, BSD-2\n" 
                    "USAGE:   script.lua  [OPTIONS] [-g ACTION]\n"
                    "OPTIONS:\n"
                    " -d  --dump  on crash, dump stack = false\n"
                    " -f  --file  name of file         = ../data/auto93.csv\n"
                    " -g  --go    start-up action      = data\n"
                    " -h  --help  show help            = false\n"
                    " -s  --seed  random number seed   = 937162211\n"
                    "ACTIONS:\n"
    )
}

def getConstants(key):
    return constants[key]
