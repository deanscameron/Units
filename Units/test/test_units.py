from nose.tools import assert_true, assert_raises

# Aim to pass the following tests from the exercise
def test_to_pass():
    assert_true(5*meters == 0.005*kilometers)
    assert_true((60*seconds).to(minutes).value==1)
    assert_true((60*seconds).to(minutes).unit==minutes)
    with assert_raises(IncompatibleUnitsError):
        5*meters+2*seconds