"""This package contains the domain definitions (the "data model")
used by the application.
"""

from dataclasses import dataclass, field

@dataclass
class HangmanDomain:
    """This application has only one domain entity: HangmanDomain.
    """
    # Selected level for the game
    level: int = field(default=1)

    # List of letters typed
    typed: list[str] = field(default_factory=list)
    # List of correctly guessed letters
    hits: list[str] = field(default_factory=list)
    # Mistakes counter
    error_count: int = field(default=0)

    # The correct word
    word: str = field(default_factory=str)
    # The secret word displayed to the player
    secret: str = field(default_factory=str)
    # Feedback message
    msg: str = field(default_factory=str)
    # Debug mode flag
    debug: bool = field(default=True)

# Creates a singleton instance of the domain,
# and all references to the domain will use this unique instance.
domain = HangmanDomain()