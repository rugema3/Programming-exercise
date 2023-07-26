#!/usr/bin/bash

# Using if Statements

echo "Please enter the first number: "
read num1

echo "Please enter the second number: "
read num2

if [ "$num1" -gt "$num2" ]
then
    echo "$num1 is greater than $num2"
elif [ "$num1" -lt "$num2" ]
then
    echo "$num1 is less than $num2"
elif [ "$num1" -eq "$num2" ]
then
    echo "$num1 equals $num2"
fi

