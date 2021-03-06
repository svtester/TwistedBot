
from twistedbot.plugins.base import PluginChatBase
from twistedbot.behavior_tree import WalkSigns


class Rotate(PluginChatBase):
    @property
    def command_verb(self):
        return "rotate"

    @property
    def aliases(self):
        return ["circulate"]

    @property
    def help(self):
        return ["rotate/circulate sign group",
                "rotate - 'group' rotates (after the end, goes back to the beginning) between signs (see readme)",
                "circulate -'group' circulates (at the end, goes backward towards the beginnings) between signs"]

    def command(self, sender, command, args):
        if subject:
            self.world.bot.behavior_tree.new_command(WalkSigns, group=" ".join(subject), walk_type=verb)
        else:
            self.send_chat_message("which sign group to %s?" % verb)


plugin = Rotate
