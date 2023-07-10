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


class ExportedGroupCallInvite(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.phone.ExportedGroupCallInvite`.

    Details:
        - Layer: ``140``
        - ID: ``0x204bd158``

    Parameters:
        link: ``str``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`phone.ExportGroupCallInvite <pyrogram.raw.functions.phone.ExportGroupCallInvite>`
    """

    __slots__: List[str] = ["link"]

    ID = 0x204bd158
    QUALNAME = "types.phone.ExportedGroupCallInvite"

    def __init__(self, *, link: str) -> None:
        self.link = link  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportedGroupCallInvite":
        # No flags
        
        link = String.read(b)
        
        return ExportedGroupCallInvite(link=link)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.link))
        
        return b.getvalue()
