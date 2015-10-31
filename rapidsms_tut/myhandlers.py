from rapidsms.contrib.handlers import KeywordHandler

help_text = {
    'aaa': 'Help for aaa',
    'bbb': 'Help for bbb',
    'ccc': 'Help for ccc',
}


class HelpHandler(KeywordHandler):
    keyword = "help"

    def help(self):
        """Invoked if someone just sends `HELP`.  We also call this
        from `handle` if we don't recognize the arguments to HELP.
        """
        self.respond("HELP <command> for more help on a specific command.")

    def handle(self, text):
        """Invoked if someone sends `HELP <any text>`"""
        text = text.strip().lower()
        if text == 'aaa':
            self.respond(help_text['aaa'])
        elif text == 'bbb':
            self.respond(help_text['bbb'])
        elif text == 'ccc':
            self.respond(help_text['ccc'])
        else:
            self.help()