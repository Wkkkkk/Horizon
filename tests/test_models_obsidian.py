"""Tests for the optional Obsidian bookmark config."""

from src.models import Config, ObsidianConfig


def _base_config_dict() -> dict:
    return {
        "ai": {"provider": "openai", "model": "gpt-4o", "api_key_env": "OPENAI_API_KEY"},
        "sources": {},
        "filtering": {},
    }


def test_config_defaults_obsidian_to_none():
    cfg = Config.model_validate(_base_config_dict())
    assert cfg.obsidian is None


def test_obsidian_config_defaults():
    data = _base_config_dict()
    data["obsidian"] = {"vault": "Obsidian"}
    cfg = Config.model_validate(data)
    assert cfg.obsidian is not None
    assert cfg.obsidian.vault == "Obsidian"
    assert cfg.obsidian.folder == "News/Horizon"
    assert cfg.obsidian.enabled is True


def test_obsidian_config_overrides():
    obs = ObsidianConfig(vault="MyVault", folder="Clips", enabled=False)
    assert obs.vault == "MyVault"
    assert obs.folder == "Clips"
    assert obs.enabled is False
