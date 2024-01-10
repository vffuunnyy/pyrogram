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

from pyrogram.methods.auth.accept_terms_of_service import AcceptTermsOfService
from pyrogram.methods.auth.check_password import CheckPassword
from pyrogram.methods.auth.connect import Connect
from pyrogram.methods.auth.disconnect import Disconnect
from pyrogram.methods.auth.get_password_hint import GetPasswordHint
from pyrogram.methods.auth.initialize import Initialize
from pyrogram.methods.auth.log_out import LogOut
from pyrogram.methods.auth.recover_password import RecoverPassword
from pyrogram.methods.auth.resend_code import ResendCode
from pyrogram.methods.auth.send_code import SendCode
from pyrogram.methods.auth.send_recovery_code import SendRecoveryCode
from pyrogram.methods.auth.sign_in import SignIn
from pyrogram.methods.auth.sign_in_bot import SignInBot
from pyrogram.methods.auth.sign_up import SignUp
from pyrogram.methods.auth.terminate import Terminate


class Auth(
    AcceptTermsOfService,
    CheckPassword,
    Connect,
    Disconnect,
    GetPasswordHint,
    Initialize,
    LogOut,
    RecoverPassword,
    ResendCode,
    SendCode,
    SendRecoveryCode,
    SignIn,
    SignInBot,
    SignUp,
    Terminate,
):
    pass
