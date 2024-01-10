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

from pyrogram.methods.chats.add_chat_members import AddChatMembers
from pyrogram.methods.chats.archive_chats import ArchiveChats
from pyrogram.methods.chats.ban_chat_member import BanChatMember
from pyrogram.methods.chats.create_channel import CreateChannel
from pyrogram.methods.chats.create_group import CreateGroup
from pyrogram.methods.chats.create_supergroup import CreateSupergroup
from pyrogram.methods.chats.delete_channel import DeleteChannel
from pyrogram.methods.chats.delete_chat_photo import DeleteChatPhoto
from pyrogram.methods.chats.delete_supergroup import DeleteSupergroup
from pyrogram.methods.chats.delete_user_history import DeleteUserHistory
from pyrogram.methods.chats.get_chat import GetChat
from pyrogram.methods.chats.get_chat_event_log import GetChatEventLog
from pyrogram.methods.chats.get_chat_member import GetChatMember
from pyrogram.methods.chats.get_chat_members import GetChatMembers
from pyrogram.methods.chats.get_chat_members_count import GetChatMembersCount
from pyrogram.methods.chats.get_chat_online_count import GetChatOnlineCount
from pyrogram.methods.chats.get_dialogs import GetDialogs
from pyrogram.methods.chats.get_dialogs_count import GetDialogsCount
from pyrogram.methods.chats.get_nearby_chats import GetNearbyChats
from pyrogram.methods.chats.get_send_as_chats import GetSendAsChats
from pyrogram.methods.chats.iter_chat_members import IterChatMembers
from pyrogram.methods.chats.iter_dialogs import IterDialogs
from pyrogram.methods.chats.join_chat import JoinChat
from pyrogram.methods.chats.leave_chat import LeaveChat
from pyrogram.methods.chats.mark_chat_unread import MarkChatUnread
from pyrogram.methods.chats.pin_chat_message import PinChatMessage
from pyrogram.methods.chats.promote_chat_member import PromoteChatMember
from pyrogram.methods.chats.restrict_chat_member import RestrictChatMember
from pyrogram.methods.chats.set_administrator_title import SetAdministratorTitle
from pyrogram.methods.chats.set_chat_description import SetChatDescription
from pyrogram.methods.chats.set_chat_permissions import SetChatPermissions
from pyrogram.methods.chats.set_chat_photo import SetChatPhoto
from pyrogram.methods.chats.set_chat_protected_content import SetChatProtectedContent
from pyrogram.methods.chats.set_chat_title import SetChatTitle
from pyrogram.methods.chats.set_send_as_chat import SetSendAsChat
from pyrogram.methods.chats.set_slow_mode import SetSlowMode
from pyrogram.methods.chats.unarchive_chats import UnarchiveChats
from pyrogram.methods.chats.unban_chat_member import UnbanChatMember
from pyrogram.methods.chats.unpin_all_chat_messages import UnpinAllChatMessages
from pyrogram.methods.chats.unpin_chat_message import UnpinChatMessage
from pyrogram.methods.chats.update_chat_username import UpdateChatUsername


class Chats(
    GetChat,
    LeaveChat,
    JoinChat,
    BanChatMember,
    UnbanChatMember,
    RestrictChatMember,
    PromoteChatMember,
    GetChatMembers,
    GetChatMember,
    SetChatPhoto,
    DeleteChatPhoto,
    SetChatTitle,
    SetChatDescription,
    PinChatMessage,
    UnpinChatMessage,
    GetDialogs,
    GetChatMembersCount,
    IterDialogs,
    IterChatMembers,
    UpdateChatUsername,
    SetChatPermissions,
    GetDialogsCount,
    ArchiveChats,
    UnarchiveChats,
    CreateGroup,
    CreateSupergroup,
    CreateChannel,
    AddChatMembers,
    DeleteChannel,
    DeleteSupergroup,
    GetNearbyChats,
    SetAdministratorTitle,
    SetSlowMode,
    DeleteUserHistory,
    UnpinAllChatMessages,
    MarkChatUnread,
    GetChatEventLog,
    GetChatOnlineCount,
    GetSendAsChats,
    SetSendAsChat,
    SetChatProtectedContent,
):
    pass
