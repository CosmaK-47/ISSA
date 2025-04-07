import random
from tabulate import tabulate
import matplotlib.pyplot as plt

class ISSA:
    def __init__(self):
        self.history = []
        self.opponent_history = []
        self.defect_streak = 0
        self.total_defects = 0
        self.revenge_mode = False
        self.revenge_timer = 0

    def reset(self):
        self.history = []
        self.opponent_history = []
        self.defect_streak = 0
        self.total_defects = 0
        self.revenge_mode = False
        self.revenge_timer = 0

    def predict_opponent_next(self):
        if not self.opponent_history:
            return 'C'
        return self.opponent_history[-1]

    def simulate_future(self, my_next_move):
        opponent_pred = self.predict_opponent_next()

        if my_next_move == 'C' and opponent_pred == 'C':
            return 3
        elif my_next_move == 'C' and opponent_pred == 'D':
            return 0
        elif my_next_move == 'D' and opponent_pred == 'C':
            return 5
        else:
            return 1

    def move(self, opponent_last_move):
        # Update opponent history and stats
        if opponent_last_move is not None:
            self.opponent_history.append(opponent_last_move)
            if opponent_last_move == 'D':
                self.total_defects += 1
                self.defect_streak += 1
            else:
                self.defect_streak = 0  # Reset on cooperation

        # Activate revenge mode if betrayal streak too long
        if self.defect_streak >= 2 or self.total_defects >= 5:
            self.revenge_mode = True
            self.revenge_timer = 5  # Stay angry for 5 turns

        # Cooldown revenge
        if self.revenge_mode:
            if self.revenge_timer > 0:
                self.revenge_timer -= 1
            else:
                self.revenge_mode = False

        # First move
        if not self.opponent_history:
            self.history.append('C')
            return 'C'

        # If in revenge mode: defect no matter what
        if self.revenge_mode:
            self.history.append('D')
            return 'D'

        # Otherwise: simulate and be strategic
        score_if_coop = self.simulate_future('C')
        score_if_defect = self.simulate_future('D')

        if score_if_coop > score_if_defect:
            self.history.append('C')
            return 'C'
        else:
            self.history.append('D')
            return 'D'


