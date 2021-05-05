# SublimeLinter-contrib-ts-standard

[![Build Status](https://travis-ci.com/sambauers/SublimeLinter-contrib-ts-standard.svg?branch=master)](https://travis-ci.com/github/sambauers/SublimeLinter-contrib-ts-standard)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter)
provides an interface to [ts-standard](https://www.npmjs.com/package/ts-standard).
It will be used with files that have the “typescript” syntax.

## Installation

SublimeLinter must be installed in order to use this plugin.

Please use [Package Control](https://packagecontrol.io) to install the linter
plugin.

Before installing this plugin, you must ensure that `ts-standard` is installed
on your system via NPM:

```sh
npm install -g ts-standard
```

In order for `ts-standard` to be executed by SublimeLinter, you must ensure that
its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings

- [SublimeLinter settings](http://sublimelinter.readthedocs.org/en/latest/settings.html)
- [Linter settings](http://sublimelinter.readthedocs.org/en/latest/linter_settings.html)
