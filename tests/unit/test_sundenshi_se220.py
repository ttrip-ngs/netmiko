"""Unit tests for Sun Denshi SE220."""

from netmiko.sundenshi import SundenshiSE220SSH


def test_sundenshi_se220_class_exists():
    """Verify SundenshiSE220SSH class can be imported."""
    assert SundenshiSE220SSH is not None


def test_sundenshi_se220_inheritance():
    """Verify SundenshiSE220SSH inherits from BaseConnection."""
    from netmiko.base_connection import BaseConnection

    assert issubclass(SundenshiSE220SSH, BaseConnection)


def test_sundenshi_se220_dispatcher_mapping():
    """Verify device_type mapping in ssh_dispatcher."""
    from netmiko.ssh_dispatcher import CLASS_MAPPER

    assert "sundenshi_se220" in CLASS_MAPPER
    assert CLASS_MAPPER["sundenshi_se220"] == SundenshiSE220SSH


def test_sundenshi_se220_not_cisco_based():
    """Verify SundenshiSE220SSH does NOT inherit from CiscoBaseConnection."""
    from netmiko.cisco_base_connection import CiscoBaseConnection

    assert not issubclass(SundenshiSE220SSH, CiscoBaseConnection)
