import libdnf
#
# subcommand should be {} not []
# extraoptions should be {} not []
#
# fiure out how to refer to "parent" command
#
class CompletionParser(libdnf.conf.ConfigParser):
    def __init__(self):
        super(CompletionParser, self).__init__()

    def build_data(self):
        name = self.getValue('DEFAULT', 'name')
        aliases = self.getValue('DEFAULT', 'alias').split(' ')
        extraoptions = self.getValue('DEFAULT', 'extra options').split(' ')
        subcommands = set(
            self.sections() + self.getValue('DEFAULT', 'subcommands').split(' '))
        subcommands.remove('DEFAULT')

        self._command = CompletionParser.CompletionCommand(
            name, aliases, subcommands, extraoptions )
        self._command._build_subcommands()
        self._command.dump()

    class CompletionCommand():
        def __init__(self,
                     name,
                     alias = [],
                     subcommands = [],
                     extraoptions = [],
                     subcommands_opts = None,
                     extraoptions_opts = None,
        ):
            #super(CompletionParser, self).__init__()
            self._name = name
            self._alias = alias
            self._subcommands = subcommands
            self._extraoptions = extraoptions
            self._subcommands_obj = []
            self._subcommands_opts = None
            self._extraoptions_opts = None

            self._configure_subcommands()

        @property
        def name(self):
            return self._name

        #@name.setter
        #def name(self, var):
        #    self._name = var

        @property
        def alias(self):
            return self._alias

        @property
        def subcommands(self):
            return self._subcommands

        @property
        def extraoptions(self):
            return self._extraoptions

        @property
        def subcommands_opts(self):
            return self._subcommands_opts

        @property
        def extraoptions_opt(self):
            return self._extraoptions_opts

        def _build_subcommands(self):
            for s in self.subcommands:
                self._subcommands_obj.append(
                    CompletionParser.CompletionCommand(s))

        def _dump_subcommands(self):
            for s in self._subcommands_obj:
                s.dump()

        def _dump(self):
            print(
                "name:", self.name,
                "aliases:", self.alias,
                "subcommands:", self.subcommands,
                "extraoptions:", self.extraoptions,
            )

        def dump(self):
            self._dump()
            self._dump_subcommands()

        def _configure_subcommands(self):
            if self._subcommands_opts is None:
                self._subcommands_opts = []
            elif self._subcommands_opts == '+':
                self._subcommands = self.subcommands + super().subcommands

parser = CompletionParser()
parser.read('module.ini')
try:
    parser.build_data()
except Exception as e:
    print(e)
"""
# What I want to do
#
#!/bin/python

for file in dirs:
    parser = CompletionParser()
    parser.read(file)
    parser.build_commands()
    parser.dump_output()
#
# so what's happening inside?
# read function is a normal overload
# build just builds all the objects to
# store commands metadata
# for each object in memory they can be dumped


parser = libdnf.conf.ConfigParser()
parser.read('module.ini')

cmd_name = parser.getValue('DEFAULT', 'name')
cmd_list = [cmd_name]
cmd_list = cmd_list + parser.getValue('DEFAULT', 'alias').split(' ')
cmd_subc = parser.getValue('DEFAULT', 'subcommands')
cmd_xopt = parser.getValue('DEFAULT', 'extra options')

print(cmd_name)
print(cmd_list)
print(cmd_subc)
print(cmd_xopt)

"""
