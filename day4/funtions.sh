#!/bin/bash

# function
greet() {
    echo "Hello, $1!"
}

# parameterized function
add() {
    result=$(($1 + $2))
    echo "Sum: $result"
}

# Call functions
greet "Adir"
greet "DevTest"
add 5 3