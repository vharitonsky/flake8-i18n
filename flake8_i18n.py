import ast

GETTEXT_FUNC_NAMES = ('_', 'gettext', 'ngettext')


def _is_fstring(node):
    return isinstance(node, ast.JoinedStr)


def _is_printf_format(node):
    return (
       isinstance(node, ast.BinOp) and
       isinstance(node.op, ast.Mod) and
       isinstance(node.left, ast.Str)
    )


def _is_gettext_call(node):
    return (
        isinstance(node, ast.Call) and
        isinstance(node.func, ast.Name) and
        node.func.id in GETTEXT_FUNC_NAMES
    )


def _is_format(node):
    return (
        isinstance(node, ast.Call) and
        isinstance(node.func, ast.Attribute) and
        isinstance(node.func.value, ast.Str) and
        node.func.attr == 'format'
    )


class Flake8i18n(object):
    name = 'flake8_i18n'
    version = '0.1.0'
    message_fstring = 'I001 fstring is resolved before function call'
    message_format_inter = 'I002 format is resolved before function call'
    message_printf_inter = 'I003 printf is resolved before function call'
    checks = None

    def __init__(self, tree):
        self.tree = tree

    @classmethod
    def parse_options(cls, options):
        if options.i18nfuncs:
            global GETTEXT_FUNC_NAMES
            GETTEXT_FUNC_NAMES = options.i18nfuncs

    @classmethod
    def add_options(cls, parser):
        parser.add_option(
            '--i18nfuncs',
            type='str',
            comma_separated_list=True,
            default=[],
            parse_from_config=True,
            help='A list of i18n func names.',
        )

    def run(self):
        for node in ast.walk(self.tree):
            if _is_gettext_call(node):
                if node.args and _is_fstring(node.args[0]):
                    yield (
                        node.lineno,
                        node.col_offset,
                        self.message_fstring,
                        type(self),
                    )
                elif node.args and _is_printf_format(node.args[0]):
                    yield (
                        node.lineno,
                        node.col_offset,
                        self.message_printf_inter,
                        type(self),
                    )
                elif node.args and _is_format(node.args[0]):
                    yield (
                        node.lineno,
                        node.col_offset,
                        self.message_format_inter,
                        type(self),
                    )
