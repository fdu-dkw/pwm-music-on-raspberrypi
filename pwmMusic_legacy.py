import RPi.GPIO as GPIO
import wiringpi

# ==========================CONSTANTS==========================
FREQ: dict[str, float] = {
    '': 0,
    'b3': 440*2**(-10/12),
    'c4': 440*2**(-9/12),
    'c_4': 440*2**(-8/12),
    'd4': 440*2**(-7/12),
    'd_4': 440*2**(-6/12),
    'e4': 440*2**(-5/12),
    'f4': 440*2**(-4/12),
    'f_4': 440*2**(-3/12),
    'g4': 440*2**(-2/12),
    'g_4': 440*2**(-1/12),
    'a4': 440,             # a4->440Hz
    'a_4': 880*2**(-11/12),
    'b4': 880*2**(-10/12),
    'c5': 880*2**(-9/12),
    'c_5': 880*2**(-8/12),
    'd5': 880*2**(-7/12),
    'd_5': 880*2**(-6/12),
    'e5': 880*2**(-5/12),
    'f5': 880*2**(-4/12),
    'f_5': 880*2**(-3/12),
    'g5': 880*2**(-2/12),
    'g_5': 880*2**(-1/12),
    'a5': 880,             # a5->880Hz
    'a_5': 1760*2**(-11/12),
    'b5': 1760*2**(-10/12),
    'c6': 1760*2**(-9/12),
    'c_6': 1760*2**(-8/12),
    'd6': 1760*2**(-7/12),
    'd_6': 1760*2**(-6/12),
    'e6': 1760*2**(-5/12),
    'f6': 1760*2**(-4/12),
    'f_6': 1760*2**(-3/12),
    'g6': 1760*2**(-2/12),
    'g_6': 1760*2**(-1/12),
    'a6': 1760,            # a6->1760Hz
    'a_6': 1760*2**(1/12),
    'b6': 1760*2**(2/12)
}
EA = 13
I2 = 19
I1 = 26
EB = 16
I4 = 20
I3 = 21
BPM = 120
US_PER_BEAT = 1000000 * 60 / BPM
INIT_FREQ = 0
DUTY = 50
HOLD = 0
# ==========================END OF CONSTANTS==========================


# ==========================INITALIZERS==========================
def set(*, ea=EA, i2=I2, i1=I1, eb=EB, i4=I4, i3=I3, bpm=BPM, init_freq=INIT_FREQ, duty=DUTY):
    global EA, I2, I1, EB, I4, I3, BPM, US_PER_BEAT, INIT_FREQ, DUTY
    EA, I2, I1, EB, I4, I3 = (ea, i2, i1, eb, i4, i3)
    BPM = bpm
    US_PER_BEAT = 1000000 * 60 / BPM
    INIT_FREQ = init_freq
    DUTY = duty
    global pwma, pwmb
    pwma, pwmb = init()


def reset():
    set(ea=13, i2=19, i1=26, eb=16, i4=20, i3=21, bpm=120, init_freq=880, duty=50)


def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup([EA, I2, I1, EB, I4, I3], GPIO.OUT)
    GPIO.output([EA, I2, EB, I3], GPIO.LOW)
    GPIO.output([I1, I4], GPIO.HIGH)
    pwma = GPIO.PWM(EA, INIT_FREQ)
    pwmb = GPIO.PWM(EB, INIT_FREQ)
    pwma.start(0)
    pwmb.start(0)
    pwma.ChangeDutyCycle(DUTY)
    # pwmb.ChangeDutyCycle(DUTY)
    pwmb.ChangeDutyCycle(0)
    return pwma, pwmb
# ==========================END OF INITALIZERS==========================


# ==========================METHODS==========================
def beep_no_rest(frequency, beats: float):
    pwma.ChangeFrequency(frequency)
    wiringpi.delayMicroseconds(int(US_PER_BEAT * beats))


def rest(beats: float):
    pwma.ChangeDutyCycle(0)
    wiringpi.delayMicroseconds(int(US_PER_BEAT * beats))
    pwma.ChangeDutyCycle(DUTY)


def beep(frequency, beats: float):
    if frequency == 0:
        rest(beats)
    else:
        beep_no_rest(frequency, beats * 7/8)
        rest(beats / 8)


def play_one_note(pitch: str, beats: float, have_rest=1):
    if (have_rest == 1):
        beep(adjust(FREQ[pitch]), beats)
    else:
        beep_no_rest(adjust(FREQ[pitch]), beats)


def play(section):
    for note in section:
        play_one_note(*note)
# ==========================END OF METHODS==========================


# ==========================ADJUSTMENT==========================
def adjust(frequency: float):
    return frequency**1.116
# ==========================END OF ADJUSTMENT==========================


pwma, pwmb = init()  # (important)

if __name__ == '__main__':  # for test
    # set()
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
