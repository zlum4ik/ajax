
def test_side_bar(fixture_for_test):
    fixture_for_test.side_bar_actions()
    assert fixture_for_test.assert_menu()

