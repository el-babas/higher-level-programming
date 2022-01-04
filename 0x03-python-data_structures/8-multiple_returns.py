#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)

    new_tuple = (0, None) if length == 0 else (length, sentence[0])
    return (new_tuple)
