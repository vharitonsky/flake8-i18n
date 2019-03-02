# -*- coding: utf-8 -*-

import ast
import unittest

from flake8_i18n import Flake8i18n


class TestFlake8i18n(unittest.TestCase):

    def test_fstring(self):
        tree = ast.parse("_(f'')")
        checker = Flake8i18n(tree)
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0][0], 1)
        self.assertEqual(ret[0][1], 0)

    def test_format_interp(self):
        tree = ast.parse("_('{}'.format('line'))")
        checker = Flake8i18n(tree)
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0][0], 1)
        self.assertEqual(ret[0][1], 0)

    def test_printf_interp(self):
        tree = ast.parse("_('%s' % 'line')")
        checker = Flake8i18n(tree)
        ret = list(checker.run())
        self.assertEqual(len(ret), 1)
        self.assertEqual(ret[0][0], 1)
        self.assertEqual(ret[0][1], 0)


if __name__ == '__main__':
    unittest.main()
