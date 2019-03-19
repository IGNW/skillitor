from enum import IntEnum
from typing import List


class SkillLevel(IntEnum):
    UNDEFINED = 0
    BEGINNER = 1
    INTERMEDIATE = 2
    ADVANCED = 3


class SkillSpec:
    def __init__(self, skill_name: str, skill_level: SkillLevel):
        self.skill_name = skill_name
        self.skill_level = skill_level

    def __str__(self):
        return "{}/{}".format(self.skill_name, self.skill_level)

    def __repr__(self):
        return self.__str__()


class SkillAssociation:
    def __init__(self, email: str, skills: List[SkillSpec]):
        self.email = email
        self.skills = skills

    def __str__(self):
        skill_string = ', '.join(map(str, self.skills))
        return "{} => {}".format(self.email, skill_string)
