#!/bin/bash

# rm -r ../out/*
cd ..
# python -m src.main -o 1
# python -m src.main -o 2
# python -m src.main -o 3
# python -m src.main -o 4
# python -m src.main -o 2 -m 0.35
# python -m src.main -o 2 -m 0.22
# python -m src.main -o 2 -m 0.62
# python -m src.main -o 2 -m 0.78
# python -m src.main -o 2 -m 0.92

# python -m src.main -o 1 -f ../data/auto2.csv
# python -m src.main -o 2 -f ../data/auto2.csv
# python -m src.main -o 1 -f ../data/china.csv
# python -m src.main -o 2 -f ../data/china.csv
# python -m src.main -o 1 -f ../data/pom.csv
# python -m src.main -o 2 -f ../data/pom.csv
# python -m src.main -o 1 -f ../data/nasa93dem.csv
# python -m src.main -o 2 -f ../data/nasa93dem.csv
# python -m src.main -o 1 -f ../data/coc1000.csv
# python -m src.main -o 2 -f ../data/coc1000.csv
# python -m src.main -o 1 -f ../data/coc10000.csv
# python -m src.main -o 2 -f ../data/coc10000.csv

python -m src.main -o 1 -f ../data/SSM.csv
python -m src.main -o 2 -f ../data/SSM.csv
python -m src.main -o 1 -f ../data/SSN.csv
python -m src.main -o 2 -f ../data/SSN.csv
python -m src.main -o 1 -f ../data/healthCloseIsses12mths0001-hard.csv
python -m src.main -o 2 -f ../data/healthCloseIsses12mths0001-hard.csv
python -m src.main -o 1 -f ../data/healthCloseIsses12mths0011-easy.csv
python -m src.main -o 2 -f ../data/healthCloseIsses12mths0011-easy.csv