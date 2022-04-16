from interactions import Option, OptionType, ChannelType
from ..const import METADATA

cmd = dict(
    name="mod",
    description="Handles all moderation aspects.",
    scope=METADATA["guild"],
    options=[
        Option(
            type=OptionType.SUB_COMMAND_GROUP,
            name="member",
            description="Handles moderating a member.",
            options=[
                Option(
                    type=OptionType.SUB_COMMAND,
                    name="ban",
                    description="Bans a user.",
                    options=[
                        Option(
                            type=OptionType.USER,
                            name="user",
                            description="The user you wish to ban.",
                            required=True,
                        ),
                        Option(
                            type=OptionType.STRING,
                            name="reason",
                            description="The reason behind why you want to ban them.",
                            required=False,
                        ),
                    ],
                ),
                Option(
                    type=OptionType.SUB_COMMAND,
                    name="unban",
                    description="Unbans a user.",
                    options=[
                        Option(
                            type=OptionType.INTEGER,
                            name="id",
                            description="The ID of the user you wish to unban.",
                            required=True,
                        ),
                        Option(
                            type=OptionType.STRING,
                            name="reason",
                            description="The reason behind why you want to unban them.",
                            required=False,
                        ),
                    ],
                ),
                Option(
                    type=OptionType.SUB_COMMAND,
                    name="kick",
                    description="Kicks a user.",
                    options=[
                        Option(
                            type=OptionType.USER,
                            name="user",
                            description="The user you wish to kick.",
                            required=True,
                        ),
                        Option(
                            type=OptionType.STRING,
                            name="reason",
                            description="The reason behind why you want to kick them.",
                            required=False,
                        ),
                    ],
                ),
                Option(
                    type=OptionType.SUB_COMMAND,
                    name="warn",
                    description="Warns a user.",
                    options=[
                        Option(
                            type=OptionType.USER,
                            name="user",
                            description="The user you wish to warn.",
                            required=True,
                        ),
                        Option(
                            type=OptionType.STRING,
                            name="reason",
                            description="The reason behind why you want to warn them.",
                            required=False,
                        ),
                    ],
                ),
            ],
        ),
        Option(
            type=OptionType.SUB_COMMAND_GROUP,
            name="channel",
            description="Handles moderating a channel.",
            options=[
                Option(
                    type=OptionType.SUB_COMMAND,
                    name="slowmode",
                    description="Applies a slowmode to a channel.",
                    options=[
                        Option(
                            type=OptionType.CHANNEL,
                            name="channel",
                            description="The channel you wish to slowmode.",
                            required=True,
                            channel_types=[ChannelType.GUILD_TEXT],
                        ),
                        Option(
                            type=OptionType.INTEGER,
                            name="length",
                            description="How long you want the slowmode to be. (in seconds)",
                            required=True,
                            max_value=21600,
                        ),
                    ],
                ),
                Option(
                    type=OptionType.SUB_COMMAND,
                    name="purge",
                    description="\"Purges\" or deletes messages from a channel in bulk.",
                    options=[
                        Option(
                            type=OptionType.CHANNEL,
                            name="channel",
                            description="The channel you wish to slowmode.",
                            required=True,
                            channel_types=[ChannelType.GUILD_TEXT],
                        ),
                        Option(
                            type=OptionType.INTEGER,
                            name="length",
                            description="How many messages you wish to purge.",
                            required=True,
                        ),
                    ],
                ),
                Option(
                    type=OptionType.SUB_COMMAND,
                    name="lock",
                    description="Locks down a channel into read-only mode.",
                    options=[
                        Option(
                            type=OptionType.CHANNEL,
                            name="channel",
                            description="The channel you wish to lock.",
                            required=True,
                            channel_types=[ChannelType.GUILD_TEXT],
                        ),
                    ],
                ),
                Option(
                    type=OptionType.SUB_COMMAND,
                    name="unlock",
                    description="Unlocks a channel for public use.",
                    options=[
                        Option(
                            type=OptionType.CHANNEL,
                            name="channel",
                            description="The channel you wish to unlock.",
                            required=True,
                            channel_types=[ChannelType.GUILD_TEXT],
                        ),
                    ],
                ),
            ],
        ),
    ],
)