from apistar import Route, TestClient, typesystem
from apistar.frameworks.wsgi import WSGIApp as App


class Color(typesystem.Enum):
    errors = {'invalid': 'Must be a valid color.'}
    enum = ['red', 'green', 'blue']


class TermsAndConditions(typesystem.Enum):
    errors = {'invalid': 'You must agree to the terms and conditions to proceed.'}
    enum = ['yes']


def validate_color(value: Color):
    return {'value': value}


def validate_terms(value: TermsAndConditions):
    return {'value': value}


app = App(routes=[
    Route('/color/', 'GET', validate_color),
    Route('/terms/', 'GET', validate_terms),
])


client = TestClient(app)


def test_valid_enum():
    response = client.get('/color/?value=red')
    assert response.status_code == 200
    assert response.json() == {'value': 'red'}


def test_valid_literal():
    response = client.get('/terms/?value=yes')
    assert response.status_code == 200
    assert response.json() == {'value': 'yes'}


def test_invalid_enum():
    response = client.get('/color/?value=foo')
    assert response.status_code == 400
    assert response.json() == {'value': 'Must be a valid color.'}


def test_invalid_literal():
    response = client.get('/terms/?value=foo')
    assert response.status_code == 400
    assert response.json() == {'value': 'You must agree to the terms and conditions to proceed.'}
