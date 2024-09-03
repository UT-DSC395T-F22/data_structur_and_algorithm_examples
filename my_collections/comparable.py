import sys
from typing import Any

if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    try:
        from typing_extensions import Protocol
    except ImportError:

        class Protocol:  # type: ignore
            pass


class Comparable(Protocol):
    """A base class for comparable types.

    This class exists mainly to indicate to static type checkers
    that the elements for a collection can be compared using a total order.

    You do not need to implement anything for this class.
    """

    def __eq__(self, other: Any) -> bool:
        """Equality operator."""

    def __ne__(self, other: Any) -> bool:
        """Inequality operator."""

    def __lt__(self, other: Any) -> bool:
        """Less than operator."""

    def __le__(self, other: Any) -> bool:
        """Less than or equal operator"""

    def __gt__(self, other: Any) -> bool:
        """Greater than operator."""

    def __ge__(self, other: Any) -> bool:
        """Greater than or equal operator."""

