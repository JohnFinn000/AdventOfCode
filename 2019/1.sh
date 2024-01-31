#!/bin/bash 

total= 0
while read line; do
  echo "$(($line / 3 - 2))";
done < 1_input.txt
echo ${total}
