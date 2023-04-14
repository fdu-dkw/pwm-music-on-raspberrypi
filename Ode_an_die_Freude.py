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
