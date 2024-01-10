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


class MessageActionGiftCode(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``170``
        - ID: ``678C2E09``

    Parameters:
        months (``int`` ``32-bit``):
            N/A

        slug (``str``):
            N/A

        via_giveaway (``bool``, *optional*):
            N/A

        unclaimed (``bool``, *optional*):
            N/A

        boost_peer (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

        currency (``str``, *optional*):
            N/A

        amount (``int`` ``64-bit``, *optional*):
            N/A

        crypto_currency (``str``, *optional*):
            N/A

        crypto_amount (``int`` ``64-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["months", "slug", "via_giveaway", "unclaimed", "boost_peer", "currency", "amount", "crypto_currency", "crypto_amount"]

    ID = 0x678c2e09
    QUALNAME = "types.MessageActionGiftCode"

    def __init__(self, *, months: int, slug: str, via_giveaway: Optional[bool] = None, unclaimed: Optional[bool] = None, boost_peer: "raw.base.Peer" = None, currency: Optional[str] = None, amount: Optional[int] = None, crypto_currency: Optional[str] = None, crypto_amount: Optional[int] = None) -> None:
        self.months = months  # int
        self.slug = slug  # string
        self.via_giveaway = via_giveaway  # flags.0?true
        self.unclaimed = unclaimed  # flags.2?true
        self.boost_peer = boost_peer  # flags.1?Peer
        self.currency = currency  # flags.2?string
        self.amount = amount  # flags.2?long
        self.crypto_currency = crypto_currency  # flags.3?string
        self.crypto_amount = crypto_amount  # flags.3?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionGiftCode":
        
        flags = Int.read(b)
        
        via_giveaway = True if flags & (1 << 0) else False
        unclaimed = True if flags & (1 << 2) else False
        boost_peer = TLObject.read(b) if flags & (1 << 1) else None
        
        months = Int.read(b)
        
        slug = String.read(b)
        
        currency = String.read(b) if flags & (1 << 2) else None
        amount = Long.read(b) if flags & (1 << 2) else None
        crypto_currency = String.read(b) if flags & (1 << 3) else None
        crypto_amount = Long.read(b) if flags & (1 << 3) else None
        return MessageActionGiftCode(months=months, slug=slug, via_giveaway=via_giveaway, unclaimed=unclaimed, boost_peer=boost_peer, currency=currency, amount=amount, crypto_currency=crypto_currency, crypto_amount=crypto_amount)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.via_giveaway else 0
        flags |= (1 << 2) if self.unclaimed else 0
        flags |= (1 << 1) if self.boost_peer is not None else 0
        flags |= (1 << 2) if self.currency is not None else 0
        flags |= (1 << 2) if self.amount is not None else 0
        flags |= (1 << 3) if self.crypto_currency is not None else 0
        flags |= (1 << 3) if self.crypto_amount is not None else 0
        b.write(Int(flags))
        
        if self.boost_peer is not None:
            b.write(self.boost_peer.write())
        
        b.write(Int(self.months))
        
        b.write(String(self.slug))
        
        if self.currency is not None:
            b.write(String(self.currency))
        
        if self.amount is not None:
            b.write(Long(self.amount))
        
        if self.crypto_currency is not None:
            b.write(String(self.crypto_currency))
        
        if self.crypto_amount is not None:
            b.write(Long(self.crypto_amount))
        
        return b.getvalue()
