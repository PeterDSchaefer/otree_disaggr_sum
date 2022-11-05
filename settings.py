from os import environ

ROOMS = [
    dict(
        name='Round_1',
        display_name='Virtual Lab, November 07th'
    ),
    dict(
        name='Room_with_list',
        display_name='Virtual Lab, November 07th',
        participant_label_file='room_participants',
        use_secure_urls=True
    )
]

SESSION_CONFIGS = [
     dict(
         name='aggregated_planning',
         app_sequence=['reporting', 'peq'],
         num_demo_participants=2,
         aggregated_planning=True,
         aggregated_reporting=True
     ),
    dict(
        name='disaggregated_planning',
        app_sequence=['reporting', 'peq'],
        num_demo_participants=2,
        aggregated_planning=False,
        aggregated_reporting=True
    ),
    dict(
        name='disaggregated_reporting',
        app_sequence=['reporting', 'peq'],
        num_demo_participants=2,
        aggregated_planning=False,
        aggregated_reporting=False
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['treatment', 'role', 'payment_roundno', 'revenue_actual', 'revenue_report', 'lottery_round_no', 'lottery_won', 'payoff_ecu', 'payoff_euro', 'payment_code']
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '4964100468377'
