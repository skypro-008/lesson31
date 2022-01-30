import pytest

from tests.factories import VacancyFactory
from vacancies.serializers import VacancySerializer


@pytest.mark.django_db
def test_list_view(client):
    vacancies = VacancyFactory.create_batch(10)

    response = client.get("/vacancy/")

    assert response.status_code == 200
    assert response.data == VacancySerializer(vacancies, many=True).data