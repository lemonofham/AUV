#!/bin/bash
echo -n "Please enter the number of tests > "
read tests
for ((i = 0 ; i < tests ; i++ )); do
	echo -n "Please enter the number of players > "
	read players
	declare -a A
	declare -a B
	for ((i = 0 ; i < players ; i++ )); do
		A[i]=0
		B[i]=false
	done
	echo -n "Please enter the number of knights > "
	read x
	if [ "$x" -ne "0" ]; then
		echo -n "Please enter the numbers of players who are knights > "
	fi
	for ((i = 0 ; i < x ; i++ )); do
		read y
		A[y-1]=1
		B[y-1]=true
	done
	y=$(($n-$x-1))
	imposter=0
	if [ "$y" -ne "0" ]; then
		echo -n "Please enter the number of imposter > "
		read imposter
		A[imposter-1]=2
		B[imposter-1]=true
		for ((j = 0; j < players ; j++ )); do
			if [ !B[j] ]; then
				A[j]=0
			fi
		done
	else
		for ((j = 0; j < players ; j++ )); do
			if [ !B[j] ]; then
				A[j]=2
			fi
		done 
	fi
done 

