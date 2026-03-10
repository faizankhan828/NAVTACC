class Match:
    def __init__(
        self,
        match_id,
        team1,
        team2,
        venue,
        match_date,
        result="TBD",
        player_of_match="TBD",
        team1_score="0/0",
        team2_score="0/0",
    ):
        self.match_id = match_id
        self.team1 = team1
        self.team2 = team2
        self.venue = venue
        self.match_date = match_date
        self.result = result
        self.player_of_match = player_of_match
        self.team1_score = team1_score
        self.team2_score = team2_score

    @classmethod
    def from_line(cls, line, franchise_lookup, venue_lookup):
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != 9:
            raise ValueError(f"Invalid match row: {line}")

        match_id, team1_name, team2_name, venue_name, match_date, result, pom, t1_score, t2_score = parts
        team1 = franchise_lookup.get(team1_name, team1_name)
        team2 = franchise_lookup.get(team2_name, team2_name)
        venue = venue_lookup.get(venue_name, venue_name)

        return cls(match_id, team1, team2, venue, match_date, result, pom, t1_score, t2_score)

    def record_result(self, result, player_of_match, team1_score, team2_score):
        self.result = result
        self.player_of_match = player_of_match
        self.team1_score = team1_score
        self.team2_score = team2_score

    def summary(self):
        team1_name = self.team1.name if hasattr(self.team1, "name") else str(self.team1)
        team2_name = self.team2.name if hasattr(self.team2, "name") else str(self.team2)
        venue_name = self.venue.name if hasattr(self.venue, "name") else str(self.venue)
        return (
            f"{self.match_id}: {team1_name} vs {team2_name} at {venue_name} on {self.match_date} | "
            f"{self.team1_score} - {self.team2_score} | {self.result}"
        )

    def __str__(self):
        return self.summary()
