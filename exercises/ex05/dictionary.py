"""EX05-Dictionary Utils.""" 

__author__ = "730553436"
"""Codes for Dictionaries within this module."""


def invert(info1: dict[str, str]) -> dict[str, str]:
    """Invert the keys and the values to become the opposite."""
    info2: dict[str, str] = {}
    for key in info1:
        if info1[key] in info2:
            raise KeyError("cannot have duplicate keys")
        info2[info1[key]] = key
    return info2


def favorite_color(colors: dict[str, str]) -> str:
    """Output the most frequent color."""
    count: dict[str, int] = {}
    for key in colors:
        if colors[key] in count:
            count[colors[key]] = count[colors[key]] + 1
        else:
            count[colors[key]] = 1
    
    color = ''
    maximum = 0
    for key in count:
        if count[key] > maximum:
            color = key
            maximum = count[key]
    
    return color


def count(values1: list[str]) -> dict[str, int]:
    """Return the correct dictionary value according to key."""
    counter: dict[str, int] = {}
    for value in values1:
        if value in counter:
            counter[value] = counter[value] + 1
        else:
            counter[value] = 1
    return counter


def alphabetizer(words1: list[str]) -> dict[str, list[str]]:
    """Return the correct lowercase letter according to the values."""
    result: dict[str, list[str]] = {}
    for word in words1:
        letter: str = word[0]
        if letter in result:
            result[letter].append(word)
        else:
            result[letter] = [word]
    
    return result


def update_attendance(existingdict: dict[str, list[str]], day: str, student: str) -> None:
    """Print the students that attended a specific day."""
    if day in existingdict:
        if student not in existingdict[day]:
            existingdict[day].append(student)
    else:
        existingdict[day] = [student]