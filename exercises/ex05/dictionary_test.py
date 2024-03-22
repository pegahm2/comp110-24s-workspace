"""EX06 - Dict Unit Tests.""" 

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance

__author__ = "730553436"
"""Checks the functions using edge and use cases."""


def test_invert_use1() -> dict[str, str]:
    """Use test 1: function should return nothing but invert correct key and value in the dictionary."""
    info1: dict[str, str] = {"hello": "bye", "good": "bad", "happy": "sad"}
    info2: dict[str, str] = invert(info1)
    valid_info2: dict[str, str] = {"bye": "hello", "bad": "good", "sad": "happy"} 

    assert info2 == valid_info2


def test_invert_use2() -> dict[str, str]: 
    """Use test 2: function should return nothing but invert correct key and value in the dictionary."""
    info1: dict[str, str] = {"fun": "boring", "mad": "funny"}
    info2: dict[str, str] = invert(invert(invert(info1)))
    valid_info2: dict[str, str] = {"boring": "fun", "funny": "mad"}

    assert info2 == valid_info2


def test_invert_edge() -> dict[str, str]: 
    """Edge Test: function should return nothing and invert nothing because empty."""
    info1: dict[str, str] = {}
    info2: dict[str, str] = invert(info1)
    valid_info2: dict[str, str] = {}

    assert info2 == valid_info2


def test_favorite_color_use1() -> str:
    """Use test 1: function should return nothing but invert correct key and value in the dictionary."""
    colors: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(colors) == "blue"


def test_favorite_color_use2() -> str:
    """Use test 2: function should return nothing but invert correct key and value in the dictionary."""
    colors: dict[str, str] = {"Pegah": "green", "Ellie": "blue", "Mark": "orange"}
    
    assert favorite_color(colors) == "green"


def test_favorite_color_edge() -> str:
    """Edge test: function should return nothing with empty string."""
    colors: dict[str, str] = {}
    assert favorite_color(colors) == ""


def test_count_use1() -> dict[str, int]:
    """Use test 1: function should return the correct dictionary value according to key."""
    values: list[str] = ["hello", "bye", "hello", "hello", "bye", "good"]

    values_validation: dict[str, int] = {"hello": 3, "bye": 2, "good": 1}
    assert count(values) == values_validation


def test_count_use2() -> dict[str, int]:
    """Use test 2: function should return the correct dictionary value according to key."""
    values: list[str] = ["hello", "bye", "hello", "hello", "good", "good"]

    values_validation: dict[str, int] = {"hello": 3, "bye": 1, "good": 2}
    assert count(values) == values_validation


def test_count_edge() -> dict[str, int]:
    """Edge test : function should not return anything."""
    values: list[str] = []

    values_validation: dict[str, int] = {}
    assert count(values) == values_validation


def test_alphabetizer_use1() -> dict[str, list[str]]:
    """Use case 1: returns the correct lowercase letter."""
    words1: list[str] = ["hello", "good", "bad"]
    word_lowercase: dict[str, list[str]] = {"h": ["hello"], "g": ["good"], "b": ["bad"]}
    assert alphabetizer(words1) == word_lowercase


def test_alphabetizer_use2() -> dict[str, list[str]]:
    """Use case 2: returns the correct lowercase letter."""
    words1: list[str] = ["fun", "nice", "fast", "Nose"]
    word_lowercase: dict[str, list[str]] = {"f": ["fun", "fast"], "n": ["nice", "Nose"]}
    assert alphabetizer(words1) == word_lowercase


def test_alphabetizer_edge() -> dict[str, list[str]]:
    """Edge case : returns nothing."""
    words1: list[str] = []
    word_lowercase: dict[str, list[str]] = {}
    assert alphabetizer(words1) == word_lowercase


def test_update_attendance_use1() -> None:
    """Use case 1: return nothing but print names of students in attendance."""
    existingdict: dict[str, list[str]] = {"monday": ["molly", "adam"], "tuesday": ["molly"]}
    updated_attendance: dict[str, list[str]] = {"monday": ["molly", "adam"], "tuesday": ["molly", "adam"]}
    day: str = "tuesday"
    student: str = "adam"
    update_attendance(existingdict, day, student)
    assert existingdict == updated_attendance


def test_update_attendance_use2() -> None:
    """Use case 2: return nothing but print names of students in attendance."""
    existingdict: dict[str, list[str]] = {"monday": ["mary"], "tuesday": ["mary", "adam"]}
    updated_attendance: dict[str, list[str]] = {"monday": ["mary", "adam"], "tuesday": ["mary", "adam"]}
    day: str = "monday"
    student: str = "adam"
    update_attendance(existingdict, day, student)
    assert existingdict == updated_attendance


def test_update_attendance_edge() -> None:
    """Edge case: return nothing because no names."""
    existingdict: dict[str, list[str]] = {}
    updated_attendance: dict[str, list[str]] = {"": [""]}
    day: str = ""
    student: str = ""
    update_attendance(existingdict, day, student)
    assert existingdict == updated_attendance