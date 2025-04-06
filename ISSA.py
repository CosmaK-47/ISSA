class ISSA:
    def __init__(self):
        self.history = []
        self.opponent_history = []
        self.defect_count = 0
        self.forgiven = False

    def reset(self):
        self.__init__()

    def predict_opponent_next(self):
        # Naive prediction: opponent repeats last move
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
        if opponent_last_move is not None:
            self.opponent_history.append(opponent_last_move)
            if opponent_last_move == 'D':
                self.defect_count += 1

        # First move
        if not self.opponent_history:
            self.history.append('C')
            return 'C'

        # Predict if forgiveness gives better expected score
        score_if_coop = self.simulate_future('C')
        score_if_defect = self.simulate_future('D')

        if score_if_coop > score_if_defect:
            self.history.append('C')
            return 'C'  # strategic forgiveness
        else:
            self.history.append('D')
            return 'D'

