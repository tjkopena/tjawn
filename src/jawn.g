?start: file

file: _dict_inner

?value: null
      | true
      | false
      | number
      | string
      | text
      | list
      | set
      | dict

dict:               "{" _dict_inner "}"
_dict_inner:        (pair _SEP?)*
pair:               key _ASGN value
key:                QUOT_STR | BARE_STR

set:                "{" value (_SEP? value )* "}"
                  | "{" _EMPTYSET _SEP? "}"
_EMPTYSET.15:       "_"

list:               "[" (value _SEP?)* "]"

text:               TEXT
TEXT.40:            /\"\"\"/ _STRING_ESC_INNER /\"\"\"/
                  | /'''/    _STRING_ESC_INNER /'''/

string:             QUOT_STR | BARE_STR | URL
QUOT_STR.20:        /\"/ _STRING_ESC_INNER /\"/
                  | /'/  _STRING_ESC_INNER /'/
BARE_STR.10:        /[^\s"'{[}\]:=,]+/
URL.15:             /https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)/

number:             NUMBER
NUMBER.30:          /[+-]?\d+(\.\d+)?([eE][+-]?\d+)?(?=[\s,\]}]|$)/

NULL.50:            "null"i
null: NULL

TRUE.60:            "true"i
true: TRUE

FALSE.70:           "false"i
false: FALSE

_STRING_ESC_INNER:  _STRING_INNER /(?<!\\)(\\\\)*?/
_STRING_INNER:      /(.|\n)*?/

_ASGN:              ":" | "="
_SEP:               ","

%import common.SIGNED_NUMBER
%import common.WS
%ignore WS
