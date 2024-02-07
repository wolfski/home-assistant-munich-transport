"""Munich public transport (MVG) integration."""
from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN, SCAN_INTERVAL


def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    return True
