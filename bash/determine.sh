#!/usr/bin/bash

# Determine whether a number is positive or negative

echo "Please enter the number: "
read num

if [ $num -lt 0 ]
then
	echo "$num is negative"

elif [ $num -gt 0 ]
then
	echo "$num is positive"
else
	echo "$num is zero"
fi
