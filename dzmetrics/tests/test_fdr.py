"""Tests for fdr module."""
from unittest import TestCase

from dzmetrics.fdr import rejector


class TestRejector(TestCase):
    """Tests for rejector function."""
    def test_status(self):
        """Test status values."""
        p = [0.04, 0.8, 0.81, 0.01, 0.2, 0.9, 0.03, 0.95]
        status = rejector(p, 0.1)["status"]

        self.assertEqual(
            status,
            [False, False, False, True, False, False, False, False],
            )

    def test_count(self):
        """Test count value."""
        p = [0.04, 0.8, 0.81, 0.01, 0.2, 0.9, 0.03, 0.95]
        count = rejector(p, 0.1)["count"]

        self.assertEqual(count, 1)

