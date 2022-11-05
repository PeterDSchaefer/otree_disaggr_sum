from otree.api import *
import csv, random
author ="Peter Schaefer"

doc = """
This app is a budgeting task.
"""

class C(BaseConstants):
    NAME_IN_URL = 'reporting'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 2
    FIXED_PAY_MANAGER = 150
    FIXED_PAY_OWNER = 100
    CONVERSION_RATE = 25
    MIN_COMP = 125
    #with open("reporting/values.csv", encoding = "utf-8") as file:
    #    values = list(csv.DictReader(file))
    myFile = open('reporting/values.csv', 'r')
    reader = csv.DictReader(myFile)
    values = list()
    for dictionary in reader:
        values.append(dictionary)

class Subsession(BaseSubsession):
    pass

def creating_session(subsession: Subsession):
    subsession.group_randomly(fixed_id_in_group=True)
    for p in subsession.get_players():
        if p.round_number == 1:
            p.participant.payment_roundno = random.randint(1, C.NUM_ROUNDS)
            p.participant.lottery_round_no = random.randint(0, C.NUM_ROUNDS)
            print(p.participant.payment_roundno)
            if p.id_in_group == 2:
                print(p.participant.lottery_round_no)
        if p.round_number == p.participant.payment_roundno:
            p.payment_round = 1
        else:
            p.payment_round = 0
        if p.participant.lottery_round_no == 0:
            p.participant.lottery_won = 1
        if p.session.config['aggregated_planning']:
            if p.session.config['aggregated_reporting']:
                p.treatment = 1
                p.participant.treatment = 1
        else:
            if p.session.config['aggregated_reporting']:
                p.treatment = 2
                p.participant.treatment = 2
            else:
                p.treatment = 3
                p.participant.treatment = 3
                print(p.participant.treatment)
        # Treatment is 1 if planning and reporting is aggregated; it is 2 if planning is disaggregated, but reporting is aggregated;
        # it is 3 if planning and reporting is disaggregated

class Group(BaseGroup):
    report = models.IntegerField()
    guess = models.IntegerField()
    market_size = models.IntegerField()
    market_share = models.IntegerField()
    price = models.IntegerField()

class Player(BasePlayer):
    treatment = models.IntegerField()
    move_total = models.IntegerField()
    share_move_total = models.IntegerField()
    size_move_total = models.IntegerField()
    price_move_total = models.IntegerField()
    payment_round = models.BooleanField()
    #lottery_round = models.BooleanField()

# PAGES
class Welcome(Page):
    def is_displayed(player):
        return player.round_number == 1

class Setting_overview(Page):
    form_model='player'
    def is_displayed(player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player, timeout_happened):
        if player.round_number == 1:
            if player.id_in_group==1:
                player.participant.role=1
            else:
                player.participant.role=2

class Setting_payoffs(Page):
    form_model='player'
    def is_displayed(player):
        return player.round_number == 1

class Setting_distribution(Page):
    form_model='player'
    def is_displayed(player):
        return player.round_number == 1


class Setting(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player, timeout_happened):
        # If this is the first round, draw a round for the payout
        if player.round_number == 1:
            initial = random.randint(1, 10)

class Questions(Page):
    def is_displayed(player):
        return player.round_number==1

class Report(Page):
    form_model = 'group'
    form_fields = ['report', 'market_size', 'market_share', 'price']

    def vars_for_template(player: Player):
        group = player.group
        player.move_total = 0
        player.share_move_total = 0
        player.size_move_total = 0
        player.price_move_total = 0

        #Check whether the current round is the round for payout

        print(C.values[round(player.round_number)-1])
        return dict(
            revenue=C.values[round(player.round_number)-1]["Revenue"],
            market_size=C.values[round(player.round_number)-1]["MarketSize"],
            market_share=C.values[round(player.round_number)-1]["MarketShare"],
            price=C.values[round(player.round_number)-1]["Price"]
        )

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 1

    @staticmethod
    def live_method(player: Player, data):
        if player.treatment == 1:
            player.move_total = player.move_total + data["moved"]
        if player.treatment >= 2:
            if data["what"] == "share":
                player.share_move_total = player.share_move_total + data["moved"]
            if data["what"] == "size":
                player.size_move_total = player.size_move_total + data["moved"]
            if data["what"] == "price":
                player.price_move_total = player.price_move_total + data["moved"]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.payment_round == 1:
            player.participant.revenue_actual = C.values[round(player.round_number)-1]["Revenue"]
            player.participant.revenue_report = player.group.report
            if player.id_in_group == 1:
                player.participant.payoff_ecu = max(C.FIXED_PAY_MANAGER + int(player.participant.revenue_actual) - int(player.participant.revenue_report), C.MIN_COMP)
                player.participant.payoff_euro = player.participant.payoff_ecu / C.CONVERSION_RATE

class WaitForP1(WaitPage):

    title_text = "Please wait"
    body_text = "The manager is preparing her/his report. You will see the report once she/he is finished."

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 2

class Guess(Page):
    form_model = 'group'
    form_fields = ['guess']

    @staticmethod
    def is_displayed(player):
        return player.id_in_group == 2

    def before_next_page(player: Player, timeout_happened):
        if player.id_in_group == 2:
            if player.payment_round == 1:
                player.participant.revenue_actual = C.values[round(player.round_number)-1]["Revenue"]
                player.participant.revenue_report = player.group.report

            if player.round_number == player.participant.lottery_round_no:
                if abs(int(C.values[round(player.round_number)-1]["Revenue"]) - player.group.guess) <= 50:
                    player.participant.lottery_won = 1
                else:
                    player.participant.lottery_won = 0

            if player.round_number == C.NUM_ROUNDS:
                player.participant.payoff_ecu = C.FIXED_PAY_OWNER + int(player.participant.revenue_report) + player.participant.lottery_won * 50
                player.participant.payoff_euro = player.participant.payoff_ecu / C.CONVERSION_RATE

class ShowReport(Page):
    form_model = 'group'

    def is_displayed(player):
        return (player.id_in_group == 2)

class Results(Page):
    def vars_for_template(player):
        a = 1
        c = 1
        for i in player.in_all_rounds():
            if i.payment_round:
                b = a
            a = a + 1
        return dict(
            paymentround = b,
            pay_owner_from_round = C.FIXED_PAY_OWNER + int(player.participant.revenue_report)
        )

    def is_displayed(player):
        return 0
        #return player.round_number == C.NUM_ROUNDS

class Finish(Page):
    pass

class WaitForAll(WaitPage):
    wait_for_all_groups = True

    title_text = "Please wait"
    body_text = "Please hold on. Once all participants are ready, you will be rematched with another participant and continue to the next period."

page_sequence = [Welcome, Setting_overview, Setting_payoffs, Setting, Questions, Setting_distribution, Report, WaitForP1, ShowReport, Guess, Finish, WaitForAll]
