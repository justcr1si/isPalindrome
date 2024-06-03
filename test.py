from string import punctuation

def isPalindrome(sequence: str | int) -> bool:
    if not isinstance(sequence, str):
        sequence = str(sequence)
    else:
        sequence = sequence.lower().replace(' ', '')
        for letter in punctuation:
            if letter in sequence:
                sequence = sequence.replace(letter, '')

    return sequence == sequence[::-1]