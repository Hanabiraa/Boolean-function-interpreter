import frontend.AST as AST

def match(tokens, token):
    if tokens[0].token_type == token:
        return tokens.pop(0)
    else:
        raise Exception('Invalid syntax on token {}'.format(tokens[0].token_type))


def parse_e(tokens):
    left_node = parse_e2(tokens)

    while tokens[0].token_type in [AST.TokenType.T_OR]:
        node = tokens.pop(0)
        node.children.append(left_node)
        node.children.append(parse_e2(tokens))
        left_node = node

    return left_node


def parse_e2(tokens):
    left_node = parse_e3(tokens)

    while tokens[0].token_type in [AST.TokenType.T_AND]:
        node = tokens.pop(0)
        node.children.append(left_node)
        node.children.append(parse_e3(tokens))
        left_node = node

    return left_node


def parse_e3(tokens):
    if tokens[0].token_type == AST.TokenType.T_BOOL:
        return tokens.pop(0)

    match(tokens, AST.TokenType.T_LPAR)
    expression = parse_e(tokens)
    match(tokens, AST.TokenType.T_RPAR)

    return expression
