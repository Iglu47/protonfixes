""" 神都不良探 Underdog Detective
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    util.protontricks('klite')
    util.set_environment('WINEDLLOVERRIDES', 'winegstreamer=')
    # it uses quartz instead of mfplat on win7
    util.protontricks('win7')
