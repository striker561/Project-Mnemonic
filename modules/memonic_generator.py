import itertools
import random
from typing import Dict, List, Union


def generate_phrase_of_word_count(
    phrase: Dict,
    count: int,
    return_string: bool = False,
    return_string_suffix: str = "\n",
) -> Union[str, Dict]:
    print(f"Generating a {count}-word Phrase Word From {len(phrase)} words")

    generator = list(itertools.permutations(phrase, count))

    if not return_string:
        return generator

    return_string = ""

    for generated in generator:
        return_string += " ".join(generated) + return_string_suffix

    return return_string

def get_random_phrases(
    phrase_list: List[str],
    num_phrases: int,
    return_string: bool = False,
) -> Union[List[str], str]:
    if num_phrases > len(phrase_list):
        raise ValueError("Number of requested phrases exceeds available phrases")
    
    random_gen = random.sample(phrase_list, num_phrases)
    
    if not return_string:
        return random_gen
        
    return ' '.join(random_gen)
    