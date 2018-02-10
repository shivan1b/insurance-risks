from django.apps import apps
from django.shortcuts import get_object_or_404, render
from . import services


def show_risk_detail_form(request, uuid, template='risk/index.html'):
    Risk = apps.get_model('risk', 'Risk')
    risk = get_object_or_404(Risk, id=uuid)
    ctx = services.get_risk_data_for_context(risk=risk)

    return render(request, template, ctx)
