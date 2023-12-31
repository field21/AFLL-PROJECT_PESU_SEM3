
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BREAK CASE COLON DEFAULT EQUAL GREATER IDENTIFIER LBRACE LESSER LPARA MINUS NUMERIC PLUS PRINT QUOTE RBRACE RPARA SEMICOLON STRING SWITCHdeclaration : SWITCH LPARA IDENTIFIER RPARA LBRACE cases RBRACEcases : case_break\n             | case_break cases\n             case_break : CASE NUMERIC COLON stae BREAK SEMICOLON\n                  | DEFAULT COLON stae BREAK SEMICOLON\n                  stae : IDENTIFIER EQUAL NUMERIC SEMICOLON\n            | IDENTIFIER EQUAL IDENTIFIER PLUS PLUS SEMICOLON \n            | IDENTIFIER PLUS PLUS SEMICOLON\n            | IDENTIFIER MINUS MINUS SEMICOLON\n            | stae stae stae\n            | print_statement\n    print_statement : PRINT LPARA QUOTE STRING QUOTE RPARA SEMICOLON\n                       | PRINT LPARA QUOTE IDENTIFIER QUOTE RPARA SEMICOLONempty :'
    
_lr_action_items = {'SWITCH':([0,],[2,]),'$end':([1,11,],[0,-1,]),'LPARA':([2,19,],[3,26,]),'IDENTIFIER':([3,14,15,16,18,20,21,23,28,34,37,38,39,45,48,49,],[4,17,17,17,-11,17,17,30,17,41,-6,-8,-9,-7,-12,-13,]),'RPARA':([4,43,44,],[5,46,47,]),'LBRACE':([5,],[6,]),'CASE':([6,8,29,35,],[9,9,-5,-4,]),'DEFAULT':([6,8,29,35,],[10,10,-5,-4,]),'RBRACE':([7,8,12,29,35,],[11,-2,-3,-5,-4,]),'NUMERIC':([9,23,],[13,31,]),'COLON':([10,13,],[14,15,]),'PRINT':([14,15,16,18,20,21,28,37,38,39,45,48,49,],[19,19,19,-11,19,19,19,-6,-8,-9,-7,-12,-13,]),'BREAK':([16,18,20,28,37,38,39,45,48,49,],[22,-11,27,-10,-6,-8,-9,-7,-12,-13,]),'EQUAL':([17,],[23,]),'PLUS':([17,24,30,36,],[24,32,36,42,]),'MINUS':([17,25,],[25,33,]),'SEMICOLON':([22,27,31,32,33,42,46,47,],[29,35,37,38,39,45,48,49,]),'QUOTE':([26,40,41,],[34,43,44,]),'STRING':([34,],[40,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'declaration':([0,],[1,]),'cases':([6,8,],[7,12,]),'case_break':([6,8,],[8,8,]),'stae':([14,15,16,20,21,28,],[16,20,21,21,28,28,]),'print_statement':([14,15,16,20,21,28,],[18,18,18,18,18,18,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> declaration","S'",1,None,None,None),
  ('declaration -> SWITCH LPARA IDENTIFIER RPARA LBRACE cases RBRACE','declaration',7,'p_declaration','switch_statement.py',223),
  ('cases -> case_break','cases',1,'p_cases','switch_statement.py',227),
  ('cases -> case_break cases','cases',2,'p_cases','switch_statement.py',228),
  ('case_break -> CASE NUMERIC COLON stae BREAK SEMICOLON','case_break',6,'p_case_break','switch_statement.py',233),
  ('case_break -> DEFAULT COLON stae BREAK SEMICOLON','case_break',5,'p_case_break','switch_statement.py',234),
  ('stae -> IDENTIFIER EQUAL NUMERIC SEMICOLON','stae',4,'p_stae','switch_statement.py',239),
  ('stae -> IDENTIFIER EQUAL IDENTIFIER PLUS PLUS SEMICOLON','stae',6,'p_stae','switch_statement.py',240),
  ('stae -> IDENTIFIER PLUS PLUS SEMICOLON','stae',4,'p_stae','switch_statement.py',241),
  ('stae -> IDENTIFIER MINUS MINUS SEMICOLON','stae',4,'p_stae','switch_statement.py',242),
  ('stae -> stae stae stae','stae',3,'p_stae','switch_statement.py',243),
  ('stae -> print_statement','stae',1,'p_stae','switch_statement.py',244),
  ('print_statement -> PRINT LPARA QUOTE STRING QUOTE RPARA SEMICOLON','print_statement',7,'p_print_statement','switch_statement.py',254),
  ('print_statement -> PRINT LPARA QUOTE IDENTIFIER QUOTE RPARA SEMICOLON','print_statement',7,'p_print_statement','switch_statement.py',255),
  ('empty -> <empty>','empty',0,'p_empty','switch_statement.py',259),
]
