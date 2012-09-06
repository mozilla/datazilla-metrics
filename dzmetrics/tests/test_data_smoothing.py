"""Tests for ttest module."""
from unittest import TestCase

from dzmetrics.data_smoothing import exp_smooth

NEW_N = 25
NEW_S = 5
NEW_M = 50
OLD_N = 25
OLD_S = 8
OLD_M = 53

class TestExpSmoothtest(TestCase):
    """Tests for exp_smooth."""
    def test_exp_smooth_mean(self):
        """Test correct exp_smooth mean value."""
        result = exp_smooth(NEW_N, NEW_S, NEW_M, OLD_N, OLD_S, OLD_M)

        assert result['mean'] > NEW_M
        assert result['mean'] < OLD_M

    def test_exp_smooth_stddev(self):
        """Test correct exp_smooth stddev value."""
        result = exp_smooth(NEW_N, NEW_S, NEW_M, OLD_N, OLD_S, OLD_M)

        assert result['stddev'] > NEW_S
        assert result['stddev'] < OLD_S

    def test_exp_smooth_n(self):
        """Test correct exp_smooth n value."""
        result = exp_smooth(NEW_N, NEW_S, NEW_M, OLD_N, OLD_S, OLD_M)

        assert result['n'] == NEW_N
        assert result['n'] == OLD_N

