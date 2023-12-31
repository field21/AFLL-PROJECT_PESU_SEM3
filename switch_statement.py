# import ply.yacc as yacc
# import ply.lex as lex


# # Define the tokens
# tokens = (
#     'LBRACE',
#     'RBRACE',
#     'IDENTIFIER',
#     'SEMICOLON',
#     'RPARA',
#     'LPARA',
#     'GREATER',
#     'LESSER',
#     'EQUAL',
#     'NUMERIC',
#     'PRINT',
#     'COLON',
#     'SWITCH',
#     'CASE',
#     'BREAK',
#     'DEFAULT',
#     'PLUS',
#     'MINUS',
#     'STRING',
#     'QUOTE'
# )


# # Define token regular expressions
# t_ignore = ' \t'

# def t_SWITCH(t):
#     r'switch'
#     return t

# def t_newline(t):
#     r'\n+'
#     t.lexer.lineno += t.value.count("\n")

# def t_DEFAULT(t):
#     r'default'
#     return t

# def t_BREAK(t):
#     r'break'
#     return t
# def t_CASE(t):
#     r'case'
#     return t
# def t_PRINT(t):
#     r'printf'
#     return t

# t_PLUS= r'\+'
# t_MINUS=r'\-'
# t_COLON=r'\:'
# t_SEMICOLON = r'\;'
# t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
# t_LBRACE=r'\{'
# t_RBRACE=r'\}'
# t_LPARA=r'\('
# t_RPARA=r'\)'
# t_GREATER=r'\>'
# t_LESSER=r'\<'
# t_EQUAL=r'\='
# t_NUMERIC=r'[0-9_]+'
# t_STRING=r'[a-zA-Z_]+'
# t_QUOTE=r'\"'
# # Error handling
# def t_error(t):
#     print(f"Illegal character: {t.value[0]}")
#     t.lexer.skip(1)

# def p_declaration(p):
#     '''declaration : SWITCH LPARA IDENTIFIER RPARA LBRACE cases RBRACE'''
#     p[0] = f'switch {p[3]}:\n{p[6]}'

# def p_cases(p):
#     '''cases : case_break
#              | case_break cases
#              '''
#     p[0] = ' '.join(p[1:])

# def p_case_break(p):
#     '''case_break : CASE NUMERIC COLON stae SEMICOLON BREAK SEMICOLON
#                   | DEFAULT COLON stae BREAK SEMICOLON
#                   '''
#     p[0] = f'if {p[1]} {p[2]} {p[3]}: break'

# def p_stae(p):
#     '''stae : IDENTIFIER EQUAL NUMERIC SEMICOLON
#             | IDENTIFIER EQUAL IDENTIFIER PLUS PLUS SEMICOLON 
#             | IDENTIFIER PLUS PLUS SEMICOLON
#             | IDENTIFIER MINUS MINUS SEMICOLON
#             | stae stae stae
#             | print_statement
#     '''
#     if len(p) == 2:
#         p[0] = f'{p[1]}'
#     elif len(p) == 4:
#         p[0] = f'{p[1]} {p[2]} {p[3]}'
#     else:
#         p[0] = f'{p[1]} {p[2]} {p[3]}:\n{p[4]}'

# def p_print_statement(p):
#     '''print_statement : PRINT LPARA QUOTE STRING QUOTE RPARA SEMICOLON
#                        | PRINT LPARA QUOTE IDENTIFIER QUOTE RPARA SEMICOLON'''
#     p[0] = f'print({p[4]})'



# def p_empty(p):
#     'empty :'
#     pass


# # Error rule for syntax errors
# def p_error(p):
#     print("Invalid statement.")


# # Build the lexer and parser
# lexer = lex.lex()
# parser = yacc.yacc()


# # Get user input
# input_text = input("Enter an switch statement: ")
# #input_text ="switch (x){case 1:;break; default:;break;}"

# lexer.input(input_text)
# for token in lexer:
#       print(token)
# parser.parse(input_text)




# result = parser.parse(input_text, lexer=lexer)
# if result:
#     print("code generated")
#     print("valid statement")
# else:
#     print("invalid statement")
import ply.yacc as yacc
import ply.lex as lex

# Define the tokens
tokens = (
    'LBRACE',
    'RBRACE',
    'IDENTIFIER',
    'SEMICOLON',
    'RPARA',
    'LPARA',
    'GREATER',
    'LESSER',
    'EQUAL',
    'NUMERIC',
    'PRINT',
    'COLON',
    'SWITCH',
    'CASE',
    'BREAK',
    'DEFAULT',
    'PLUS',
    'MINUS',
    'STRING',
    'QUOTE'
)

# Define token regular expressions
t_ignore = ' \t'

def t_SWITCH(t):
    r'switch'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_DEFAULT(t):
    r'default'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_CASE(t):
    r'case'
    return t

def t_PRINT(t):
    r'printf'
    return t

t_PLUS= r'\+'
t_MINUS=r'\-'
t_COLON=r'\:'
t_SEMICOLON = r'\;'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LBRACE=r'\{'
t_RBRACE=r'\}'
t_LPARA=r'\('
t_RPARA=r'\)'
t_GREATER=r'\>'
t_LESSER=r'\<'
t_EQUAL=r'\='
t_NUMERIC=r'[0-9_]+'
t_STRING=r'[a-zA-Z_]+'
t_QUOTE=r'\"'

# Error handling
def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)

# Define the grammar rules
def p_declaration(p):
    '''declaration : SWITCH LPARA IDENTIFIER RPARA LBRACE cases RBRACE'''
    p[0] = f'switch {p[3]}:\n{p[6]}'

def p_cases(p):
    '''cases : case_break
             | case_break cases
             '''
    p[0] = ' '.join(p[1:])

def p_case_break(p):
    '''case_break : CASE NUMERIC COLON stae BREAK SEMICOLON
                  | DEFAULT COLON stae BREAK SEMICOLON
                  '''
    p[0] = f'if {p[1]} {p[2]} {p[3]}: break'

def p_stae(p):
    '''stae : IDENTIFIER EQUAL NUMERIC SEMICOLON
            | IDENTIFIER EQUAL IDENTIFIER PLUS PLUS SEMICOLON 
            | IDENTIFIER PLUS PLUS SEMICOLON
            | IDENTIFIER MINUS MINUS SEMICOLON
            | stae stae stae
            | print_statement
    '''
    if len(p) == 2:
        p[0] = f'{p[1]}'
    elif len(p) == 4:
        p[0] = f'{p[1]} {p[2]} {p[3]}'
    else:
        p[0] = f'{p[1]} {p[2]} {p[3]}:\n{p[4]}'

def p_print_statement(p):
    '''print_statement : PRINT LPARA QUOTE STRING QUOTE RPARA SEMICOLON
                       | PRINT LPARA QUOTE IDENTIFIER QUOTE RPARA SEMICOLON'''
    p[0] = f'print({p[4]})'

def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    print("Invalid statement.")

# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

# Get user input
input_text = input("Enter a switch statement: ")

lexer.input(input_text)
for token in lexer:
      print(token)

result = parser.parse(input_text, lexer=lexer)
if result:
    print("code generated")
    print("valid statement")
else:
    print("invalid statement")
