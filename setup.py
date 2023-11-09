#!/usr/bin/env python

## NOTE: ##
## this setup.py was generated by zero2pypi:
## http://gfxmonk.net/dist/0install/zero2pypi.xml

from setuptools import *
setup(
	packages = find_packages(exclude=['test', 'test.*']),
	name='python-termstyle',
	url='http://gfxmonk.net/dist/0install/python-termstyle.xml',
	description='console colouring for python',
	py_modules=['termstyle'],
	install_requires=['setuptools'],
	version='0.1.10',
	long_description='\n**Note**: This package has been built automatically by\n`zero2pypi <http://gfxmonk.net/dist/0install/zero2pypi.xml>`_.\nIf possible, you should use the zero-install feed instead:\nhttp://gfxmonk.net/dist/0install/python-termstyle.xml\n\n----------------\n\n=========\ntermstyle\n=========\n\ntermstyle is a simple python library for adding coloured output to\nterminal (console) programs.  The definitions come from ECMA-048_, the\n"Control Functions for Coded Character Sets" standard.\n\nInstallation:\n-------------\n\nI thoroughly recommend using the zero-install feed (see the project homepage) to manage your dependencies if at all possible. zero-install_ provides a much better system than pip or easy_install, and works with absolutely any language and allows decentralised package management that requires no special privileges to install.\n\nExample Usage:\n--------------\n::\n\n\tfrom termstyle import *\n\tprint "%s:%s" % (red(\'Hey\'), green(\'how are you?\'))\n\tprint blue(\'How \', bold(\'you\'), \' doin?\')\n\nor, you can use a colour just as a string::\n\n\tprint "%sBlue!%s" % (blue, reset)\n\nStyles:\n-------\n::\n\n\treset or default (no colour / style)\n\ncolour::\n\n\tblack\n\tred\n\tgreen\n\tyellow\n\tblue\n\tmagenta\n\tcyan\n\twhite\n\nbackground colour::\n\n\tbg_black\n\tbg_red\n\tbg_green\n\tbg_yellow\n\tbg_blue\n\tbg_magenta\n\tbg_cyan\n\tbg_white\n\tbg_default\n\nIn terminals supporting transparency ``bg_default`` is often used to set\nthe background to transparent [#]_.\n\nweight::\n\n\tbold\n\tinverted\n\nstyle::\n\n\titalic\n\tunderscore\n\nControls:\n---------\n::\n\n\tauto() - sets colouring on only if sys.stdout is a terminal\n\tdisabe() - disable colours\n\tenable() - enable colours\n\n.. [#] Supporting terminals include rxvt-unicode_, and Eterm_.\n\n.. _ECMA-048: http://www.ecma-international.org/publications/files/ECMA-ST/Ecma-048.pdf\n.. _rxvt-unicode: http://software.schmorp.de/\n.. _Eterm: http://www.eterm.org/\n.. _zero-install: http://0install.net/\n',
classifiers=[
		"License :: OSI Approved :: BSD License",
		"Programming Language :: Python",
		"Programming Language :: Python :: 3",
		"Intended Audience :: Developers",
		"Topic :: Software Development :: Libraries :: Python Modules",
	],
	keywords='output colour console ansi',
	license='BSD',
)
