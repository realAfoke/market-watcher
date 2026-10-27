import pytest
from market_watcher.rules import percent_change,should_alert


def test_percent_drop():
    assert percent_change(100,85) == pytest.approx(-15)

def test_percent_incr():
    assert percent_change(85,102) == pytest.approx(20)



def test_should_alert_true_on_big_rise():
    assert should_alert(45,100,5)

def test_should_alert_true_on_big_drop():
    assert should_alert(120,65,5)

def test_should_alert_true_on_change_equal_to_threshold():
    assert should_alert(100,105,5)

def test_should_alert_false_on_small_rise():
    assert not should_alert(100,102,5)

def test_should_alert_false_on_when_old_is_none():
    assert not should_alert(None,80,5)
