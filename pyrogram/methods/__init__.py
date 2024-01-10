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

from pyrogram.methods.advanced import Advanced
from pyrogram.methods.auth import Auth
from pyrogram.methods.bots import Bots
from pyrogram.methods.chats import Chats
from pyrogram.methods.contacts import Contacts
from pyrogram.methods.decorators import Decorators
from pyrogram.methods.invite_links import InviteLinks
from pyrogram.methods.messages import Messages
from pyrogram.methods.password import Password
from pyrogram.methods.users import Users
from pyrogram.methods.utilities import Utilities


class Methods(
    Advanced,
    Auth,
    Bots,
    Contacts,
    Password,
    Chats,
    Users,
    Messages,
    Decorators,
    Utilities,
    InviteLinks,
):
    pass
