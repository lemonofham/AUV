#!/bin/bash
IFS=''
echo -n "Please enter the input target folder > "
read input_folder
echo -n "Please enter the output folder > "
read output_folder
ls -1 "./$input_folder" > temp.txt
check=0
while read -r -u9 line; do
	if [ "${line: -4}" = ".cpp" ]; then
		length=${#line}
		z=$(($length-4))
		file_name=${line:0:$z}
		ls -1 "./$output_folder" > tmp.txt
		checker=0
		while read -r line1; do
			if [ "$line1" = "$file_name.out" ]; then
				checker=1
			fi
		done < tmp.txt 
		rm tmp.txt
		if [ "$checker" = "1" ]; then
			rm "./$output_folder/$file_name.out"
		fi
		g++ "./$input_folder/$line" -o "./$output_folder/$file_name.out"
		ls -1 "./$output_folder" > tmp.txt
        	checker=0
        	while read -r line1; do
                	if [ "$line1" = "$file_name.out" ]; then
                        	checker=1
                	fi
        	done < tmp.txt
		rm tmp.txt
		if [ "$checker" = "1" ]; then
			correct=1	
			echo -n "Please enter full path of test cases file for input file $line > "
			read input_file_path	
			echo -n "Please enter correct (expected) output given test cases > "
                        read correct_output	
			out="_output"
			timeout 5 "./$output_folder/$file_name.out" < "$input_file_path" > "./$file_name$out.txt"
			echo "" >> "./$file_name$out.txt"
			read lines <<< $(wc -l < "./$file_name$out.txt")	
			while read -r line1; do
				lines="$(echo -e "${lines}" | tr -d '[:space:]')"		
				if [ "$lines" != "1" ]; then	
					correct=0
				fi
				if [ "$line1" != "$correct_output" ]; then
					correct=0
				fi
			done < "./$file_name$out.txt"
			if [ "$correct" = "1" ]; then
				echo "YES"
			else
				echo "NO"
			fi
		fi
	fi
done 9< temp.txt
rm temp.txt
