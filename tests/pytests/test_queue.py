"""
Test module for Queue data structure with basic operations
"""

import time

from impy.datastructures.queues import ordering_system


def test_order_system(caplog):
    ordering_system()
    time.sleep(0.5 * 4)
    assert caplog.record_tuples == [
        ("root", 30, "pizza"),
        ("root", 30, "samosa"),
        ("root", 30, "biryani"),
        ("root", 30, "burger"),
    ]
