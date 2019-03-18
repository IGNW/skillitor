#!/usr/bin/env python3

from enum import IntEnum
from pprint import pprint, pformat
import re


class SkillLevel(IntEnum):
    UNDEFINED = 0
    BEGINNER = 1
    INTERMEDIATE = 2
    ADVANCED = 3


class QueryParser:
    _patterns = {
        're_skill_id': r"""[-.#+*\w\d]+""",
        're_beginner': r'{}|b|beginner'.format(SkillLevel.BEGINNER),
        're_intermediate': r'{}|i|intermediate'.format(SkillLevel.INTERMEDIATE),
        're_advanced': r'{}|a|advanced'.format(SkillLevel.ADVANCED),
    }
    _patterns['re_skill_level'] = r'\[(?:{re_beginner}|{re_intermediate}|{re_advanced})\]'.format(**_patterns)
    _patterns['re_skill_list'] = r"""
        (
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
        (set|unset)\ skills?\s+
        {re_skill_list}
        (?:for\ (\S+@\S+))?      # Optional email address for target user
    """.format(**_patterns), re.VERBOSE)

    _re_find_statement = re.compile(r"""
        (find|find-all|find-any)(?:\ skills?)?\s+
        {re_skill_list}
    """.format(**_patterns), re.VERBOSE)

    def parse_command(self, query_text: str):
        set_match = self._re_set_statement.search(query_text)
        find_match = self._re_find_statement.search(query_text)
        # print('Set pattern:' + str(self._re_set_statement.pattern))

        # TODO: Take the data that I've parsed out and build some kind of
        # message object that we'll use with gRPC.
        if set_match:
            print("Found set match")
            action, skill_string, email = set_match.groups()
            skills = self.parse_skill_string(skill_string)
            print("Action: {}, skills: {}, email: {}".format(
                action, pformat(skills), email))
        elif find_match:
            print("Found find match")
            action, skill_string = find_match.groups()
            skills = self.parse_skill_string(skill_string)
            print('Action: {}, skills: {}'.format(action, skills))
        else:
            print("No match :(")
            return None

    def parse_skill_string(self, skill_string):
        """Split up a string with skills into (skill, level) tuples"""
        skills = []
        for skill_and_level in re.split(r'\s*,\s*', skill_string):
            skill, level = re.search(self._patterns['re_skill_and_level'],
                                     skill_and_level).groups()
            level = self.normalize_skill_level(level)
            skills.append((skill, level))
        return skills

    @staticmethod
    def normalize_skill_level(level: str) -> SkillLevel:
        """Convert the skill level to an integer"""
        if level is None:
            return SkillLevel.UNDEFINED
        level = level.strip('[]').lower()
        if level in [str(int(SkillLevel.BEGINNER)), 'b', 'beginner']:
            level = SkillLevel.BEGINNER
        elif level in [str(int(SkillLevel.INTERMEDIATE)), 'i', 'intermediate']:
            level = SkillLevel.INTERMEDIATE
        elif level in [str(int(SkillLevel.ADVANCED)), 'a', 'advanced']:
            level = SkillLevel.ADVANCED
        return level
