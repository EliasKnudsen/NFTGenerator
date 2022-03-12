#! /bin/bash
g++ main.cpp
echo "Compiled main.cpp"
./a.out > out.out
echo "Executed a.out"
python3 -V
python3 gen.py $1 $2
