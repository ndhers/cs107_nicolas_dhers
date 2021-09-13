#!/bin/bash

read -r -p "please enter file to commit: " file
git add $file
git status
read -r -p "Do you wish to continue?[Y/N] " answer
if [ $answer = "N" ]; then
	exit 1
else
	read -r -p "please enter commit message: " commit_message
fi
git commit -m "$commit_message"
git status
read -r -p "Do you wish to continue?[Y/N] " answer_2
if [ $answer_2 = "N" ]; then
        exit 1
else
	git push
fi


