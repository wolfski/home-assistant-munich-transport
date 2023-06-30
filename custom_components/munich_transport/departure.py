from dataclasses import dataclass
from datetime import datetime

from .const import DEFAULT_ICON, TRANSPORT_TYPE_VISUALS


@dataclass
class Departure:
    """Departure dataclass to store data from API"""

    trip_id: str
    line_name: str
    line_type: str
    timestamp: datetime
    time: str
    direction: str | None = None
    icon: str | None = None
    bg_color: str | None = None
    location: tuple[float, float] | None = None

    @classmethod
    def from_dict(cls, source):
        line_visuals = TRANSPORT_TYPE_VISUALS.get(source['type']) or {}
        timestamp = datetime.fromtimestamp(source['time'])
        return cls(
            trip_id=source['line'] + '_' + str(source['planned']),
            line_name=source['line'],
            line_type=source['type'],
            timestamp=timestamp,
            time="%s min" % str(int((timestamp - datetime.now()).total_seconds() / 60)),
            direction=source['destination'],
            icon=line_visuals.get("icon") or DEFAULT_ICON,
            bg_color=line_visuals.get("color"),
            location=(0.0, 0.0),
        )

    def to_dict(self):
        return {
            "line_name": self.line_name,
            "line_type": self.line_type,
            "time": self.time,
            "direction": self.direction,
            "color": self.bg_color,
        }
