# NOTE: Optional currently is giving an error when subscripting.
# pylint: disable=unsubscriptable-object


from __future__ import annotations


from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from toml import load as load_toml
from typing import Dict, List, Optional


class TomlValueConverter:

    value_converters = {
        "str": str,
    }

    @classmethod
    def convert(cls, value, type_):
        if isinstance(type_, str):
            converter = cls.value_converters.get(type_)
            if converter is None:
                raise ValueError(f"Found no TOML value converter for type {type_}.")
            return converter(value)
        if callable(type_):
            return type_(value)
        raise ValueError(f"Unknown type given for TOML value conversion: {type_}.")


class TomlConvertible(ABC):

    @classmethod
    @abstractmethod
    def from_toml(cls, data: Dict):
        ...

    @classmethod
    def convert_value(cls, value, type_):
        match type_:
            case "str":
                return str(value)
            case "Optional[str]":


@dataclass
class Biographical(TomlConvertible):

    given_name: str
    family_name: str
    location: str
    email: str
    website: str

    @classmethod
    def from_toml(cls, data) -> Biographical:
        annotations = cls.__dict__["__annotations__"]
        found_keys = set()
        for key in data:
            if key not in annotations:
                raise ValueError(f"Unexpected key '{key}' in section 'biographical'.")
            found_keys.add(key)
        for key in annotations:
            if key not in found_keys:
                raise ValueError(f"Expected key '{key}' in section 'biographical'.")
            values = {key: type_(data[key])
                      if not issubclass(type_, TomlConvertible)
                      else type_.from_toml(data[key])
                      for key, type_ in cls.__dict__["__annotations__"].items()}
        return Biographical(**values)


@dataclass
class Degree(TomlConvertible):

    institution: str
    location: str
    date: str
    degree: str
    gpa: Optional[str]
    coursework: Optional[List[str]]

    @classmethod
    def from_toml(cls, data: Dict) -> Degree:
        ...


@dataclass
class Experience(TomlConvertible):

    title: str
    employer: str
    employer_extra: Optional[str]
    duration: str
    summary: Optional[str]
    points: Optional[List[str]]


@dataclass
class Publication(TomlConvertible):

    title: str
    authors: List[str]
    venue: str
    url: str


@dataclass
class Award(TomlConvertible):

    date: str
    title: str


@dataclass
class Resume(TomlConvertible):

    biographical: Biographical
    degrees: List[Degree]
    experiences: List[Experience]
    publications: List[Publication]
    awards: List[Award]

    @classmethod
    def from_toml_file(toml_file: Path) -> Resume:
        data = load_toml(toml_file)
        if "biographical" not in data:
            raise ValueError(f"TOML file {toml_file} missing 'biographical' section.")



def read_file_to_resume(toml_file: Path) -> Resume:
    data = load_toml(toml_file)
    ...  # TODO


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("toml_file", type=Path)
    args = parser.parse_args()

    resume = read_file_to_resume(args.toml_file)
