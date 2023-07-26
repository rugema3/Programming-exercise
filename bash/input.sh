#!/usr/bin/bash

# reading user input and dealing with it accordingly.
read -p "Please enter the first number: " num1
read -p "Please enter the second number: " num2
var=$((num1 + num2))

echo "the sum of $num1 and $num2 is: $var"
