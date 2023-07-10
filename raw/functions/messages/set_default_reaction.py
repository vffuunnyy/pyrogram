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


class SetDefaultReaction(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``140``
        - ID: ``0xd960c4d4``

    Parameters:
        reaction: ``str``

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["reaction"]

    ID = 0xd960c4d4
    QUALNAME = "functions.messages.SetDefaultReaction"

    def __init__(self, *, reaction: str) -> None:
        self.reaction = reaction  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetDefaultReaction":
        # No flags
        
        reaction = String.read(b)
        
        return SetDefaultReaction(reaction=reaction)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.reaction))
        
        return b.getvalue()
