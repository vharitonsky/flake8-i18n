.. -*- coding: utf-8 -*-

Flake8 i18n plugin
==========================
Way too often using gettext in python results in one of
the following errors:

_(f"{context_variable}")

Not only gettext will not work here because fstring interpolation
happens before function call, but using gettext tools for collecting
translation keys results in:

    File "/usr/lib/python3.6/site-packages/babel/messages/extract.py",

    line 480, in extract_python
    value = eval(code, {'__builtins__': {}}, {})

    File "<string>", line 2, in <module>
    NameError: name 'context_variable' is not defined

Similar cases are
    _("%s" % value)
and
    _("{}".format(value))

which will not trigger a collection error,
but will still result in an incorrect key name in gettext function call.

This flake8 extensions provides basic checks for the above cases.


Install
-------
Install with pip::

    $ pip install flake8-i18n

Configure
---------

Add following into your .flake8 file

    i18nfuncs =
        gettext
        ngettext
        myfunny_gettext
        _

Otherwise the default function name list is
    gettext
    ngettext
    _


Using string interpolation inside gettext will now result in one of the following:

    I001 fstring is resolved before function call

    I002 format is resolved before function call

    I003 printf is resolved before function call


Requirements
------------
- Python 3.6, 3.7
- flake8


License
-------
GNU General Public License v2 (GPLv2)
