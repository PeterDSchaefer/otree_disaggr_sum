from otree.api import *


doc = """
Your app description
"""

class C(BaseConstants):
    NAME_IN_URL = 'peq'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    FIXED_PAY_MANAGER = 175
    FIXED_PAY_OWNER = 100
    CONVERSION_RATE = 25
    MIN_COMP = 125
    EXPERIMENT_NO = '2022-06'

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    code_noted = models.BooleanField(label="Have you written down or saved your code?", widget=widgets.RadioSelect)

    payoff_self = models.FloatField()

    code = models.StringField()

    age = models.IntegerField(min = 1912, max = 2012, label = "What is your birthyear?")

    gender = models.StringField(
        choices = [["Male", "Male"], ["Female", "Female"], ["Other", "Other"]],
        label = "What is your gender?",
        widget = widgets.RadioSelect
    )

    discipline = models.StringField(
        choices = ["Business", "Engineering", "Humanities", "Natural/life sciences", "Social sciences", "Other"],
        label = "What is your primary faculty or department?",
        widget = widgets.RadioSelect
    )

    degree = models.StringField(
        choices = ["High school diploma (Abitur)", "Bachelor", "Master or higher"],
        label = "What is the highest educational degree you currently have?",
        widget = widgets.RadioSelect
    )

    perceived_trust = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label="The owners trusted me to make truthful reports.",
        widget=widgets.RadioSelectHorizontal
    )

    mathskills = models.IntegerField(
        choices=[1,2,3,4,5,6],
        label="What was your final grade in mathematics in high school?",
        widget=widgets.RadioSelectHorizontal)

    cognitive_effort= models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label="I was making my own computations while I was adjusting sliders.",
        widget=widgets.RadioSelectHorizontal
    )

    motive_honesty= models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label="Whenever I prepared my report to the owner, I wanted to be honest with the owner.",
        widget=widgets.RadioSelectHorizontal
    )

    motive_credibility= models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label="Whenever I prepared my report to the owner, I wanted to appear honest to the owner.",
        widget=widgets.RadioSelectHorizontal
    )

    motive_egoism= models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label="Whenever I prepared my report to the owner, I wanted to send a report that would make me earn money.",
        widget=widgets.RadioSelectHorizontal
    )

    motive_altruism= models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label="Whenever I prepared my report to the owner, I wanted to send a report that would leave money to the owner.",
        widget=widgets.RadioSelectHorizontal
    )

    deliberation_honesty= models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label="Whenever I was adjusting a slider, I thought about whether the resulting report to the owner would be honest.",
        widget=widgets.RadioSelectHorizontal
    )

    deliberation_credibility= models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label="Whenever I was adjusting a slider, I thought about whether the resulting report to the owner would make me appear honest.",
        widget=widgets.RadioSelectHorizontal
    )

    deliberation_egoism= models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label="Whenever I was adjusting a slider, I thought about how much money I would make from the resulting report.",
        widget=widgets.RadioSelectHorizontal
    )

    deliberation_altruism = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label="Whenever I was adjusting a slider, I thought about how much money the owner would make from the resulting report.",
        widget=widgets.RadioSelectHorizontal
    )

    deliberation_general= models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label="Whenever I was adjusting a slider, I deliberated about the pros and cons of entering a number that was lower or higher than the actual number.",
        widget=widgets.RadioSelectHorizontal
    )

    reactance_planning= models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label="The numbers that I was required to enter for planning made me feel distrusted.",
        widget=widgets.RadioSelectHorizontal
    )

    reactance_reporting= models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label="The numbers that I was required to report made me feel distrusted.",
        widget=widgets.RadioSelectHorizontal
    )

    contingency= models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label="It would be unethical for a manager to increase the own payoff by significantly understating the actual revenue in the report.",
        widget=widgets.RadioSelectHorizontal
    )

    normative_expect= models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label="The owners were expecting to receive honest reports from the managers each period.",
        widget=widgets.RadioSelectHorizontal
    )

    empirical_expect= models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label="Other managers reported low revenues in this experiment.",
        widget=widgets.RadioSelectHorizontal
    )

    machiav1= models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label="These days a person doesn’t really know whom she/he can count on.",
        widget=widgets.RadioSelectHorizontal
    )

    machiav2= models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label="You sometimes can’t help wondering whether anything is worthwhile.",
        widget=widgets.RadioSelectHorizontal
    )

    machiav3= models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label="To make money there are no right and wrong ways anymore, only easy and hard ways.",
        widget=widgets.RadioSelectHorizontal
    )

    uncertainty_sub= models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label="The owners were uncertain about how truthful my reports were.",
        widget=widgets.RadioSelectHorizontal
    )

    uncertainty_sup = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label="I was uncertain about how honest the managers’ reports were.",
        widget=widgets.RadioSelectHorizontal
    )



# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'discipline', 'degree', 'mathskills']

class PEQ_sub(Page):
    form_model = 'player'
    form_fields = ['cognitive_effort', 'motive_honesty', 'motive_credibility', 'motive_egoism', 'motive_altruism',
                   'deliberation_honesty', 'deliberation_credibility', 'deliberation_egoism', 'deliberation_altruism',
                   'deliberation_general', 'reactance_planning', 'reactance_reporting', 'contingency', 'normative_expect',
                   'empirical_expect', 'perceived_trust', 'machiav1', 'machiav2', 'machiav3', 'uncertainty_sub']

    def is_displayed(player):
        return player.participant.role == 1

class PEQ_sup(Page):
    form_model = 'player'
    form_fields = ['machiav1', 'machiav2', 'machiav3', 'uncertainty_sup']

    def is_displayed(player):
        return player.participant.role == 2

class Results(Page):
    def vars_for_template(player):
        return dict(
            pay_owner_from_round=C.FIXED_PAY_OWNER + int(player.participant.revenue_report),
            pay_manager_from_round=C.FIXED_PAY_MANAGER + int(player.participant.revenue_actual) - int(player.participant.revenue_report)
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.payoff_self = player.participant.payoff_euro
        player.participant.payment_code = C.EXPERIMENT_NO + "-" + str(player.session.code) + "-" + str(player.participant.code)
        player.code = player.participant.payment_code

class Code(Page):
    form_model = 'player'

class Finish(Page):
    pass

page_sequence = [MyPage, PEQ_sub, PEQ_sup, Results, Code, Finish]
