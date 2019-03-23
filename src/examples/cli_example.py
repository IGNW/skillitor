#!/usr/bin/env python3
import cmd

from skillitor.core.command_interpreter import CommandInterpreter


class CliQuery(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.qp = CommandInterpreter()
        self.prompt = 'Skillitor> '

    def do_skillset(self, line):
        errmsg = self.qp.process_set_cmd(line)
        if errmsg:
            print("ERROR: " + errmsg)

    def do_skillunset(self, line):
        errmsg = self.qp.process_set_cmd(line)
        if errmsg:
            print("ERROR: " + errmsg)

    def do_skillfind(self, line):
        errmsg, result = self.qp.process_find_cmd(line)
        if errmsg:
            print("ERROR: " + errmsg)
        print("Got find results: " + str(result))

    def do_skillshow(self, line):
        print("Command not implemented.")

    def do_skilladmin(self, _):
        print("Command not implemented.")

    def do_skilldebug(self, _):
        print("Command not implemented.")

    def do_q(self, _):
        return True


if __name__ == '__main__':
    CliQuery().cmdloop()
