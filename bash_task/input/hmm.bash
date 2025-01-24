#!/bin/bash
g++ a.cpp -o a.out
./a.out < ./input.txt > ./output.txt
echo "" >> ./output.txt
wc -l < ./output.txt
while IFS="" read -r line; do
	if [ "   10" = "$line" ]; then
		echo "YES"
	fi
done < ./output.txt
