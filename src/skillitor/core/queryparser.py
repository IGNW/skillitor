#!/usr/bin/env python3

import re


class QueryParser:
    SKILL_BEGINNER = 1
    SKILL_INTERMEDIATE = 2
    SKILL_ADVANCED = 3

    _fragments = {
        're_skill_id': r"""[-.#+*\w\d]+""",
        're_skill_level': r"""\[(?:1|b|beginner|2|i|intermediate|3|a|advanced)\]""",
    }
    _fragments['re_skill_list'] = r"""
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
    """.format(**_fragments)

    _re_set_statement = re.compile(r"""
        (set|unset)\ skills?\s+
        {re_skill_list}
        (?:for\ (\S+@\S+))?      # Optional email address for target user
    """.format(**_fragments), re.VERBOSE)

    _re_find_statement = re.compile(r"""
        (find|find-all|find-any)\ skills?\s+
        {re_skill_list}
    """.format(**_fragments), re.VERBOSE)

    def parse_command(self, query_text: str):
        print("The pattern I'm using is: " + str(self._re_set_statement.pattern))
        print('Input text: ' + query_text)

        m1 = self._re_set_statement.search(query_text)
        m2 = self._re_find_statement.search(query_text)
        if m1:
            print("Match!")
            print(m1.groups())
        elif m2:
            print("Match!")
            print(m2.groups())
        else:
            print("No match :(")
