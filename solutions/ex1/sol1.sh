#! /usr/bin/bash

mkdir -p bandpass_john
cd bandpass_raw
all_files=($(ls))
#echo ${all_files[@]}
num_dat=0
num_ASCII=0
num_asc=0
for f in ${all_files[@]}
do
split=(${f//./ })
name=${split[0]}
type=${split[1]}

# first get the file type counts
if [[ $type == dat ]]
then
num_dat=$((num_dat+1))
elif [[ $type == ASCII ]]
then
num_ASCII=$((num_ASCII+1))
elif [[ $type == asc ]]
then
num_asc=$((num_asc+1))
else
echo oops
fi



done
echo .dat: $num_dat
echo .ASCII: $num_ASCII
echo .asc: $num_asc

popd
