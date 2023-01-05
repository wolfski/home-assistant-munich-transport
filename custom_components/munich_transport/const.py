from datetime import timedelta

DOMAIN = "munich_transport"
SCAN_INTERVAL = timedelta(seconds=90)

DEFAULT_ICON = "mdi:clock"

CONF_DEPARTURES = "departures"
CONF_DEPARTURES_NAME = "name"
CONF_DEPARTURES_WALKING_TIME = "walking_time"
CONF_TYPE_SUBURBAN = "SBAHN"
CONF_TYPE_SUBWAY = "UBAHN"
CONF_TYPE_TRAM = "TRAM"
CONF_TYPE_BUS = "BUS"

TRANSPORT_TYPE_VISUALS = {
    CONF_TYPE_SUBURBAN: {
        "code": "S",
        "icon": "mdi:subway-variant",
        "color": "#4C9046",
    },
    CONF_TYPE_SUBWAY: {
        "code": "U",
        "icon": "mdi:subway",
        "color": "#0065AE",
    },
    CONF_TYPE_TRAM: {
        "code": "M",
        "icon": "mdi:tram",
        "color": "#E30613",
    },
    CONF_TYPE_BUS: {
        "code": "BUS",
        "icon": "mdi:bus",
        "color": "#133B4B"
    }
}
