import logging

from tests.settings import TEST_DATA


def test_positive_login(fixture_for_test):
    fixture_for_test.login_actions(email=TEST_DATA['positive_login']['email'],
                                     password=TEST_DATA['positive_login']['password'])
    assert fixture_for_test.assert_later_btn().is_displayed()


def test_negative_login(fixture_for_test):
    fixture_for_test.login_actions(email=TEST_DATA['negative_login']['email'],
                                     password=TEST_DATA['negative_login']['password'])
    assert fixture_for_test.assert_negative_login().is_displayed()
