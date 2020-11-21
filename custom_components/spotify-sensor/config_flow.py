from homeassistant.config_entries import ConfigFlow
from homeassistant.helpers import config_validation as cv
from homeassistant.components.spotify.const import DOMAIN as SPOTIFY_DOMAIN, DATA_SPOTIFY_ME
import voluptuous as vol

from .const import DOMAIN, CONF_USERNAME, ERROR_INVALID_USER, ERROR_NO_USERS

class SpotifySensorFlowHandler(ConfigFlow, domain=DOMAIN):
    """Config flow to handle Spotify Sensor creation."""

    async def async_step_user(self, user_input = None):
        self.hass.data.setdefault(DOMAIN, {})
        usernames: [str] = [entry[DATA_SPOTIFY_ME]['display_name'] for entry in self.hass.data[SPOTIFY_DOMAIN].values()] 
        setup_usernames: [str] = list(self.hass.data[DOMAIN].keys())
        open_usernames: [str] = list([u for u in usernames if u not in setup_usernames])

        errors = {}
        if not open_usernames:
            errors['base'] = ERROR_NO_USERS

        if user_input is not None:
            if user_input[CONF_USERNAME] in open_usernames:
                self.hass.data[DOMAIN].setdefault(CONF_USERNAME, {})
                return self.async_create_entry(title=user_input[CONF_USERNAME], data=user_input)
            else:
                errors[CONF_USERNAME] = ERROR_INVALID_USER

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_USERNAME): vol.In(open_usernames),
            }),
        )
