VENUES_DATA = [
    "V-001|Gaddafi Stadium|Lahore|Pakistan|27000|Batting Friendly|true|85",
    "V-002|National Stadium|Karachi|Pakistan|34228|Balanced|true|112",
    "V-003|Rawalpindi Cricket Stadium|Rawalpindi|Pakistan|15000|Bowling Friendly|true|55",
    "V-004|Multan Cricket Stadium|Multan|Pakistan|35000|Batting Friendly|true|42",
    "V-005|Peshawar Cricket Stadium|Peshawar|Pakistan|13500|Balanced|true|38",
    "V-006|Dubai International Cricket Stadium|Dubai|United Arab Emirates|25000|Batting Friendly|true|60",
    "V-007|Sharjah Cricket Stadium|Sharjah|United Arab Emirates|16000|Balanced|true|44",
    "V-008|Abu Dhabi Cricket Ground|Abu Dhabi|United Arab Emirates|20000|Bowling Friendly|true|30",
]


class Venue:
    def __init__(self, venue_id, name, city, country, capacity, pitch_type, floodlights, matches_hosted):
        self.venue_id = venue_id
        self.name = name
        self.city = city
        self.country = country
        self.capacity = int(capacity)
        self.pitch_type = pitch_type
        self.floodlights = str(floodlights).strip().lower() in {"1", "true", "yes"}
        self.matches_hosted = int(matches_hosted)

    @classmethod
    def from_line(cls, line):
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != 8:
            raise ValueError(f"Invalid venue row: {line}")
        return cls(*parts)

    def description(self):
        lights = "Yes" if self.floodlights else "No"
        return f"{self.name}, {self.city} ({self.country}) | Pitch: {self.pitch_type} | Lights: {lights}"

    def __str__(self):
        return self.description()
