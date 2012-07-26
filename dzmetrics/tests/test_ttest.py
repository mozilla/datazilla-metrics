"""Tests for ttest module."""
from unittest import TestCase

from dzmetrics.ttest import welchs_ttest


class TestWelchsTtest(TestCase):
    """Tests for welchs_ttest."""
    def test_p(self):
        """Test correct p value."""
        x1 = [10, 11, 12, 13]
        x2 = [5, 6, 8, 9]
        p = welchs_ttest(x1, x2)["p"]

        assert abs(p-0.0043) < 0.00001


    def test_stddev1(self):
        """Test correct stddev1 value."""
        x1 = [10, 11, 12, 13]
        x2 = [5, 6, 8, 9]
        s1 = welchs_ttest(x1, x2)["stddev1"]

        assert abs(s1-1.291) < 0.001


    def test_stddev2(self):
        """Test correct stddev2 value."""
        x1 = [10, 11, 12, 13]
        x2 = [5, 6, 8, 9]
        s2 = welchs_ttest(x1, x2)["stddev2"]

        assert abs(s2-1.826) < 0.001


    def test_mean1(self):
        """Test correct mean1 value."""
        x1 = [10, 11, 12, 13]
        x2 = [5, 6, 8, 9]
        m1 = welchs_ttest(x1, x2)["mean1"]

        assert abs(m1-11.5) < 0.001


    def test_mean2(self):
        """Test correct mean2 value."""
        x1 = [10, 11, 12, 13]
        x2 = [5, 6, 8, 9]
        m2 = welchs_ttest(x1, x2)["mean2"]

        assert abs(m2-7.0) < 0.001


    def test_h0_rejected(self):
        """Test correct h0_rejected value."""
        x1 = [10, 11, 12, 13]
        x2 = [5, 6, 8, 9]
        h0r = welchs_ttest(x1, x2, alpha=0.05)["h0_rejected"]

        assert h0r
