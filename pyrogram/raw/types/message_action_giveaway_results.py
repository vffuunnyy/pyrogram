#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class MessageActionGiveawayResults(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``170``
        - ID: ``2A9FADC5``

    Parameters:
        winners_count (``int`` ``32-bit``):
            N/A

        unclaimed_count (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["winners_count", "unclaimed_count"]

    ID = 0x2a9fadc5
    QUALNAME = "types.MessageActionGiveawayResults"

    def __init__(self, *, winners_count: int, unclaimed_count: int) -> None:
        self.winners_count = winners_count  # int
        self.unclaimed_count = unclaimed_count  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionGiveawayResults":
        # No flags
        
        winners_count = Int.read(b)
        
        unclaimed_count = Int.read(b)
        
        return MessageActionGiveawayResults(winners_count=winners_count, unclaimed_count=unclaimed_count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.winners_count))
        
        b.write(Int(self.unclaimed_count))
        
        return b.getvalue()
