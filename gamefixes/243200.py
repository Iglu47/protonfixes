""" The Dark Eye: Memoria
https://github.com/ValveSoftware/Proton/issues/1412
No cutscene audio in Daedalic Games (Memoria, The Night of the Rabbit, A New Beginning - Final Cut) (105000 230820 243200) #1412 
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    util.set_environment('WINEDLLOVERRIDES', 'xaudio2_7=d')
