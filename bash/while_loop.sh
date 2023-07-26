#!/usr/bin/bash

# Using loops in bash scripts.
i=1

while [[ $i -lt 20 ]]
do
	echo "$i"
	((i +=1)) # Increament i every time.
done
