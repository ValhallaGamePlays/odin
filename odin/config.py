import logging
import os
from os import path

from odin.secrets import (
    ACCESS_CONTROLS,
    BACKEND,
    BOT_IDENTITY,
    BOT_ADMINS,
    CHATROOM_PRESENCE,
    XMPP_CA_CERT_FILE,
)

# This is a minimal configuration to get you started with the Text ://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.pyode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py


here = path.abspath(path.dirname(__file__))


# You might wish to have your bot respond by being called with certain
# names, rather than the BOT_PREFIX above. This option allows you to
# specify alternative prefixes the bot will respond to in addition to
# the prefix above.
BOT_ALT_PREFIXES = ('Odin',)

# Continuing on this theme, you might want to permit your users to be
# lazy and not require correct capitalization, so they can do 'Err',
# 'err' or even 'ERR'.
BOT_ALT_PREFIX_CASEINSENSITIVE = True

# If you use alternative prefixes, you might want to allow users to insert
# separators like , and ; between the prefix and the command itself. This
# allows users to refer to your bot like this (Assuming 'Err' is in your
# BOT_ALT_PREFIXES):
# "Err, status" or "Err: status"
#
# Note: There's no need to add spaces to the separators here
#
BOT_ALT_PREFIX_SEPARATORS = (':', ',', ';')

# The location where all of Err's data should be stored. Make sure to set
# this to a directory that is writable by the user running the bot.
BOT_DATA_DIR = path.join(here, 'data')

# extra search path to find custom storage plugins
BOT_EXTRA_PLUGIN_DIR = path.join(here, 'plugins')

# The location of the log file. If you set this to None, then logging will
# happen to console only.
BOT_LOG_FILE = path.join(here, 'errbot.log')

# The verbosity level of logging that is done to the above logfile, and to
# the console. This takes the standard Python logging levels, DEBUG, INFO,
# WARN, ERROR. For more info, see http://docs.python.org/library/logging.html
#
# If you encounter any issues with Err, please set your log level to
# logging.DEBUG and attach a log with your bug report to aid the developers
# in debugging the issue.
BOT_LOG_LEVEL = logging.DEBUG

# Uncomment the following and set it to True if you want the prefix to be
# optional for normal chat.
# (Meaning messages sent directly to the bot as opposed to within a MUC)
BOT_PREFIX_OPTIONAL_ON_CHAT = True

# Chme, or nickname, your bot should use. What you set here will
# be the nickname that Errbot shows in chatrooms. Note that some XMPP
# implementations, notably HipChat, are very picky about what name you
# use. In the case of HipChat, make sure this matches exactly with the
# name you gave the user.
CHATROOM_FN = 'Odin'

# A list of commands which should be responded to in private, even if
# the command was given in a MUC. For example:
# DIVERT_TO_PRIVATE = ('help', 'about', 'status')
DIVERT_TO_PRIVATE = ('help', 'about')

# Allow messages sent in a chatroom to be directed at requester.
#GROUPCHAT_NICK_PREFIXED = False
GROUPCHAT_NICK_PREFIXED = True

# XMPP supports some formatting with XEP-0071 (http://www.xmpp.org/extensions/xep-0071.html).
# It is disabled by default because XMPP clients support has been found to be spotty.
# Switch it to True to enable XHTML-IM formatting.
# XMPP_XHTML_IM = False
XMPP_XHTML_IM = True

