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


class KeyboardButtonRequestPoll(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``140``
        - ID: ``0xbbc7515d``

    Parameters:
        text: ``str``
        quiz (optional): ``bool``
    """

    __slots__: List[str] = ["text", "quiz"]

    ID = 0xbbc7515d
    QUALNAME = "types.KeyboardButtonRequestPoll"

    def __init__(self, *, text: str, quiz: Optional[bool] = None) -> None:
        self.text = text  # string
        self.quiz = quiz  # flags.0?Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonRequestPoll":
        
        flags = Int.read(b)
        
        quiz = Bool.read(b) if flags & (1 << 0) else None
        text = String.read(b)
        
        return KeyboardButtonRequestPoll(text=text, quiz=quiz)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.quiz is not None else 0
        b.write(Int(flags))
        
        if self.quiz is not None:
            b.write(Bool(self.quiz))
        
        b.write(String(self.text))
        
        return b.getvalue()
