from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants

class PlayerBot(Bot):

    def play_round(self):

        yield (views.Demographics, {
            'age': 24,
            'gender': 'Masculino'})

        # yield (views.CognitiveReflectionTest, {
        #     'crt_bat': 10,
        #     'crt_widget': 5,
        #     'crt_lake': 48
        # })

        for value in [
       #     self.player.crt_bat,
            self.player.payoff
        ]:
            assert value != None
