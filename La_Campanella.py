# =================================================================
# [info]
#
# name       : La_Campanella
# description: play part of La Cambanella of Liszt Ferenc
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
    ['f_5', 1/2, HOLD],
    ['f_6', 1/2], ['f_6', 1/2], ['e6', 1/2],
    ['d6', 1/2], ['d6', 1/2], ['c_6', 7/16, HOLD], ['b5', 1/32, HOLD], ['c_6', 1/32, HOLD],
    ['b5', 1/2], ['a_5', 1/2], ['b5', 1/2],
    ['c_6', 1/2, HOLD], ['f_5', 1/2], ['f_5', 7/16, HOLD], ['g5', 1/32, HOLD], ['a5', 1/32, HOLD],
    ['g5', 1/2], ['f_5', 1/2], ['e5', 1/2],
    ['d5', 1/2], ['c_5', 1/2], ['b4', 7/16, HOLD], ['d5', 1/32, HOLD], ['e5', 1/32, HOLD],
    ['d5', 1/2], ['c_5', 1/2], ['b4', 1/2],
    ['f_4', 1]
]

SECTION2 = [
    ['f_5', 1/2, HOLD],
    ['f_6', 1/2], ['f_6', 1/2], ['e6', 7/16, HOLD], ['d6', 1/32, HOLD], ['e6', 1/32, HOLD],
] + SECTION1[4:20] + [
    ['f_5', 1/2], ['b5', 1/4], ['d6', 1/4], ['f_6', 1/2],
    ['f_5', 1/2], ['a_5', 1/4], ['c_6', 1/4], ['f_6', 1/2],
    ['b4', 1]
]

if __name__ == '__main__':
    print('La Campanella')

    pwmMusic.set(bpm=94, duty=10)
    pwmMusic.play(SECTION1)
    pwmMusic.play(SECTION2)
    pwmMusic.play(SECTION1)
    pwmMusic.play(SECTION2)
    pwmMusic.stop()

    print('Bravo!')
