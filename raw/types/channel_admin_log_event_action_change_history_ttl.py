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


class ChannelAdminLogEventActionChangeHistoryTTL(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``140``
        - ID: ``0x6e941a38``

    Parameters:
        prev_value: ``int`` ``32-bit``
        new_value: ``int`` ``32-bit``
    """

    __slots__: List[str] = ["prev_value", "new_value"]

    ID = 0x6e941a38
    QUALNAME = "types.ChannelAdminLogEventActionChangeHistoryTTL"

    def __init__(self, *, prev_value: int, new_value: int) -> None:
        self.prev_value = prev_value  # int
        self.new_value = new_value  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionChangeHistoryTTL":
        # No flags
        
        prev_value = Int.read(b)
        
        new_value = Int.read(b)
        
        return ChannelAdminLogEventActionChangeHistoryTTL(prev_value=prev_value, new_value=new_value)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.prev_value))
        
        b.write(Int(self.new_value))
        
        return b.getvalue()
