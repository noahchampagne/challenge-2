# Pickle Store

- Namespace: nchampag
- ID: pickled_store
- Type: custom
- Category: Reverse Engineering
- Points: 1
- Templatable: yes
- MaxUsers: 1

## Description

Pickled data isn't the safest storage

## Details

Connect to the program with netcat:

`$ nc {{server}} {{port}}`

The program's source code can be downloaded {{url_for("pickle_store.py", "here")}}.

## Hints

- Look at how the pickled data is stored
- Do we protect how the pickled data is loaded
- The cat command loves to read pickled data

## Solution Overview

Load pickle data that cats the flag.txt file

## Challenge Options

```yaml
cpus: 0.5
memory: 128m
pidslimit: 20
ulimits:
  - nofile=128:128
diskquota: 64m
init: true
```

## Learning Objective

Examining source code to identify functionality

## Tags

- python

## Attributes

- author: Noah Champagne
- organization: picoCTF
- event: picoCTF Problem Developer Training
