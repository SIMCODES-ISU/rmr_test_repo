"""
Unit and regression test for the rmr_test_repo package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import rmr_test_repo


def test_rmr_test_repo_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "rmr_test_repo" in sys.modules
