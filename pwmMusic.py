# =================================================================
# [info]
#
# module name: pwmMusic
# description: Turn your IES car into an instrument!
# platform   : RaspberryPi 4B+ (with Fudan University IES car kit)
# version    : 0.4
# date       : 2023/4/14
# e-mail     : kwdeng22@m.fudan.edu.cn
# -----------------------------------------------------------------
# [contributors]
#
# LIN Yin    | 2022 Computer Science & Technology| Fudan University
# DENG Kaiwen|         2022 Technological Science| Fudan University
# YU Jizhou  |         2022 Technological Science| Fudan University
# -----------------------------------------------------------------
# [N.B.]
#
# 1) Please read readme.md before running relevant programs.
# 2) Make sure GPIO & L298N are correctly connected.
# 3) for a better effect, tuning is advised (use pwmTuna.py).
# 4) usage:
# |import pwmMusic
# |from pwmMusic impoort HOLD
# =================================================================

import RPi.GPIO as GPIO
import wiringpi

# ==========================CONSTANTS==========================
FREQ = {
    #  | pitch | frequency | theoretical frequency (not exact; Idk why...) |
    'c4':   277,               # 440*2**(-9/12),
    'c_4':  293,               # 440*2**(-8/12),
    'd4':   310,               # 440*2**(-7/12),
    'd_4':  329,               # 440*2**(-6/12),
    'e4':   352,               # 440*2**(-5/12),
    'f4':   374,               # 440*2**(-4/12),
    'f_4':  399,               # 440*2**(-3/12),
    'g4':   420,               # 440*2**(-2/12),
    'g_4':  445,               # 440*2**(-1/12),
    'a4':   480,               # 440,
    'a_4':  510,               # 880*2**(-11/12),
    'b4':   541,               # 880*2**(-10/12),
    'c5':   575,               # 880*2**(-9/12),
    'c_5':  615,               # 880*2**(-8/12),
    'd5':   655,               # 880*2**(-7/12),
    'd_5':  700,               # 880*2**(-6/12),
    'e5':   745,               # 880*2**(-5/12),
    'f5':   795,               # 880*2**(-4/12),
    'f_5':  850,               # 880*2**(-3/12),
    'g5':   905,               # 880*2**(-2/12),
    'g_5':  970,               # 880*2**(-1/12),
    'a5':   1035,              # 880,
    'a_5':  1105,              # 1760*2**(-11/12),
    'b5':   1180,              # 1760*2**(-10/12),
    'c6':   1265,              # 1760*2**(-9/12),
    'c_6':  1355,              # 1760*2**(-8/12),
    'd6':   1460,              # 1760*2**(-7/12),
    'd_6':  1560,              # 1760*2**(-6/12),
    'e6':   1690,              # 1760*2**(-5/12),
    'f6':   1820,              # 1760*2**(-4/12),
    'f_6':  1960,              # 1760*2**(-3/12),
    'g6':   2120,              # 1760*2**(-2/12),
    'g_6':  2290,              # 1760*2**(-1/12),
    'a6':   2500,              # 1760,
    'a_6':  2700,              # 1760*2**(1/12),
    'b6':   2930,              # 1760*2**(2/12),

    '':     0,  # for rest
}
EA = 13  # GPIO connecting ENA
I2 = 19  # GPIO connecting IN2
I1 = 26  # GPIO connecting IN1
EB = 16  # GPIO connecting ENB
I4 = 20  # GPIO connecting IN4
I3 = 21  # GPIO connecting IN3
BPM = 60                          # pace
US_PER_BEAT = 1000000 * 60 / BPM  # microseconds per beat
INIT_FREQ = FREQ['b6']            # (just default value)
DUTY = 10                         # (just default value)
HOLD = 0                          # e.g. ['a5', 1, HOLD]
# ==========================END OF CONSTANTS==========================


# ==========================INITALIZERS==========================
def set(*, ea=EA, i2=I2, i1=I1, eb=EB, i4=I4, i3=I3, bpm=BPM, init_freq=INIT_FREQ, duty=DUTY):
    global EA, I2, I1, EB, I4, I3, BPM, US_PER_BEAT, INIT_FREQ, DUTY, pwma, pwmb
    BPM = bpm
    US_PER_BEAT = 1000000 * 60 / BPM
    INIT_FREQ = init_freq
    DUTY = duty
    if (EA, I2, I1, EB, I4, I3) != (ea, i2, i1, eb, i4, i3):
        stop()
        EA, I2, I1, EB, I4, I3 = (ea, i2, i1, eb, i4, i3)
        pwma, pwmb = init()


def reset():
    set(ea=13, i2=19, i1=26, eb=16, i4=20, i3=21, bpm=120, init_freq=FREQ['b6'], duty=10)


def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup([EA, I2, I1, EB, I4, I3], GPIO.OUT)
    GPIO.output([EA, I2, EB, I3], GPIO.LOW)
    GPIO.output([I1, I4], GPIO.HIGH)
    pwma = GPIO.PWM(EA, INIT_FREQ)
    pwmb = GPIO.PWM(EB, INIT_FREQ)
    pwma.start(0)
    pwmb.start(0)
    return pwma, pwmb
# ==========================END OF INITALIZERS==========================


# ==========================METHODS==========================
def beep_no_rest(frequency, beats: float):
    pwma.ChangeDutyCycle(DUTY)
    pwmb.ChangeDutyCycle(DUTY)
    pwma.ChangeFrequency(frequency)
    pwmb.ChangeFrequency(frequency)
    wiringpi.delayMicroseconds(int(US_PER_BEAT * beats))
    pwma.ChangeDutyCycle(0)
    pwmb.ChangeDutyCycle(0)


def rest(beats: float):
    pwma.ChangeDutyCycle(0)
    pwmb.ChangeDutyCycle(0)
    wiringpi.delayMicroseconds(int(US_PER_BEAT * beats))
    pwma.ChangeDutyCycle(DUTY)
    pwmb.ChangeDutyCycle(DUTY)


def beep(frequency, beats: float):
    if frequency == 0:
        rest(beats)
    else:
        beep_no_rest(frequency, beats * 7/8)
        rest(beats / 8)


def play_one_note(pitch: str, beats: float, have_rest=1):
    if (have_rest == 1):
        beep((FREQ[pitch]), beats)
    else:
        beep_no_rest((FREQ[pitch]), beats)


def play(section):
    for note in section:
        play_one_note(*note)


def stop():
    pwma.stop()
    pwmb.stop()
    GPIO.cleanup()
    GPIO.setwarnings(True)
# ==========================END OF METHODS==========================


GPIO.setwarnings(False)
GPIO.cleanup()
pwma, pwmb = init()  # (important)

if __name__ == '__main__':  # for test
    # set(bpm=1000)  # run this line if you want to hear a sound like blaster shooting
    play([
        ['c4', 1], ['c4', .25], ['c4', .25], ['c4', .25], ['c4', .25],
        ['d4', 1], ['d4', .25], ['d4', .25], ['d4', .25], ['d4', .25],
        ['e4', 1], ['e4', .25], ['e4', .25], ['e4', .25], ['e4', .25],
        ['f4', 1], ['f4', .25], ['f4', .25], ['f4', .25], ['f4', .25],
        ['g4', 1], ['g4', .25], ['g4', .25], ['g4', .25], ['g4', .25],
        ['a4', 1], ['a4', .25], ['a4', .25], ['a4', .25], ['a4', .25],
        ['b4', 1], ['b4', .25], ['b4', .25], ['b4', .25], ['b4', .25],

        ['c5', 1], ['c5', .25], ['c5', .25], ['c5', .25], ['c5', .25],
        ['d5', 1], ['d5', .25], ['d5', .25], ['d5', .25], ['d5', .25],
        ['e5', 1], ['e5', .25], ['e5', .25], ['e5', .25], ['e5', .25],
        ['f5', 1], ['f5', .25], ['f5', .25], ['f5', .25], ['f5', .25],
        ['g5', 1], ['g5', .25], ['g5', .25], ['g5', .25], ['g5', .25],
        ['a5', 1], ['a5', .25], ['a5', .25], ['a5', .25], ['a5', .25],
        ['b5', 1], ['b5', .25], ['b5', .25], ['b5', .25], ['b5', .25],

        ['c6', 1], ['c6', .25], ['c6', .25], ['c6', .25], ['c6', .25],
        ['d6', 1], ['d6', .25], ['d6', .25], ['d6', .25], ['d6', .25],
        ['e6', 1], ['e6', .25], ['e6', .25], ['e6', .25], ['e6', .25],
        ['f6', 1], ['f6', .25], ['f6', .25], ['f6', .25], ['f6', .25],
        ['g6', 1], ['g6', .25], ['g6', .25], ['g6', .25], ['g6', .25],
        ['a6', 1], ['a6', .25], ['a6', .25], ['a6', .25], ['a6', .25],
        ['b6', 1], ['b6', .25], ['b6', .25], ['b6', .25], ['b6', .25],
    ])
    stop()
