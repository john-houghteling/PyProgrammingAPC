#! /usr/bin/bash

mkdir -p bandpass_john
# sending the output to hell
pushd bandpass_raw > /dev/null
all_files=($(ls))
num_dat=0
num_ASCII=0
num_asc=0
for f in $( ls )
do
    split=(${f//./ })
    name=${split[0]}
    type=${split[1]}

    # first get the file type counts
    # we assume that the only options are the ones already there
    if [[ $type == dat ]]; then
        num_dat=$((num_dat+1))
    elif [[ $type == ASCII ]]; then
        num_ASCII=$((num_ASCII+1))
    elif [[ $type == asc ]]; then
        num_asc=$((num_asc+1))
    else
        echo file type not in list $f
    fi

    # now find out if the file is energy or potons
    # -E allows extended regex, wit " ?" allowing for 
    # strings that countain 1 or 0 spaces after the "#"
    if grep -Eq "# ?energy" $f; then
        cp $f ../bandpass_john/${name}.energy.filt
    elif grep -q "photon" $f; then
        cp $f ../bandpass_john/${name}.photon.filt
    else
        echo no data type found: $f
        cp $f  ../bandpass_john/${name}.UNKOWN.filt
    fi

done

echo .dat: $num_dat
echo .ASCII: $num_ASCII
echo .asc: $num_asc

# I again don't want to see this output
popd > /dev/null
