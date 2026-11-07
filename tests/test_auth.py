"""Unit tests for the authentication service."""

import pytest

from src.auth import refresh_session, validate_token


def test_valid_token():
    result = validate_token("  valid_secret_token_12345  ")

    assert result["valid"] is True
    assert result["token"] == "valid_secret_token_12345"


def test_short_token_raises_value_error():
    with pytest.raises(ValueError, match="at least 10 characters"):
        validate_token("short")


def test_whitespace_only_token_raises_value_error():
    with pytest.raises(ValueError, match="at least 10 characters"):
        validate_token("   ")


def test_none_token_raises_value_error():
    with pytest.raises(ValueError):
        validate_token(None)


def test_refresh_session():
    result = refresh_session("super_secure_session_token_xyz")

    assert result["valid"] is True
    assert result["refreshed"] is True
