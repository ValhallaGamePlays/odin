from errbot import BotPlugin, re_botcmd
import re
import string


def make_trigger(word):
    return r"(^| |[" + string.punctuation + "])" + word + r"( |[" + string.punctuation + "]|$)"


class TrollBot(BotPlugin):

    @re_botcmd(pattern=make_trigger("cookie"), prefixed=False, flags=re.IGNORECASE)
    def cookie(self, message, match):
        return 'What, you want a cookie!?'

    @re_botcmd(pattern=make_trigger("complex doom"), prefixed=False, flags=re.IGNORECASE)
    def complex_doom(self, message, match):
        return 'Fuck Complex Doom!'

    @re_botcmd(pattern=make_trigger("call of duty"), prefixed=False, flags=re.IGNORECASE)
    def call_of_duty(self, message, match):
        return 'Worst VG series ever BTW...'

    @re_botcmd(pattern=make_trigger("shit"), prefixed=False, flags=re.IGNORECASE)
    def shit(self, message, match):
        return 'fuck'

