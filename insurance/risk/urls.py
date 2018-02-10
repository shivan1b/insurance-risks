# Third Party Stuff
from macrosurl import url

from . import views

urlpatterns = [
    url('risk/:uuid/detail', views.show_risk_detail_form, name='risk-detail'),
]
