import pytest
from unittest.test.testmock.testmock import MagicMock


@pytest.fixture()
def data_serializer():
    from nhl_stats.serializers.data_serializer import DataSerializer
    serializer = DataSerializer()
    return serializer


def test_data_serializer(data_serializer):
    test_json = MagicMock(text='{"test": "data"}')
    expected_data = {'test': 'data'}

    data = data_serializer.serialize(test_json)

    assert expected_data == data