from datetime import timedelta

DOMAIN = "munich_transport"
SCAN_INTERVAL = timedelta(seconds=60)

DEFAULT_ICON = "mdi:clock"

CONF_DEPARTURES = "departures"
CONF_DEPARTURES_NAME = "name"
CONF_DEPARTURES_STATION = "station"
CONF_DEPARTURES_DIRECTIONS = "directions"
CONF_DEPARTURES_LINES = "lines"
CONF_DEPARTURES_TYPES = "types"
CONF_DEPARTURES_WALKING_TIME = "walking_time"
CONF_TYPE_SUBURBAN = "S-Bahn"
CONF_TYPE_SUBWAY = "U-Bahn"
CONF_TYPE_TRAM = "Tram"
CONF_TYPE_BUS = "Bus"

TRANSPORT_TYPE_VISUALS = {
    CONF_TYPE_SUBURBAN: { 
        "code": "S", 
        "icon": "mdi:subway-variant", 
    },  
    CONF_TYPE_SUBWAY: {
        "code": "U",
        "icon": "mdi:subway",
    },
    CONF_TYPE_TRAM: {
        "code": "M",
        "icon": "mdi:tram",
    },
    CONF_TYPE_BUS: {
        "code": "BUS",
        "icon": "mdi:bus",
    }
}
