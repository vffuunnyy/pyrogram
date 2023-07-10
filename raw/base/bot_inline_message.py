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

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

BotInlineMessage = Union[raw.types.BotInlineMessageMediaAuto, raw.types.BotInlineMessageMediaContact, raw.types.BotInlineMessageMediaGeo, raw.types.BotInlineMessageMediaInvoice, raw.types.BotInlineMessageMediaVenue, raw.types.BotInlineMessageText]


# noinspection PyRedeclaration
class BotInlineMessage:  # type: ignore
    """This base type has 6 constructors available.

    Constructors:
        .. hlist::
            :columns: 2

            - :obj:`BotInlineMessageMediaAuto <pyrogram.raw.types.BotInlineMessageMediaAuto>`
            - :obj:`BotInlineMessageMediaContact <pyrogram.raw.types.BotInlineMessageMediaContact>`
            - :obj:`BotInlineMessageMediaGeo <pyrogram.raw.types.BotInlineMessageMediaGeo>`
            - :obj:`BotInlineMessageMediaInvoice <pyrogram.raw.types.BotInlineMessageMediaInvoice>`
            - :obj:`BotInlineMessageMediaVenue <pyrogram.raw.types.BotInlineMessageMediaVenue>`
            - :obj:`BotInlineMessageText <pyrogram.raw.types.BotInlineMessageText>`
    """

    QUALNAME = "pyrogram.raw.base.BotInlineMessage"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/bot-inline-message")
