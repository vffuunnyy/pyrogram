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


class MessageMediaGiveawayResults(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageMedia`.

    Details:
        - Layer: ``170``
        - ID: ``C6991068``

    Parameters:
        channel_id (``int`` ``64-bit``):
            N/A

        launch_msg_id (``int`` ``32-bit``):
            N/A

        winners_count (``int`` ``32-bit``):
            N/A

        unclaimed_count (``int`` ``32-bit``):
            N/A

        winners (List of ``int`` ``64-bit``):
            N/A

        months (``int`` ``32-bit``):
            N/A

        until_date (``int`` ``32-bit``):
            N/A

        only_new_subscribers (``bool``, *optional*):
            N/A

        refunded (``bool``, *optional*):
            N/A

        additional_peers_count (``int`` ``32-bit``, *optional*):
            N/A

        prize_description (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetWebPagePreview
            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: List[str] = ["channel_id", "launch_msg_id", "winners_count", "unclaimed_count", "winners", "months", "until_date", "only_new_subscribers", "refunded", "additional_peers_count", "prize_description"]

    ID = 0xc6991068
    QUALNAME = "types.MessageMediaGiveawayResults"

    def __init__(self, *, channel_id: int, launch_msg_id: int, winners_count: int, unclaimed_count: int, winners: List[int], months: int, until_date: int, only_new_subscribers: Optional[bool] = None, refunded: Optional[bool] = None, additional_peers_count: Optional[int] = None, prize_description: Optional[str] = None) -> None:
        self.channel_id = channel_id  # long
        self.launch_msg_id = launch_msg_id  # int
        self.winners_count = winners_count  # int
        self.unclaimed_count = unclaimed_count  # int
        self.winners = winners  # Vector<long>
        self.months = months  # int
        self.until_date = until_date  # int
        self.only_new_subscribers = only_new_subscribers  # flags.0?true
        self.refunded = refunded  # flags.2?true
        self.additional_peers_count = additional_peers_count  # flags.3?int
        self.prize_description = prize_description  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaGiveawayResults":
        
        flags = Int.read(b)
        
        only_new_subscribers = True if flags & (1 << 0) else False
        refunded = True if flags & (1 << 2) else False
        channel_id = Long.read(b)
        
        additional_peers_count = Int.read(b) if flags & (1 << 3) else None
        launch_msg_id = Int.read(b)
        
        winners_count = Int.read(b)
        
        unclaimed_count = Int.read(b)
        
        winners = TLObject.read(b, Long)
        
        months = Int.read(b)
        
        prize_description = String.read(b) if flags & (1 << 1) else None
        until_date = Int.read(b)
        
        return MessageMediaGiveawayResults(channel_id=channel_id, launch_msg_id=launch_msg_id, winners_count=winners_count, unclaimed_count=unclaimed_count, winners=winners, months=months, until_date=until_date, only_new_subscribers=only_new_subscribers, refunded=refunded, additional_peers_count=additional_peers_count, prize_description=prize_description)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.only_new_subscribers else 0
        flags |= (1 << 2) if self.refunded else 0
        flags |= (1 << 3) if self.additional_peers_count is not None else 0
        flags |= (1 << 1) if self.prize_description is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.channel_id))
        
        if self.additional_peers_count is not None:
            b.write(Int(self.additional_peers_count))
        
        b.write(Int(self.launch_msg_id))
        
        b.write(Int(self.winners_count))
        
        b.write(Int(self.unclaimed_count))
        
        b.write(Vector(self.winners, Long))
        
        b.write(Int(self.months))
        
        if self.prize_description is not None:
            b.write(String(self.prize_description))
        
        b.write(Int(self.until_date))
        
        return b.getvalue()
