// Skillitor Query Language

grammar skillquery;

options {
    language='Python3';
}

skillquery
    : statement ';' skillquery+
    | statement ';'
    | statement
    ;

statement: action SKILL_TOKEN skill+ userid?;

action
    : SET
    | FORGET
    | FIND_ANY
    | FIND_ALL
    ;

skill
    : SKILL_ID skill_level? COMMA skill+
    | SKILL_ID skill_level? COMMA
    | SKILL_ID skill_level?
    | '\'' SKILL_ID+ '\''
    ;

skill_level
    : '[' SkillBeginner ']'
    | '[' SkillIntermediate ']'
    | '[' SkillAdvanced ']'
    ;

userid: FOR EMAIL;

GET: 'get';
SET: 'set';
FORGET: 'forget' | 'unset';
FOR: 'for';
COMMA: ',';
SKILL_TOKEN: 'skill' | 'skills';
FIND_ANY: 'find'|'find-any';
FIND_ALL: 'find-all';
SkillBeginner : 'beginner' | 'b' | '1';
SkillIntermediate : 'intermediate' | 'i' | '2';
SkillAdvanced : 'advanced' | 'a' | '3';
SPACING: ' '+;

fragment LOCAL_SUBPART : [-a-zA-Z0-9_~!$&'()*+,;=:]+;
fragment DOMAIN_SUBPART : [a-zA-Z0-9-]+;
EMAIL: LOCAL_SUBPART ('.' LOCAL_SUBPART)* '@' DOMAIN_SUBPART ('.' DOMAIN_SUBPART)*;

SKILL_ID: (ALPHANUM | SPECIAL_CHARS)+;
fragment ALPHANUM: [a-zA-Z0-9]+;
fragment SPECIAL_CHARS: [-.#+*];

WS : [ \t\n\r]+ -> skip ;
