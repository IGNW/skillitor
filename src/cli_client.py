#!/usr/bin/env python3
import cmd
import grpc
import re


from skillitor.core.api import skillitor_pb2, skillitor_pb2_grpc
from skillitor.core.command_interpreter import CommandInterpreter


class CliClient(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.qp = CommandInterpreter()
        self.prompt = '> '
        self.server = {
            'hostname': '',
            'port': '',
            'user': '',
        }
        self.rpc_handle = None
        self.current_user = None

    def _update_prompt(self):
        if self.server['hostname']:
            self.prompt = "[{user}@{hostname}:{port}]> ".format(**self.server)
        else:
            self.prompt = '> '

    def emptyline(self):
        pass  # Do nothing

    def do_connect(self, line):
        match = re.search(r'([^:\s]+@[^:\s]+)(?:(:[\w\d.]+)(:\d+)?)?', line)
        if not line or match is None:
            print("Usage: connect <email>[:<hostname>[:<port>]]")
            return

        email, hostname, port = match.groups()
        hostname = hostname.strip(':') if hostname else '127.0.0.1'
        port = port.strip(':') if port else 50051
        self.server = {'hostname': hostname, 'port': port, 'user': email}
        self._update_prompt()
        channel = grpc.insecure_channel('{hostname}:{port}'.format(**self.server))
        self.rpc_handle = skillitor_pb2_grpc.SkillitorQueryStub(channel)

    def do_disconnect(self, line):
        self.server = {'hostname': '', 'port': '', 'user': ''}  # Server settings
        self.rpc_handle = None
        self._update_prompt()

    def do_quit(self, _):
        return True

    def do_skillset(self, line, unset=False):
        if self.rpc_handle is None:
            print("You must run 'connect' first to specify server settings")
            return

        if not line:
            print("Usage: skillset <skill_list> [for <email>]")
            return

        self.qp.process_set_cmd(self.server['user'], self.rpc_handle, line, unset)

    def do_skillunset(self, line):
        self.do_skillset(line, unset=True)

    def do_skillfind(self, line):
        if self.rpc_handle is None:
            print("You must run 'connect' first to specify server settings")
            return

        if not line:
            print("Usage: skillfind any|all <skill_list>")
            return

        self.qp.process_find_cmd(self.rpc_handle, line)


if __name__ == '__main__':
    CliClient().cmdloop()
