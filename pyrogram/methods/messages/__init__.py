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

from pyrogram.methods.messages.copy_media_group import CopyMediaGroup
from pyrogram.methods.messages.copy_message import CopyMessage
from pyrogram.methods.messages.delete_messages import DeleteMessages
from pyrogram.methods.messages.download_media import DownloadMedia
from pyrogram.methods.messages.edit_inline_caption import EditInlineCaption
from pyrogram.methods.messages.edit_inline_media import EditInlineMedia
from pyrogram.methods.messages.edit_inline_reply_markup import EditInlineReplyMarkup
from pyrogram.methods.messages.edit_inline_text import EditInlineText
from pyrogram.methods.messages.edit_message_caption import EditMessageCaption
from pyrogram.methods.messages.edit_message_media import EditMessageMedia
from pyrogram.methods.messages.edit_message_reply_markup import EditMessageReplyMarkup
from pyrogram.methods.messages.edit_message_text import EditMessageText
from pyrogram.methods.messages.forward_messages import ForwardMessages
from pyrogram.methods.messages.get_discussion_message import GetDiscussionMessage
from pyrogram.methods.messages.get_history import GetHistory
from pyrogram.methods.messages.get_history_count import GetHistoryCount
from pyrogram.methods.messages.get_media_group import GetMediaGroup
from pyrogram.methods.messages.get_messages import GetMessages
from pyrogram.methods.messages.iter_history import IterHistory
from pyrogram.methods.messages.read_history import ReadHistory
from pyrogram.methods.messages.retract_vote import RetractVote
from pyrogram.methods.messages.search_global import SearchGlobal
from pyrogram.methods.messages.search_global_count import SearchGlobalCount
from pyrogram.methods.messages.search_messages import SearchMessages
from pyrogram.methods.messages.search_messages_count import SearchMessagesCount
from pyrogram.methods.messages.send_animation import SendAnimation
from pyrogram.methods.messages.send_audio import SendAudio
from pyrogram.methods.messages.send_cached_media import SendCachedMedia
from pyrogram.methods.messages.send_chat_action import SendChatAction
from pyrogram.methods.messages.send_contact import SendContact
from pyrogram.methods.messages.send_dice import SendDice
from pyrogram.methods.messages.send_document import SendDocument
from pyrogram.methods.messages.send_location import SendLocation
from pyrogram.methods.messages.send_media_group import SendMediaGroup
from pyrogram.methods.messages.send_message import SendMessage
from pyrogram.methods.messages.send_photo import SendPhoto
from pyrogram.methods.messages.send_poll import SendPoll
from pyrogram.methods.messages.send_reaction import SendReaction
from pyrogram.methods.messages.send_sticker import SendSticker
from pyrogram.methods.messages.send_venue import SendVenue
from pyrogram.methods.messages.send_video import SendVideo
from pyrogram.methods.messages.send_video_note import SendVideoNote
from pyrogram.methods.messages.send_voice import SendVoice
from pyrogram.methods.messages.stop_poll import StopPoll
from pyrogram.methods.messages.vote_poll import VotePoll


class Messages(
    DeleteMessages,
    EditMessageCaption,
    EditMessageReplyMarkup,
    EditMessageMedia,
    EditMessageText,
    ForwardMessages,
    GetHistory,
    GetMediaGroup,
    GetMessages,
    SendAudio,
    SendChatAction,
    SendContact,
    SendDocument,
    SendAnimation,
    SendLocation,
    SendMediaGroup,
    SendMessage,
    SendPhoto,
    SendSticker,
    SendVenue,
    SendVideo,
    SendVideoNote,
    SendVoice,
    SendPoll,
    VotePoll,
    StopPoll,
    RetractVote,
    DownloadMedia,
    IterHistory,
    SendCachedMedia,
    GetHistoryCount,
    ReadHistory,
    EditInlineText,
    EditInlineCaption,
    EditInlineMedia,
    EditInlineReplyMarkup,
    SendDice,
    SearchMessages,
    SearchGlobal,
    CopyMessage,
    CopyMediaGroup,
    SearchMessagesCount,
    SearchGlobalCount,
    GetDiscussionMessage,
    SendReaction,
):
    pass
