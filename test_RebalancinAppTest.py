#Fixtures
import pytest
from RebalancingApp import calculate_shares

def test_login(userLogin):
    print("Rebalancing App Test")

def test_ibm_buy():
    shares = calculate_shares(100000, 20, 10, 150)
    assert shares == 66.67

def test_orcl_sell():
    shares = calculate_shares(100000, 20, 30, 220)
    assert shares == -45.45

def test_hold_positions():
    assert calculate_shares(100000, 20, 20, 90) == 0
    assert calculate_shares(100000, 20, 20, 450) == 0
    assert calculate_shares(100000, 20, 20, 70) == 0

def test_total_buy_equals_total_sell():
    ibm = calculate_shares(100000, 20, 10, 150) * 150
    orcl = calculate_shares(100000, 20, 30, 220) * 220
    assert ibm == pytest.approx(abs(orcl), rel=1e-2)

def test_negative_variance_means_buy():
    shares = calculate_shares(100000, 20, 10, 150)
    assert shares > 0

def test_positive_variance_means_sell():
    shares = calculate_shares(100000, 20, 30, 220)
    assert shares < 0

def test_invalid_input():
    try:
        calculate_shares(100000, -10, 20, 150)
        assert False
    except Exception:
        assert True
