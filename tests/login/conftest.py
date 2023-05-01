import pytest

from framework.actions import Actions


@pytest.fixture(scope='function')
def fixture_for_test(driver):
    yield Actions(driver)
