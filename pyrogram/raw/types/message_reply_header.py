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


class MessageReplyHeader(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageReplyHeader`.

    Details:
        - Layer: ``170``
        - ID: ``AFBC09DB``

    Parameters:
        reply_to_scheduled (``bool``, *optional*):
            N/A

        forum_topic (``bool``, *optional*):
            N/A

        quote (``bool``, *optional*):
            N/A

        reply_to_msg_id (``int`` ``32-bit``, *optional*):
            N/A

        reply_to_peer_id (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

        reply_from (:obj:`MessageFwdHeader <pyrogram.raw.base.MessageFwdHeader>`, *optional*):
            N/A

        reply_media (:obj:`MessageMedia <pyrogram.raw.base.MessageMedia>`, *optional*):
            N/A

        reply_to_top_id (``int`` ``32-bit``, *optional*):
            N/A

        quote_text (``str``, *optional*):
            N/A

        quote_entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`, *optional*):
            N/A

        quote_offset (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["reply_to_scheduled", "forum_topic", "quote", "reply_to_msg_id", "reply_to_peer_id", "reply_from", "reply_media", "reply_to_top_id", "quote_text", "quote_entities", "quote_offset"]

    ID = 0xafbc09db
    QUALNAME = "types.MessageReplyHeader"

    def __init__(self, *, reply_to_scheduled: Optional[bool] = None, forum_topic: Optional[bool] = None, quote: Optional[bool] = None, reply_to_msg_id: Optional[int] = None, reply_to_peer_id: "raw.base.Peer" = None, reply_from: "raw.base.MessageFwdHeader" = None, reply_media: "raw.base.MessageMedia" = None, reply_to_top_id: Optional[int] = None, quote_text: Optional[str] = None, quote_entities: Optional[List["raw.base.MessageEntity"]] = None, quote_offset: Optional[int] = None) -> None:
        self.reply_to_scheduled = reply_to_scheduled  # flags.2?true
        self.forum_topic = forum_topic  # flags.3?true
        self.quote = quote  # flags.9?true
        self.reply_to_msg_id = reply_to_msg_id  # flags.4?int
        self.reply_to_peer_id = reply_to_peer_id  # flags.0?Peer
        self.reply_from = reply_from  # flags.5?MessageFwdHeader
        self.reply_media = reply_media  # flags.8?MessageMedia
        self.reply_to_top_id = reply_to_top_id  # flags.1?int
        self.quote_text = quote_text  # flags.6?string
        self.quote_entities = quote_entities  # flags.7?Vector<MessageEntity>
        self.quote_offset = quote_offset  # flags.10?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageReplyHeader":
        
        flags = Int.read(b)
        
        reply_to_scheduled = True if flags & (1 << 2) else False
        forum_topic = True if flags & (1 << 3) else False
        quote = True if flags & (1 << 9) else False
        reply_to_msg_id = Int.read(b) if flags & (1 << 4) else None
        reply_to_peer_id = TLObject.read(b) if flags & (1 << 0) else None
        
        reply_from = TLObject.read(b) if flags & (1 << 5) else None
        
        reply_media = TLObject.read(b) if flags & (1 << 8) else None
        
        reply_to_top_id = Int.read(b) if flags & (1 << 1) else None
        quote_text = String.read(b) if flags & (1 << 6) else None
        quote_entities = TLObject.read(b) if flags & (1 << 7) else []
        
        quote_offset = Int.read(b) if flags & (1 << 10) else None
        return MessageReplyHeader(reply_to_scheduled=reply_to_scheduled, forum_topic=forum_topic, quote=quote, reply_to_msg_id=reply_to_msg_id, reply_to_peer_id=reply_to_peer_id, reply_from=reply_from, reply_media=reply_media, reply_to_top_id=reply_to_top_id, quote_text=quote_text, quote_entities=quote_entities, quote_offset=quote_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.reply_to_scheduled else 0
        flags |= (1 << 3) if self.forum_topic else 0
        flags |= (1 << 9) if self.quote else 0
        flags |= (1 << 4) if self.reply_to_msg_id is not None else 0
        flags |= (1 << 0) if self.reply_to_peer_id is not None else 0
        flags |= (1 << 5) if self.reply_from is not None else 0
        flags |= (1 << 8) if self.reply_media is not None else 0
        flags |= (1 << 1) if self.reply_to_top_id is not None else 0
        flags |= (1 << 6) if self.quote_text is not None else 0
        flags |= (1 << 7) if self.quote_entities else 0
        flags |= (1 << 10) if self.quote_offset is not None else 0
        b.write(Int(flags))
        
        if self.reply_to_msg_id is not None:
            b.write(Int(self.reply_to_msg_id))
        
        if self.reply_to_peer_id is not None:
            b.write(self.reply_to_peer_id.write())
        
        if self.reply_from is not None:
            b.write(self.reply_from.write())
        
        if self.reply_media is not None:
            b.write(self.reply_media.write())
        
        if self.reply_to_top_id is not None:
            b.write(Int(self.reply_to_top_id))
        
        if self.quote_text is not None:
            b.write(String(self.quote_text))
        
        if self.quote_entities is not None:
            b.write(Vector(self.quote_entities))
        
        if self.quote_offset is not None:
            b.write(Int(self.quote_offset))
        
        return b.getvalue()
