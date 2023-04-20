#!/bin/bash

rm -r ../out/*
cd ..
python -m src.main -o 1
python -m src.main -o 2
