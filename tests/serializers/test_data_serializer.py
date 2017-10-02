from nhl_stats.serializers.data_serializer import DataSerializer
import pytest


@pytest.fixture()
def data_serializer():
    serializer = DataSerializer()
    return serializer


def test_data_serializer(data_serializer):
    test_json = '{"test": "data"}'
    expected_data = {'test': 'data'}

    data = data_serializer.serialize(test_json)

    assert expected_data == data