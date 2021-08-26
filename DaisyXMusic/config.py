import os
from os import path
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = "AQDBG0VCJ02r3H2yY2Y9-YTpjsOlL3SF6U3MCG5_WieCP0OWHGCNsuGS1Tpb_UNTQ4wZKozRHW4sLqw-Ic_xqsyIt7agc_bX-xzPYBdjxeEOVJW3sWHAO3OyJ0egIrpuRQedMklRhlehliS4sPGvvlVod9lqCbLoq9skDqomxJWdWm_Rgt5bplXoBooK9a6lUN7q4NKaoFmCfr7BgCteuxTFXFGPpQiG1pV9sNL1HJj7qaPgPTHv-KreRmT8L5gBHxcfsl9XPnGSrOS3mz9TKcVQEJ4e7WHdS1NHy-I7baR5WfS-5yqHTVWiPzf6d-AzaeCGtE-vrs2Si3AevWpyOgXJXWo0nAA"
BOT_TOKEN = "1780504797:AAE7R4gv0S44SJd0bI_BZFwt7GSfUHkhcag"
BOT_NAME = "@Khan_MusicBot"
UPDATES_CHANNEL = "KhanVlog"
BG_IMAGE = "https://telegra.ph/file/9b13ea3ce046a1a5c8098.png"
admins = {}
API_ID = int("4453240")
API_HASH = "543eea32f4ed971e6a7ced59d0e56aa2"
BOT_USERNAME = "Khan Music Bot"
ASSISTANT_NAME = "KhanMusicAssistant"
SUPPORT_GROUP = "KhanChat"
PROJECT_NAME = "VCPlayBot2.0"
SOURCE_CODE = "github.com/QueenArzoo/VCPlayBot"
DURATION_LIMIT = int("15")
ARQ_API_KEY = None
PMPERMIT = "ENABLE"
LOG_GRP = None
COMMAND_PREFIXES = list("/")

SUDO_USERS = list("1708421347")
