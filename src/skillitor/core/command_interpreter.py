#!/usr/bin/env python3

import re
from typing import List

from .skills import SkillLevel
from skillitor.core.api import skillitor_pb2, skillitor_pb2_grpc


class CommandInterpreter:
    _PARSE_ERROR = 'Failed to parse command. Please check your syntax'
    _patterns = {
        're_skill_id': r"""[-.#+*\w\d ]+""",
        're_beginner': r'{}|b|beginner'.format(SkillLevel.BEGINNER),
        're_intermediate': r'{}|i|intermediate'.format(SkillLevel.INTERMEDIATE),
        're_advanced': r'{}|a|advanced'.format(SkillLevel.ADVANCED),
    }
    _patterns['re_skill_level'] = r'/(?:{re_beginner}|{re_intermediate}|{re_advanced})'.format(**_patterns)
    _patterns['re_skill_list'] = r"""
        (?:
            {re_skill_id}           # Skill name
            (?:{re_skill_level})?   # Optional skill level
            \s*
            (?:                     # Optionally more skills/levels separated
                ,\s*                # by a comma
                {re_skill_id}
                (?:{re_skill_level})?
                \s*
            )*
        )
    """.format(**_patterns)
    _patterns['re_skill_and_level'] = r'({re_skill_id})({re_skill_level})?'.format(**_patterns)

    _re_set_statement = re.compile(r"""
        ({re_skill_list})
        (?:for\ (\S+@\S+))?      # Optional email address for user other than self
        \ *$                     # Ensure that we've matched everything to EOL
    """.format(**_patterns), re.VERBOSE)

    _re_find_statement = re.compile(r"""
        (any|all)\s+
        ({re_skill_list})
        \ *$                     # Ensure that we've matched everything to EOL
    """.format(**_patterns), re.VERBOSE)

    def process_set_cmd(self, current_user: str,
                        rpc_handle: skillitor_pb2_grpc.SkillitorQueryStub,
                        query_text: str, unset=False):
        """Parse set/unset command arguments

        Args:
            current_user: FIXME
            rpc_handle: FIXME
            query_text: FIXME
            unset: FIXME

        """
        errmsg = ''
        email = None
        skill_list = None
        match = self._re_set_statement.match(query_text)
        if match:
            skill_string, email = match.groups()
            skill_list = self._parse_skill_string(skill_string)
            simple_skill_list = [(s.skill_name, s.skill_level) for s in skill_list]
            print("DEBUG: Got email ({}) and skills ({})".format(email, simple_skill_list))
        else:
            errmsg = self._PARSE_ERROR
        email = email or current_user  # Use current user as a default
        if errmsg:
            print("ERROR: " + errmsg)
            return

        sa = skillitor_pb2.SkillAssociation(user_email=email, skills=skill_list)
        if unset:
            response = rpc_handle.UnsetSkills(sa)
            action = 'UnsetSkills'
        else:
            response = rpc_handle.SetSkills(sa)
            action = 'SetSkills'

        print("Sent a {} message, got response type: {}. "
              "String representation: {}".format(
            action, type(response), response))
        if not response.success:
            print("Error message was: " + response.error_msg)

        return errmsg, email, skill_list

    def process_find_cmd(self, rpc_handle: skillitor_pb2_grpc.SkillitorQueryStub,
                         query_text: str):
        """Parse set/unset command arguments

        Args:
            query_text: FIXME - add description

        """
        errmsg = ''
        find_method = skill_list = None
        match = self._re_find_statement.match(query_text)
        if match:
            find_method, skill_string = match.groups()
            skill_list = self._parse_skill_string(skill_string)
            print("DEBUG: find method ({}) and skills ({})".format(find_method, skill_list))
        else:
            errmsg = self._PARSE_ERROR

        if errmsg:
            print("ERROR: " + errmsg)
            return

        find_spec = skillitor_pb2.FindSpec(find_method=find_method,
                                           skill_list=skill_list)
        for sa in rpc_handle.FindSkills(find_spec):
            simple_skill_list = [(s.skill_name, s.skill_level) for s in sa.skills]
            print("Found user {} with skills {}".format(
                sa.user_email, simple_skill_list))

    def _parse_skill_string(self, skill_string) -> List[skillitor_pb2.SkillSpec]:
        """Split up a string with skills into (skill, level) tuples"""
        skills = []
        for skill_and_level in re.split(r'\s*,\s*', skill_string):
            skill_name, level = re.search(self._patterns['re_skill_and_level'],
                                     skill_and_level).groups()
            level = self._normalize_skill_level(level)
            skills.append(skillitor_pb2.SkillSpec(skill_name=skill_name, skill_level=level))
        return skills

    @staticmethod
    def _normalize_skill_level(level: str) -> SkillLevel:
        """Convert the skill level to an integer"""
        if level is None:
            return SkillLevel.UNDEFINED
        level = level.strip('/').lower()
        if level in [str(int(SkillLevel.BEGINNER)), 'b', 'beginner']:
            level = SkillLevel.BEGINNER
        elif level in [str(int(SkillLevel.INTERMEDIATE)), 'i', 'intermediate']:
            level = SkillLevel.INTERMEDIATE
        elif level in [str(int(SkillLevel.ADVANCED)), 'a', 'advanced']:
            level = SkillLevel.ADVANCED
        return level
