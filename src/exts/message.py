from datetime import datetime, timezone
import interactions
import src.const


class Message(interactions.Extension):
    """An extension dedicated to message context menus."""

    def __init__(self, bot: interactions.Client):
        self.bot = bot
        self.targets: dict = {}

    @interactions.extension_message_command(
        name="Create help thread", scope=src.const.METADATA["guild"]
    )
    async def create_help_thread(self, ctx: interactions.CommandContext):
        self.targets[ctx.author.id] = ctx.target
        modal = interactions.Modal(
            custom_id="help_thread_creation",
            title="Create help thread",
            components=[
                interactions.TextInput(
                    style=interactions.TextStyleType.SHORT,
                    custom_id="help_thread_name",
                    label="Help thread name:",
                    value=f"[AUTO] Help thread for {ctx.target.author.username}.",
                    min_length=1,
                    max_length=100,
                ),
                interactions.TextInput(
                    style=interactions.TextStyleType.PARAGRAPH,
                    custom_id="edit_content",
                    label="Edit the content:",
                    value=ctx.target.content,
                    min_length=1,
                    max_length=2000,
                ),
            ],
        )
        await ctx.popup(modal)

    @interactions.extension_modal("help_thread_creation")
    async def help_thread_creation_modal(
        self, ctx: interactions.CommandContext, thread_name: str, content: str
    ):
        target: interactions.Message = self.targets.pop(ctx.author.id)
        # _guild: dict = await self.bot._http.get_guild(int(ctx.guild_id))
        # guild = interactions.Guild(**_guild, _client=self.bot._http)

        # sorry EdVraz, we'll need to manually do it for now until the helper is fixed.
        _thread: dict = await self.bot._http.create_thread(
            name=thread_name,
            channel_id=src.const.METADATA["channels"]["help"],
            thread_type=interactions.ChannelType.GUILD_PUBLIC_THREAD.value,
        )
        thread = interactions.Channel(**_thread, _client=self.bot._http)

        await thread.add_member(int(ctx.author.id))
        await thread.add_member(int(target.author.id))
        embed = interactions.Embed(
            title=content.split("\n")[0][:256]
            if len(content.split("\n")[0]) > 256
            else content.split("\n")[0]
            if len(content.split("\n")[0]) > 1
            else content,
            description="\n".join(content.split("\n")[1:]),
            color=0xFEE75C,
            footer=interactions.EmbedFooter(
                text="Please create a thread in #help to ask questions!"
            ),
            timestamp=datetime.now(timezone.utc),
        )
        if target.attachments:
            embed.set_image(url=target.attachments[0].url)
        await thread.send(
            f"This help thread has been created by {ctx.author.mention} for {target.author.mention}.",
            embeds=embed,
        )
        await ctx.send(
            f"{target.author.mention}, please redirect to {thread.mention} at this time."
        )
        await ctx.send(":white_check_mark: Thread created.", ephemeral=True)


def setup(bot):
    Message(bot)
