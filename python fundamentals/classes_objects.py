lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (5,9,12,3,1,21)
}

class LotteryPlayer:
    def __init__(self):
        """
        docstring
        """
        self.name = "Rolf"
        self.numbers = (5,9,12,3,1,21)

    def total(self):
        return sum(self.numbers)

player = LotteryPlayer()
print(player.name)
print(player.total())
