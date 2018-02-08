# Third Party Stuff
import pytest
from tests.factories import risk as f
from tests.factories.base import create_user

pytestmark = pytest.mark.django_db


def test_get_all_risks(client):
    user = create_user()
    f.create_risk(insurer=user, name='automobile')
    f.create_risk(insurer=user, name='life')
    f.create_risk(insurer=user, name='health')

    response = client.get('/api/risk')
    assert response.status_code == 200
    assert 'health' == response.data['results'][0]['name']
    assert 'life' == response.data['results'][1]['name']
    assert 'automobile' == response.data['results'][2]['name']


def test_get_particular_risk(client):
    user = create_user()
    risk = f.create_risk(insurer=user, name='automobile')
    f.create_riskfield(name='motor company', ftype='ch', risk=risk)
    f.create_riskfield(name='purchase date', ftype='dt', risk=risk)

    response = client.get('/api/risk/{}'.format(risk.id))
    assert response.status_code == 200
    assert 'automobile' == response.data['name']
    assert 'purchase date' == response.data['riskfields'][0]['name']
    assert 'motor company' == response.data['riskfields'][1]['name']


def test_create_risk_authorized(client):
    user = create_user()
    data = {
        'name': 'automobile',
        'insurer': user,
    }
    client.login(user)

    response = client.post('/api/risk', data=data)
    assert response.status_code == 201


def test_create_risk_unauthorized(client):
    user = create_user()
    data = {
        'name': 'automobile',
        'insurer': user,
    }

    response = client.post('/api/risk', data=data)
    assert response.status_code == 401
