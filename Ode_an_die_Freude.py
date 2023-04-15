# =================================================================
# [info]
#
# name       : Ode_an_die_Freude
# description: play Ode an die Freude by Ludwig van Beethoven
# platform   : RaspberryPi 4B+ (with Fudan University IES car kit)
# date       : 2023/4/14
# e-mail     : kwdeng22@m.fudan.edu.cn
# repository :https://github.com/fdu-dkw/pwm-music-on-raspberrypi
# -----------------------------------------------------------------
# [contributors]
#
# LIN Yin    | 2022 Computer Science & Technology| Fudan University
# DENG Kaiwen|         2022 Technological Science| Fudan University
# YU Jizhou  |         2022 Technological Science| Fudan University
# -----------------------------------------------------------------
# [N.B.]
#
# 1) Please read README.md before running relevant programs.
# 2) Make sure GPIO & L298N are correctly connected.
# 3) Tone test is advised before first use.
# 4) For a better effect, tuning is advised (use pwmTuna.py).
# =================================================================

import pwmMusic
from pwmMusic import HOLD

SECTION1 = [
    ['e5', 1], ['e5', 1], ['f5', 1], ['g5', 1],
    ['g5', 1], ['f5', 1], ['e5', 1], ['d5', 1],
    ['c5', 1], ['c5', 1], ['d5', 1], ['e5', 1],
    ['e5', 1.5], ['d5', .5], ['d5', 2]
]

SECTION2 = [
    ['d5', 1], ['d5', 1], ['e5', 1], ['c5', 1],
    ['d5', 1], ['e5', .5], ['f5', .5], ['e5', 1], ['c5', 1],
    ['d5', 1], ['e5', .5], ['f5', .5], ['e5', 1], ['d5', 1],
    ['c5', 1], ['d5', 1], ['g4', 2]
]

if __name__ == '__main__':
    print('Ode an die Freude ')

    pwmMusic.set(bpm=120, duty=10)
    pwmMusic.play(SECTION1)
    pwmMusic.play(SECTION1[:12] + [
        ['d5', 1.5], ['c5', .5], ['c5', 2]
    ])
    pwmMusic.play(SECTION2)
    pwmMusic.play([
        ['e5', 1, HOLD]
    ] + SECTION1[:12] + [
        ['d5', 1.5], ['c5', .5], ['c5', 2]
    ])
    pwmMusic.stop()

    print('Bravo!')
