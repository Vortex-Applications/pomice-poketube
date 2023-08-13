"""
Pomice (PokeTube)
~~~~~~
The modern Lavalink wrapper designed for discord.py, retrofitted with PokeTube support.

Copyright (c) 2023, cloudwithax dba Vortex Applications.

Licensed under GPL-3.0
"""
import discord

if not discord.version_info.major >= 2:

    class DiscordPyOutdated(Exception):
        pass

    raise DiscordPyOutdated(
        "You must have discord.py (v2.0 or greater) to use this library. "
        "Uninstall your current version and install discord.py 2.0 "
        "using 'pip install discord.py'",
    )

__version__ = "2.7.1"
__title__ = "pomice-poketube"
__author__ = "cloudwithax"
__license__ = "GPL-3.0"
__copyright__ = "Copyright (c) 2023, cloudwithax dba Vortex Applications."

from .enums import *
from .events import *
from .exceptions import *
from .filters import *
from .objects import *
from .queue import *
from .player import *
from .pool import *
from .routeplanner import *