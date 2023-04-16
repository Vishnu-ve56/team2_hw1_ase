
constants = {
    'help': str("script.lua : an example script with help text and a test suite\n"
                    "(c)2022, Tim Menzies <timm@ieee.org>, BSD-2\n" 
                    "USAGE:   script.lua  [OPTIONS] [-g ACTION]\n"
                    "OPTIONS:\n"
                    " -b  --bins    initial number of bins       = 16\n"
                    " -c  --cliffs  cliff's delta threshold      = .147\n"
                    " -f  --file    data file                    = ../data/china.csv\n"
                    " -F  --Far     distance to distant          = .95\n"
                    " -g  --go      start-up action              = nothing\n"
                    " -h  --help    show help                    = false\n"
                    " -H  --Halves  search space for clustering  = 512\n"
                    " -m  --min     size of smallest cluster     = .5\n"
                    " -M  --Max     numbers                      = 512\n"
                    " -p  --p       dist coefficient             = 2\n"
                    " -r  --rest    how many of rest to sample   = 4\n"
                    " -R  --Reuse   child splits reuse a parent pole = true\n"
                    " -B  --bootstrap bootstrap                   = 512\n"
                    " -C  --conf      conf                        = 0.05\n"
                    " -s  --seed    random number seed           = 937162211\n"
                    " -n  --n_iter  no of iterations             = 3\n"
                    "ACTIONS:\n"
    )
}

def getConstants(key):
    return constants[key]
