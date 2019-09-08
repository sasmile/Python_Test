import curses
from random import randrange,choice
from collections import defaultdict

actions = ['Up','Left','Down','Right','Restart','Exit']
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']

actions_dict = dict(zip(letter_codes,actions*2))

def main(stdscr):
    def init():
        return 'game'
    def not_game(state):
        responses = defaultdict(lambda :state)
        responses['Restart'],responses['Exit'] = 'Init','Exit'
        return responses[action]
    def game():
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'

            if 游戏胜利了:
                return 'Win'
            if 游戏失败了:
                return 'Gameover'
        return 'Game'
    state_actions = {
        'Init':init,
        'Win' :lambda :not_game('Win'),
        'Gameover':lambda :not_game('Gameover'),
        'Game':game
    }
    state = 'Init'

    while state != 'Exit':
        state = state_actions[state]()

    def get_user_action(keyboard):
        char = 'N'
        while char not in actions_dict:
            char = keyboard.getch()
        return actions_dict[char]
    def transpose(field):
        return [list(row) for row in zip(*field)]
    def invert(field):
        return [row[::-1] for row in field]

class GameField(object):
    def __init__(self,width=4,height=4,win=2048):
        self.width = width
        self.height = height
        self.win_value = 2048
        self.score = 0
        self.heighscore = 0
        self.reset()

