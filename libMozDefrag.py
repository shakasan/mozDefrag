#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
libMozDefrag 0.1
Author : Francois B (Makoto)
Licence : GPL3
"""

import subprocess


def mozDefragFirefox():  # Firefox defrag

    cmd2exec = "for f in ~/.mozilla/firefox/*/*.sqlite;"
    cmd2exec += "do sqlite3 $f 'VACUUM;';"
    cmd2exec += "done"
    cmdOutput = subprocess.check_output(cmd2exec,
                                        shell=True).decode("utf-8")
    return cmdOutput


def mozDefragThunderbird():  # Thunderbird defrag

    cmd2exec = "for f in ~/.thunderbird/*/*.sqlite;"
    cmd2exec += "do sqlite3 $f 'VACUUM;';"
    cmd2exec += "done"
    cmdOutput = str(subprocess.check_output(cmd2exec,
                                            shell=True).decode("utf-8"))
    return cmdOutput


def mozFirefoxIsInstalled():  # check if Firefox is installed

    cmd2exec = "if which firefox >/dev/null;"
    cmd2exec += "then echo 1;"
    cmd2exec += "else echo 0;"
    cmd2exec += "fi"
    cmdOutput = int(subprocess.check_output(cmd2exec,
                                            shell=True).decode("utf-8"))
    return 1 if (cmdOutput > 0) else 0


def mozThunderbirdIsInstalled():  # check if Thunderbird is installed

    cmd2exec = "if which thunderbird >/dev/null;"
    cmd2exec += "then echo 1;"
    cmd2exec += "else echo 0;"
    cmd2exec += "fi"
    cmdOutput = int(subprocess.check_output(cmd2exec,
                                            shell=True).decode("utf-8"))
    return 1 if (cmdOutput > 0) else 0


def mozFirefoxIsRunning():  # check if Firefox is running

    cmd2exec = "ps auxw | grep -i firefox | grep -v grep | wc -l"
    cmdOutput = int(subprocess.check_output(cmd2exec,
                                            shell=True).decode("utf-8"))
    return 1 if (cmdOutput > 0) else 0


def mozThunderbirdIsRunning():  # check if Thunderbird is running

    cmd2exec = "ps auxw | grep -i thunderbird | grep -v grep | wc -l"
    cmdOutput = int(subprocess.check_output(cmd2exec,
                                            shell=True).decode("utf-8"))
    return 1 if (cmdOutput > 0) else 0
