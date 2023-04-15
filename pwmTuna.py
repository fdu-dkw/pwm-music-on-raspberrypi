# =================================================================
# [info]
#
# name       : pwmTuna
# description: Tune it
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

if __name__ == '__main__':

    # To determine exact vibrating frequency
    while True:
        freq = input('freq=')
        if freq == 'q':
            pwmMusic.stop()
            exit()
        pwmMusic.beep_no_rest(eval(freq), 1)

    # # To test highest outputable frequency
    # # (~256kHz for software PWM)
    # pwmMusic.set(duty=40)
    # pwmMusic.beep_no_rest(2000, 1)
    # pwmMusic.beep_no_rest(4000, 1)
    # pwmMusic.beep_no_rest(8000, 1)
    # pwmMusic.beep_no_rest(16000, 1)
    # pwmMusic.beep_no_rest(32000, 1)
    # pwmMusic.beep_no_rest(64000, 1)
    # pwmMusic.beep_no_rest(128000, 1)
    # pwmMusic.beep_no_rest(256000, 1)
    # pwmMusic.beep_no_rest(512000, 1)
    # pwmMusic.beep_no_rest(1024000, 1)
    # pwmMusic.stop()
