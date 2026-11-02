from datetime import datetime,timezone
import httpx
import pytest
from market_watcher import sources
from market_watcher import notifiers
from market_watcher.rules import percent_change,should_alert
from market_watcher.sources import Source
from market_watcher.notifiers import Notifier
from market_watcher.models import Observation
from market_watcher.storage import Storage
from market_watcher.cli import run_one





def test_percent_drop():
    assert percent_change(100,85) == pytest.approx(-15)

def test_percent_incr():
    assert percent_change(85,102) == pytest.approx(20)



def test_should_alert_true_on_big_rise():
    assert should_alert(45,100,5)[0]

def test_should_alert_true_on_big_drop():
    assert should_alert(120,65,5)[0]

def test_should_alert_true_on_change_equal_to_threshold():
    assert should_alert(100,105,5)[0]

def test_should_alert_false_on_small_rise():
    change=should_alert(100,102,5)
    assert not change[0]

def test_should_alert_false_on_when_old_is_none():
    assert not should_alert(None,80,5)


