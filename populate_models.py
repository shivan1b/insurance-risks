"""
Make sure you have created a User before trying to run this script.
Simplest way to do it is creating a superuser in Django:
        $ ./manage.py createsuperuser
"""

from insurance.risk.models import Risk, RiskField, User

user = User.objects.first()
risk = Risk.objects.create(insurer=user, name="automobile")
RiskField.objects.create(risk=risk, name="model", ftype="en", value="['A', 'B', 'C']")
RiskField.objects.create(risk=risk, name="name of insuree", ftype="ch")
RiskField.objects.create(risk=risk, name="date of purchase", ftype="dt")
RiskField.objects.create(risk=risk, name="prize dollar amount", ftype="in")
