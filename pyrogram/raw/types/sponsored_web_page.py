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


class SponsoredWebPage(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SponsoredWebPage`.

    Details:
        - Layer: ``170``
        - ID: ``3DB8EC63``

    Parameters:
        url (``str``):
            N/A

        site_name (``str``):
            N/A

        photo (:obj:`Photo <pyrogram.raw.base.Photo>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["url", "site_name", "photo"]

    ID = 0x3db8ec63
    QUALNAME = "types.SponsoredWebPage"

    def __init__(self, *, url: str, site_name: str, photo: "raw.base.Photo" = None) -> None:
        self.url = url  # string
        self.site_name = site_name  # string
        self.photo = photo  # flags.0?Photo

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SponsoredWebPage":
        
        flags = Int.read(b)
        
        url = String.read(b)
        
        site_name = String.read(b)
        
        photo = TLObject.read(b) if flags & (1 << 0) else None
        
        return SponsoredWebPage(url=url, site_name=site_name, photo=photo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.photo is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.url))
        
        b.write(String(self.site_name))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        return b.getvalue()
