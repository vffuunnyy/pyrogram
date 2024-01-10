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

from pyrogram.methods.bots.answer_callback_query import AnswerCallbackQuery
from pyrogram.methods.bots.answer_inline_query import AnswerInlineQuery
from pyrogram.methods.bots.delete_bot_commands import DeleteBotCommands
from pyrogram.methods.bots.get_bot_commands import GetBotCommands
from pyrogram.methods.bots.get_game_high_scores import GetGameHighScores
from pyrogram.methods.bots.get_inline_bot_results import GetInlineBotResults
from pyrogram.methods.bots.request_callback_answer import RequestCallbackAnswer
from pyrogram.methods.bots.send_game import SendGame
from pyrogram.methods.bots.send_inline_bot_result import SendInlineBotResult
from pyrogram.methods.bots.set_bot_commands import SetBotCommands
from pyrogram.methods.bots.set_game_score import SetGameScore


class Bots(
    AnswerCallbackQuery,
    AnswerInlineQuery,
    GetInlineBotResults,
    RequestCallbackAnswer,
    SendInlineBotResult,
    SendGame,
    SetGameScore,
    GetGameHighScores,
    SetBotCommands,
    GetBotCommands,
    DeleteBotCommands,
):
    pass
