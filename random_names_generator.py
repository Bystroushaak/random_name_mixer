#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Imports =====================================================================
import random


# Variables ===================================================================
VOWELS = list("aeiouáéíóúůyý")


# Functions & classes =========================================================
def get_words(filename):
    with open(filename) as f:
        return f.read().splitlines()


def split_word(word):
    size = len(word)

    def pick_random_part(word, j, k):
        if random.randint(0, 2) != 0:
            j = min([j, k])
            k = max([j, k])

        return word[j:k]

    splits = [
        pick_random_part(
            word,
            random.randint(0, size),
            random.randint(0, size)
        )
        for _ in range(20)
    ]
    splits = [x for x in splits if x and len(x) <= 4]

    return splits


def count_vowels(word):
    return sum(1 for vowel in VOWELS if vowel in word)


def prioritize_vowels(splits):
    return [
        x for x in splits
        if count_vowels(x) > 0 or random.choice((True, False))
    ]


def repeat_penalty(word):
    old = ""
    score = 0
    penalty = 0
    for char in list(word) + [""]:
        if char == old and char in VOWELS:
            penalty += 1
        else:
            score += penalty ** 3
            penalty = 0

        old = char

    score += penalty ** 3
    return score


def mix(words, num):
    splits = [
        prioritize_vowels(split_word(word))
        for word in words
    ]
    splits = sum(splits, [])

    candidates = list(set(
        "".join(
            random.choice(splits)
            for j in range(random.randint(0, 4))
        )
        for _ in range(num * 20)
    ))

    smallest = min(words, key=lambda x: len(x))
    longest = max(words, key=lambda x: len(x))

    def is_bad(word):
        if len(word) < len(smallest):
            return True

        if len(word) > len(longest * 2):
            return True

        if count_vowels(word) > (len(word) / 2) + 1:
            return True

        if repeat_penalty(word) > 2:
            return True

        return False

    candidates = [
        x for x in candidates
        if not is_bad(x)
    ]

    return [
        random.choice(candidates)
        for _ in range(num)
    ]


# Main program ================================================================
if __name__ == '__main__':
    import sys
    import os.path
    import argparse

    parser = argparse.ArgumentParser(
        description="Mix random names from word seeds."
    )
    parser.add_argument(
        "SEED_FILE",
        help="File with list of seed words.",
    )
    args = parser.parse_args()

    if not os.path.exists(args.SEED_FILE):
        print("`%s` not found!" % args.SEED_FILE, file=sys.stderr)
        sys.exit(1)

    words = get_words(args.SEED_FILE)

    for x in mix(words, 20):
        print(x)
