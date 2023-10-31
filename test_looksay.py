
import pytest
from looksay import look_and_say


def test_look_and_say():
    res = look_and_say(input_string="1")
    assert res == "11"

    res = look_and_say(input_string="111221")
    assert res == "312211"

    res = look_and_say(input_string="31131211131221")
    assert res == "13211311123113112211"

    res = look_and_say(input_string="55555")
    assert res == "55"

    res = look_and_say(input_string="22")
    assert res == "22"
 
def test_look_and_say_err():

    with pytest.raises(ValueError):
        look_and_say(input_string="-1")

    with pytest.raises(ValueError):
        look_and_say(input_string="string")

    with pytest.raises(ValueError):
        look_and_say(input_string="2.22")
