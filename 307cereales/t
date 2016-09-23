#! /bin/sh

if [ $# -ge 1 ] && [ $1 = "-d" ]
then
    ./307cereales 10 100 10 0 200 200 200 200 200 > test/local1
    cat test/local1
    echo "\n\033[31m=====================\033[0m"
    diff test/local1 test/result1
    echo "\033[31m=====================\033[0m\n"
else
    ./307cereales 10 100 10 0 200 200 200 200 200
fi

echo "\n\033[34m=====================\033[0m\n"

if [ $# -ge 1 ] && [ $1 = "-d" ]
then
    ./307cereales 45 41 27 63 198 259 257 231 312 > test/local2
    cat test/local2
    echo "\n\033[31m=====================\033[0m"
    diff test/local2 test/result2
    echo "\033[31m=====================\033[0m\n"
else
    ./307cereales 45 41 27 63 198 259 257 231 312
fi
