#!/bin/bash

# for loops
echo "For loop:"
for i in 1 2 3 4 5; do
    echo "Number: $i"
done

# while loops
echo "While loop:"
count=1
while [ $count -le 3 ]; do
    echo "Count: $count"
    count=$((count + 1))
done