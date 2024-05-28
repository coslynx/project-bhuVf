# user_reputation.py

class UserReputation:
    def __init__(self):
        self.reputation = {}

    def add_reputation(self, user_id, reputation_points):
        if user_id in self.reputation:
            self.reputation[user_id] += reputation_points
        else:
            self.reputation[user_id] = reputation_points

    def remove_reputation(self, user_id, reputation_points):
        if user_id in self.reputation:
            self.reputation[user_id] -= reputation_points
            if self.reputation[user_id] < 0:
                self.reputation[user_id] = 0

    def get_reputation(self, user_id):
        if user_id in self.reputation:
            return self.reputation[user_id]
        else:
            return 0

    def reset_reputation(self, user_id):
        if user_id in self.reputation:
            self.reputation[user_id] = 0

# End of user_reputation.py