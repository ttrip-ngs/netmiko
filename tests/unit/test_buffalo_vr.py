#!/usr/bin/env python
"""Unit tests for Buffalo VR SSH driver."""

import pytest
from netmiko.buffalo import BuffaloVRSSH


def test_buffalo_vr_import():
    """Test that BuffaloVRSSH class can be imported."""
    assert BuffaloVRSSH is not None


def test_buffalo_vr_class_attributes():
    """Test that BuffaloVRSSH has required attributes."""
    assert hasattr(BuffaloVRSSH, "session_preparation")
    assert hasattr(BuffaloVRSSH, "set_base_prompt")
    assert hasattr(BuffaloVRSSH, "check_config_mode")
    assert hasattr(BuffaloVRSSH, "config_mode")
    assert hasattr(BuffaloVRSSH, "exit_config_mode")
    assert hasattr(BuffaloVRSSH, "save_config")
    assert hasattr(BuffaloVRSSH, "check_enable_mode")
    assert hasattr(BuffaloVRSSH, "enable")
    assert hasattr(BuffaloVRSSH, "exit_enable_mode")
    assert hasattr(BuffaloVRSSH, "cleanup")


def test_buffalo_vr_device_type_registration():
    """Test that buffalo_vr device type is registered in ssh_dispatcher."""
    from netmiko.ssh_dispatcher import CLASS_MAPPER

    assert "buffalo_vr" in CLASS_MAPPER
    assert CLASS_MAPPER["buffalo_vr"] == BuffaloVRSSH
