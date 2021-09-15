def debug_func(raw_expr=None, word_tokens=None,
               semantic_tokens_lst=None, object_tokens_lst=None):
    """
    output all variables, which used for create AST

    :param raw_expr: str
    :param word_tokens: [[str]]
    :param semantic_tokens_list: [[str]]
    :param object_tokens: [[TokenType]]
    :return None
    """
    print('your expr: {}'.format(raw_expr),
          'simple tokens: {}'.format(word_tokens),
          'semantic tokens list: {}'.format(semantic_tokens_lst),
          'object tokens list: {}'.format(object_tokens_lst),
          sep='\n\n', end='\n')
