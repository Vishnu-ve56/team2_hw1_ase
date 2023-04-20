#!/bin/bash

rm -r ../out/*
cd ..
python -m src.main -o 1
python -m src.main -o 2
python -m src.main -o 3
python -m src.main -o 4
python -m src.main -o 2 -m 0.35
python -m src.main -o 2 -m 0.22
python -m src.main -o 2 -m 0.62
python -m src.main -o 2 -m 0.78
python -m src.main -o 2 -m 0.92