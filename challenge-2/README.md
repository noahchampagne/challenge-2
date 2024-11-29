# Pickle Store CTF README

## Pre-requisites

1. Basic understanding of pickled data in python
2. Understand the use of netcat

## Overview

In my challenge, you are tasked with storing and loading pickled data in
any way that allows for the user to read the flag.txt file. The pickle
vault stores pickled data and will then load this data. The flag can be
read in any way that the user finds possible using the exposed vulnerabilites.

## Walkthrough

### File Listing

1. pickle_store.py: The main Python script for the challenge which allows the
   user to store and load pickled data. Data is stored in base64 for easy
   plaintext input into the file. The pickled data is then loaded from
   the auth_dat.pkl file.
3. flag.txt: The file containing the flag, which is only revealed upon
   successful login as the admin user.

## Conclusion

The main complexity in this challenge lies in the user's understanding of
pickled data specifically related to how it is loaded. The program has some
misdirection encouraging the user to figure out how to input some authorized
user data. However, this is completely unnecessary. The user can instead input
a class which imports OS and runs the cat command on flag.txt.
