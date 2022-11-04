import typing

from dataclasses import dataclass, fields


@dataclass(frozen=True)
class Verse:
    chapter: int
    verse: int
    text: str

    @classmethod
    def from_dirty_dict(cls, **kwargs):
        """Removes unwanted elements from kwargs
        and creates new Verse instance with the only
        attributes defined at the class level.

        Args:
            **kwargs: initial parameters to initialize the class

        Returns:
            New Verse instance
        """
        attrs = set([v.name for v in fields(cls)])
        data = {k: v for k, v in kwargs.items() if k in attrs}
        return cls(**data)


@dataclass(frozen=True)
class Bible:
    """Bible object

    Attributes:
        reference: reference to the bible
        translation_id: translation id
    """
    # TODO: Homework! Finish the documentation for Verse and Bible classes!
    reference: str
    translation_id: str
    translation_name: str
    translation_note: str
    text: str
    verses: typing.List[Verse]
