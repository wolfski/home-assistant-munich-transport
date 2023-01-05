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
        line_visuals = TRANSPORT_TYPE_VISUALS.get(source['product']) or {}
        timestamp = datetime.fromtimestamp(source['departureTime'] / 1000)
        return cls(
            trip_id=source["departureId"],
            line_name=source['label'],
            line_type=source['product'],
            timestamp=timestamp,
            time="%s min" % source['departureTimeMinutes'],
            direction=(source['destination'][:32] + '...') if len(source['destination']) > 32
            else source['destination'],
            icon=line_visuals.get("icon") or DEFAULT_ICON,
            bg_color=source['lineBackgroundColor'],
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
