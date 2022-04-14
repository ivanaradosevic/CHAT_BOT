import json
from typing import List

class Intent:
    tag: str
    patterns: List[str]
    responses: List[str]
    context: List[str]

def load_intents() -> List[Intent]:
    with open("data/intents.json", "r", encoding="utf-8") as f:
        intents_json = json.load(f)

    intents: List[Intent] = []

    for intent_dict in intents_json["intents"]:
        intent = Intent()
        intent.tag = intent_dict["tag"]
        intent.patterns = intent_dict["patterns"]
        intent.responses = intent_dict["responses"]

        intents.append(intent)
    
    return intents

def get_lables(intents: List[Intent]):
    training_labels = []

    for intent in intents:
        if intent.tag not in training_labels:
            training_labels.append(intent.tag)
        
    return training_labels