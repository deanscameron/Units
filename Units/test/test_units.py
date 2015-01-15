from nose.tools import assert_true, assert_raises

def test_to_pass():
    assert_true(5*meters == 0.005*kilometers)
    assert_true((60*seconds).to_unit(minutes).coeff==1)
    assert_true((60*seconds).to_unit(minutes).unit==minutes)
    with assert_raises(TypeError):
        5*meters+2*seconds