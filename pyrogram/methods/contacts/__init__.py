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

from pyrogram.methods.contacts.add_contact import AddContact
from pyrogram.methods.contacts.delete_contacts import DeleteContacts
from pyrogram.methods.contacts.get_contacts import GetContacts
from pyrogram.methods.contacts.get_contacts_count import GetContactsCount
from pyrogram.methods.contacts.import_contacts import ImportContacts


class Contacts(GetContacts, DeleteContacts, ImportContacts, GetContactsCount, AddContact):
    pass
