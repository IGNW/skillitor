#!/usr/bin/env python3

from pprint import pprint, pformat
import re
from typing import List, Tuple

from .skills import SkillLevel, SkillSpec


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

    def process_set_cmd(self, query_text: str) -> str:
        """Parse set/unset command arguments"""
        errmsg = ''
        match = self._re_set_statement.match(query_text)
        if match:
            skill_string, email = match.groups()
            skills = self._parse_skill_string(skill_string)
            print("DEBUG: Got email ({}) and skills ({})".format(email, skills))
            # TODO: Store data in the database.
        else:
            errmsg = self._PARSE_ERROR
        return errmsg

    def process_find_cmd(self, query_text: str) -> Tuple[str, dict]:
        errmsg = ''
        match = self._re_find_statement.match(query_text)
        if match:
            find_method, skill_string = match.groups()
            skills = self._parse_skill_string(skill_string)
            print("DEBUG: Got find method ({}) and skills ({})".format(find_method, skills))
            # TODO: Query the database and return results
        else:
            errmsg = self._PARSE_ERROR

        # TODO: The second return type should probably be a skills.SkillAssociation
        return errmsg, {}

    def _parse_skill_string(self, skill_string) -> List[SkillSpec]:
        """Split up a string with skills into (skill, level) tuples"""
        skills = []
        for skill_and_level in re.split(r'\s*,\s*', skill_string):
            skill, level = re.search(self._patterns['re_skill_and_level'],
                                     skill_and_level).groups()
            level = self._normalize_skill_level(level)
            skills.append(SkillSpec(skill, level))
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
