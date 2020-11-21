# Spotify Sensor for HA

Spotify sensor for Home-Assistant inspired by [spotify-playlist-sensor](https://github.com/dnguyen800/spotify-playlist-sensor).

Spotify-sensor adds a sensor for your spotify accounts, that lists your playlist, recently played items and top artists in its attributes.
Can be used to build Spotify UIs in Home-Assistant much like [spotify-card](https://github.com/custom-cards/spotify-card), but without needing a custom lovelace card.

Can be especially useful, if your spotify devices are not listed by spotify-card and the like (e.g. Sonos players), but can be used through other services, as you can implement those actions natively in home-assistant yourself.


## How to install

This is easily installed through [HACS](https://github.com/hacs/integration).

Just add this repository as a "custom repository" and search for "spotify-sensor".


## How to setup

You can setup this component through the UI. You need to have setup the normal [spotify-integration](https://www.home-assistant.io/integrations/spotify) previously for all accounts you want to use.


## How to contribute

If you want to add functionality and help development of this custom component, you may find the [.vscode/tasks.json](https://github.com/drakulix/spotify-sensor/blob/master/.vscode/tasks.json) useful.

If you are using Visual Studio Code you can directly run these tasks to setup a local home-assistant instance for quick troubleshooting and testing.

If not the json-file includes some quick commands to use may adapt.

**Note**: For using those tasks you need to have podman installed. Alternatively replace podman with docker.