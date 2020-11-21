from datetime import timedelta, datetime
import json
import logging
from homeassistant.core import HomeAssistant
from homeassistant.const import DEVICE_CLASS_TIMESTAMP
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity import Entity
from homeassistant.components.spotify.const import DOMAIN as SPOTIFY_DOMAIN, DATA_SPOTIFY_CLIENT, DATA_SPOTIFY_ME

from .const import DOMAIN, ICON, CONF_USERNAME, DATA_PLAYLISTS, DATA_RECENTLY, DATA_TOP_ARTISTS, DATA_CURRENT

SCAN_INTERVAL = timedelta(minutes=10)
_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities):
    """Setup the spotify sensor entity"""

    entry = next((entry for entry in hass.data[SPOTIFY_DOMAIN].values() if entry[DATA_SPOTIFY_ME]['display_name'] == config_entry.data[CONF_USERNAME]), None)
    if entry:
        async_add_entities([SpotifySensor(hass, entry[DATA_SPOTIFY_CLIENT], entry[DATA_SPOTIFY_ME]['display_name'])])
        return True
    else:
        _LOGGER.warn("Skipping spotify-sensor for {}, because no matching 'spotify' configuration can be found.".format(config_entry.data[CONF_USERNAME]))
        return False

class SpotifySensor(Entity):
    """Sensor containing spotify playlist information"""

    def __init__(self, hass, client, name):
        self.hass = hass
        self._spotify = client
        self._last_update = None
        self._name = name
        self.hass.data[DOMAIN].setdefault(self._name, {})
    
    async def async_update(self):
        self.hass.data[DOMAIN][self._name] = {
            DATA_PLAYLISTS: await self.hass.async_add_executor_job(self._spotify.current_user_playlists),
            DATA_RECENTLY: await self.hass.async_add_executor_job(self._spotify.current_user_recently_played),
            DATA_TOP_ARTISTS: await self.hass.async_add_executor_job(self._spotify.current_user_top_artists),
        }
        self._last_update = datetime.now()

    @property
    def state(self):
        """Return the currently playing song"""
        return self._last_update if self._last_update else ""

    @property
    def name(self):
        """Return the name."""
        return self._name
    
    def available(self):
        return self._last_update is not None

    @property
    def icon(self):
        return ICON

    @property
    def device_class(self):
        return DEVICE_CLASS_TIMESTAMP

    @property
    def device_state_attributes(self):
        return self.hass.data[DOMAIN][self._name]
