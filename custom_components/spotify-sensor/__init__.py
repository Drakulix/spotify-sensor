from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import ConfigType
from homeassistant.components.spotify.const import DOMAIN as SPOTIFY_DOMAIN

from .const import DOMAIN, CONF_USERNAME

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    hass.data.setdefault(DOMAIN, {})
    return True

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    hass.data[DOMAIN].setdefault(config_entry.data[CONF_USERNAME], {})
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(
            config_entry, "sensor"
        )
    )
    return True
