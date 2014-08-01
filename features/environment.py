from behaving import environment as benv

PERSONAS = {
    'Andrew': dict(
        first_name='Andrew',
        last_name='Acorn',
        email='andrew.acorn@mailinator.com',
        password='areallyreallygoodpassword'
    ),
    'Ben': dict(
        first_name='Ben',
        last_name='Brown',
        email='ben.brown@mailinator.com',
        password='anotherreallyreallygoodpassword'
    )
}


def before_all(context):
    benv.before_all(context)


def after_all(context):
    benv.after_all(context)


def before_feature(context, feature):
    benv.before_feature(context, feature)


def after_feature(context, feature):
    benv.after_feature(context, feature)


def before_scenario(context, scenario):
    benv.before_scenario(context, scenario)
    context.personas = PERSONAS


def after_scenario(context, scenario):
    benv.after_scenario(context, scenario)