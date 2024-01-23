from dataclasses import dataclass
from datetime import datetime

from .const import DEFAULT_ICON, TRANSPORT_TYPE_VISUALS


@dataclass
class Departure:
    """Departure dataclass to store data from API"""

    trip_id: str
    line_name: str
    line_type: str
    line_code: str
    timestamp: datetime
    departure_time: str
    time: str
    direction: str | None = None
    icon: str | None = None
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
            departure_time=timestamp.strftime('%H:%M'),
            time="%s min" % str(int((timestamp - datetime.now()).total_seconds() / 60)),
            direction=source['destination'],
            icon=line_visuals.get("icon") or DEFAULT_ICON,
            line_code=line_visuals.get("code") or "",
            location=(0.0, 0.0),
        )

    def to_dict(self):
        return {
            "line_name": self.line_name,
            "line_type": self.line_type,
            "time": self.time,
            "departure_time": self.departure_time,
            "direction": self.direction,
            "line_code": self.line_code,
        }