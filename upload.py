from pantry_wrapper import get_contents, append_basket
import os, dotenv
from typing import Union

dotenv.load_dotenv() 

PANTRY_ID = os.environ.get("PANTRY_ID")

def get() -> Union[str, dict]:
    contents = get_contents(str(PANTRY_ID), "metadata", "body")
    return contents

get() 

def append(data: dict):
    if PANTRY_ID is None:
        raise Exception("PANTRY_ID does not exist as an enviroment variable!")
    current = get()
    if type(current) != dict:
        raise Exception("Failed to get data from Pantry, did not return a dict as expected! This might be caused by an error.")
    keys: list[str] = list(current.keys())

    if len(keys) > 0 and keys[-1].isnumeric():
        new_key = int(keys[-1]) + 1 
    else:
        new_key = 1 

    current[str(new_key)] = data


    append_basket(PANTRY_ID, "metadata", current)



def delete(id: int):
    if PANTRY_ID is None:
        return
    current = get() 
    if type(current) != dict:
        return 

    del current[str(id)] 
    append_basket(PANTRY_ID, "metadata", current)

""" append({
    "title": "Fraud and Toji", 
    "download": "https://files.catbox.moe/97uh1e.mp4", 
    "tags": ["gojo", "toji", "jjk", "jujutsu", "kaisen", "anime"], 
    "creator": None, 
    "duration": "14s", 
    "source": None
}) """


