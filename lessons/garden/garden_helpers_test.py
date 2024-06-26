"""Test my garden functions."""
__author__ = "730553436"

import pytest
from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date


def test_add_by_kind_case() -> None:
    """Case test: function should return nothing but append the plant to its type in dataset."""
    by_kind = {"flower": ["tulip", "rose"], "tree": ["oak", "birch"]}
    new_plant_kind: str = "flower"
    new_plant: str = "sunflower"
    add_by_kind(by_kind, new_plant_kind, new_plant)
    assert by_kind == {"flower": ["tulip", "rose", "sunflower"], "tree": ["oak", "birch"]}


def test_add_by_kind_edge() -> None:
    """Edge test: adding a kind not in dictionary."""
    by_kind = {"flower": ["tulip", "rose"]}
    add_by_kind(by_kind, "tree", "birch")
    assert by_kind == {"flower": ["tulip", "rose"], "tree": ["birch"]}


def test_add_by_date_case() -> None:
    """Case test: function should return nothing but append the plant to the correct month."""
    garden_by_date = {"january": ["tulip", "oak"], "february": ["rose", "birch"]}
    plant: str = "violet"
    month: str = "january"
    add_by_date(garden_by_date, month, plant)
    assert garden_by_date == {"january": ["tulip", "oak", "violet"], "february": ["rose", "birch"]}


def test_add_by_date_edge() -> None:
    """Edge test: adding a date not in dictionary."""
    garden_by_date = {"january": ["tulip", "oak"], "february": ["rose", "birch"]}
    add_by_date(garden_by_date, "march", "violet")
    assert garden_by_date == {"january": ["tulip", "oak"], "february": ["rose", "birch"], "march": ["violet"]}


def test_lookup_by_kind_and_date_case() -> None:
    """Case test: function should return nothing but append the specific plant to the correct month."""
    with pytest.raises(AssertionError):
        plants_by_date = {"january": ["tulip", "oak"], "february": ["rose", "birch"]}
        plants_by_kind = {"tree": ["oak", "birch"], "flower": ["tulip", "rose"]}
        kind: str = "flower"
        month: str = "february"
        # combined_list: list[str] = ["rose"]
        # result: str = add_by_date(plants_by_date, plants_by_kind, kind, month)
        lookup_by_kind_and_date(plants_by_date, plants_by_kind, kind, month)


def test_lookup_by_kind_and_date_edge() -> None:
    """Edge test: adding a kind and date not in dictionary."""
    plants_by_date = {"january": ["tulip", "oak"], "february": ["rose", "birch"]}
    plants_by_kind = {"tree": ["oak", "birch"], "flower": ["tulip", "rose"]}
    results = lookup_by_kind_and_date(plants_by_date, plants_by_kind, "tree", "april")
    output = "flowers to plant in april: []"
    assert results == output