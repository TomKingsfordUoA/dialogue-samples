## Introduction 

The multiwoz dataset is used. Consists of a collection of human-human written conversations.
https://github.com/budzianowski/multiwoz

The goal of this project is to provide a sample of realistic phrases of dialogue for testing of a co-speech gesture
system.

## Getting Started
```
./download_multiwoz.sh
md5sum -c MultiWOZ_2.1.zip.md5sum
unzip *.zip

python3 -m venv venv
source venv/bin/activate

python process.py
```

The output is a random sample of phrases from the dataset.
