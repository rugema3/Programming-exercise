#!/usr/bin/bash

# Using for loops in bash scripting.

for i in {20..1000} # iterate from 20 to 1000
do
	echo $i # Output the numbers as you iterate
done
echo ""

for word in ALX havard stanford ALU Harding # Iterate over words
do
	echo $word
done
