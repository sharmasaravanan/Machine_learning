#!/bin/sh

# Author : Sharma
# Copyright (c) besoins.in
# Script follows here:

echo "Git push is started"

echo "How many files you are going to push?"
read n

if [ $n -gt 1 ]
then
    echo "Enter the files name as comma separated value: "
    read filenames
    for file in $(echo $filenames | tr "," "\n")
    do
        echo "Adding $file"
        git add $file
    done
else
    echo "Enter the file name to be added: "
    read filename
    echo "Adding $filename"
    git add $filename
fi


echo "git added successfully"

git commit -m "updated on $(date '+%Y/%m/%d')"
echo "Commited all the changes"

git push origin master
echo "All changes are pushed to Github"

echo "Have a great day"
