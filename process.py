import json
import random
from pprint import pprint

if __name__ == "__main__":
    with open("MultiWOZ_2.1/data.json") as f:
        raw_dialogue = json.load(f)

    filenames = list(raw_dialogue.keys())
    files = [raw_dialogue[filename] for filename in filenames]
    dialogue = [row['text'] for file in files for row in file['log']]

    random.seed(42)
    pprint(random.sample(dialogue, 10))
