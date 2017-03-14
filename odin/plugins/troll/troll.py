from errbot import BotPlugin, re_botcmd
import re


class TrollBot(BotPlugin):

    @re_botcmd(pattern=r"(^| )cookie( |$)", prefixed=False, flags=re.IGNORECASE)
    def cookie(self, message, match):
        return 'What, you want a cookie!?'

    @re_botcmd(pattern=r"(^| )complex doom( |$)", prefixed=False, flags=re.IGNORECASE)
    def complex_doom(self, message, match):
        return 'Fuck Complex Doom!'

    @re_botcmd(pattern=r"(^| )call of duty( |$)", prefixed=False, flags=re.IGNORECASE)
    def call_of_duty(self, message, match):
        return 'Worst VG series ever BTW...'

    @re_botcmd(pattern=r"(^| )shit( |$)", prefixed=False, flags=re.IGNORECASE)
    def shit(self, message, match):
        return 'fuck'

