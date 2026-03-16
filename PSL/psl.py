import random
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent


# ─── File-reading helper ───

def _read_lines(filepath: Path) -> list[str]:
    if not filepath.exists():
        print(f"  [WARNING] File not found: {filepath}")
        return []
    with filepath.open("r", encoding="utf-8") as fh:
        return [l.strip() for l in fh if l.strip() and not l.strip().startswith("#")]


def _parse_line(line: str, expected: int) -> list[str]:
    parts = [x.strip() for x in line.split("|")]
    if len(parts) != expected:
        raise ValueError(f"Expected {expected} fields, got {len(parts)}: {line[:50]}")
    return parts


# ─── Player ───

class Player:
    def __init__(self, player_id, full_name, nationality, age, role,
                 batting_style, bowling_style, total_runs, total_wickets,
                 matches_played, salary):
        self.player_id = player_id
        self.full_name = full_name
        self.nationality = nationality
        self.age = int(age)
        self.role = role
        self.batting_style = batting_style
        self.bowling_style = bowling_style
        self.total_runs = int(total_runs)
        self.total_wickets = int(total_wickets)
        self.matches_played = int(matches_played)
        self.salary = float(salary)
        # Computed
        self.batting_avg = round(self.total_runs / self.matches_played, 2) if self.matches_played else 0.0
        self.bowling_avg = round(self.matches_played / self.total_wickets, 2) if self.total_wickets else 0.0

    @classmethod
    def from_line(cls, line: str) -> "Player":
        return cls(*_parse_line(line, 11))

    def display(self) -> None:
        print(f"  {self.full_name:<24} {self.role:<14} Runs:{self.total_runs:<5} "
              f"Wkts:{self.total_wickets:<4} Avg:{self.batting_avg:<6}")

    def __lt__(self, other: "Player") -> bool:
        return self.total_runs < other.total_runs

    def __str__(self) -> str:
        return f"{self.full_name} ({self.role})"


# ─── CoachingStaff ───

class CoachingStaff:
    def __init__(self, staff_id, full_name, nationality, role,
                 experience_years, qualifications, franchise_team, salary):
        self.staff_id = staff_id
        self.full_name = full_name
        self.nationality = nationality
        self.role = role
        self.experience_years = int(experience_years)
        self.qualifications = qualifications
        self.franchise_team = franchise_team
        self.salary = float(salary)

    @classmethod
    def from_line(cls, line: str) -> "CoachingStaff":
        return cls(*_parse_line(line, 8))

    def display(self) -> None:
        print(f"  {self.full_name:<24} {self.role:<18} Exp:{self.experience_years:>2}y")

    def __str__(self) -> str:
        return f"{self.full_name} ({self.role})"


# ─── Venue ───

class Venue:
    def __init__(self, venue_id, stadium_name, city, country,
                 capacity, pitch_type, has_floodlights, matches_hosted):
        self.venue_id = venue_id
        self.stadium_name = stadium_name
        self.city = city
        self.country = country
        self.capacity = int(capacity)
        self.pitch_type = pitch_type
        self.has_floodlights = str(has_floodlights).strip().lower() in {"1", "true", "yes"}
        self.matches_hosted = int(matches_hosted)

    @classmethod
    def from_line(cls, line: str) -> "Venue":
        return cls(*_parse_line(line, 8))

    def display(self) -> None:
        lights = "Yes" if self.has_floodlights else "No"
        print(f"  {self.stadium_name:<38} {self.city:<12} "
              f"Cap:{self.capacity:<6} Pitch:{self.pitch_type:<17} Lights:{lights}")

    def __str__(self) -> str:
        return f"{self.stadium_name}, {self.city}"


# ─── Franchise ───

class Franchise:
    def __init__(self, franchise_id, team_name, city, home_ground, owner,
                 titles_won, matches_played, matches_won, matches_lost,
                 net_run_rate, points, jersey_color, founded_year):
        self.franchise_id = franchise_id
        self.team_name = team_name
        self.city = city
        self.home_ground = home_ground
        self.owner = owner
        self.titles_won = int(titles_won)
        self.matches_played = int(matches_played)
        self.matches_won = int(matches_won)
        self.matches_lost = int(matches_lost)
        self.net_run_rate = float(net_run_rate)
        self.points = int(points)
        self.jersey_color = jersey_color
        self.founded_year = int(founded_year)
        self.squad: list[Player] = []
        self.staff: list[CoachingStaff] = []

    @classmethod
    def from_line(cls, line: str) -> "Franchise":
        return cls(*_parse_line(line, 13))

    def update_result(self, won: bool, nrr_change: float) -> None:
        self.matches_played += 1
        self.net_run_rate = round(self.net_run_rate + nrr_change, 2)
        if won:
            self.matches_won += 1
            self.points += 2
        else:
            self.matches_lost += 1

    def display_squad(self) -> None:
        print(f"\n  Squad ({len(self.squad)} players)")
        print(f"  {'-' * 68}")
        for player in sorted(self.squad, reverse=True):
            player.display()

    def display_staff(self) -> None:
        print(f"\n  Coaching Staff ({len(self.staff)} members)")
        print(f"  {'-' * 50}")
        for s in self.staff:
            s.display()

    def display(self) -> None:
        print(f"  {self.team_name:<22} City:{self.city:<12} "
              f"P:{self.matches_played:<3} W:{self.matches_won:<3} "
              f"L:{self.matches_lost:<3} NRR:{self.net_run_rate:>6.2f} Pts:{self.points}")

    def __bool__(self) -> bool:
        return True

    def __len__(self) -> int:
        return len(self.squad)

    def __str__(self) -> str:
        return self.team_name


# ─── Match ───

class Match:
    def __init__(self, match_id: str, team_a: Franchise, team_b: Franchise,
                 venue: Venue, match_date: str, match_type: str) -> None:
        self.match_id = match_id
        self.team_a = team_a
        self.team_b = team_b
        self.venue = venue
        self.match_date = match_date
        self.match_type = match_type
        self.score_a = self.score_b = 0
        self.wickets_a = self.wickets_b = 0
        self.result = ""
        self.is_completed = False

    def simulate_match(self) -> None:
        self.score_a = random.randint(110, 220)
        self.score_b = random.randint(110, 220)
        self.wickets_a = random.randint(1, 10)
        self.wickets_b = random.randint(1, 10)

        winner = self.team_a if self.score_a >= self.score_b else self.team_b
        self.result = f"{winner} won by {abs(self.score_a - self.score_b)} runs"
        self.is_completed = True

        nrr_delta = round((self.score_a - self.score_b) / 100.0, 2)
        self.team_a.update_result(self.score_a >= self.score_b, nrr_delta)
        self.team_b.update_result(self.score_b > self.score_a, -nrr_delta)
        self.venue.matches_hosted += 1

    def display_scorecard(self) -> None:
        if not self.is_completed:
            print(f"  {self.match_id}: not completed yet")
            return
        print(f"  {self.match_id} | {self.team_a} vs {self.team_b} | {self.venue}\n"
              f"    {self.team_a.franchise_id}: {self.score_a}/{self.wickets_a}  "
              f"{self.team_b.franchise_id}: {self.score_b}/{self.wickets_b}\n"
              f"    Result: {self.result}")

    def __str__(self) -> str:
        return f"{self.match_id}: {self.team_a} vs {self.team_b} @ {self.venue}"


# ─── PSL System ───

class PSL:
    def __init__(self, season: str, year: int) -> None:
        self._season = season
        self._year = year
        self._franchises: list[Franchise] = []
        self._venues: list[Venue] = []
        self._schedule: list[Match] = []

    # ── Generic lookup ──

    def _find_franchise(self, field: str, value: str) -> Franchise | None:
        target = value.strip().lower()
        for team in self._franchises:
            if getattr(team, field).lower() == target:
                return team
        return None

    # ── Loaders ──

    def load_all(self) -> None:
        # Franchises
        self._franchises = []
        for line in _read_lines(DATA_DIR / "teams.txt"):
            try:
                self._franchises.append(Franchise.from_line(line))
            except ValueError as e:
                print(f"  Skipping: {e}")

        # Venues
        self._venues = []
        for line in _read_lines(DATA_DIR / "venues.txt"):
            try:
                self._venues.append(Venue.from_line(line))
            except ValueError as e:
                print(f"  Skipping: {e}")

        # Players → assign to franchise by ID code (PSL-LQ-001 → "LQ")
        for line in _read_lines(DATA_DIR / "players.txt"):
            try:
                player = Player.from_line(line)
                code = player.player_id.split("-")[1] if "-" in player.player_id else ""
                team = self._find_franchise("franchise_id", code)
                if team:
                    team.squad.append(player)
            except ValueError as e:
                print(f"  Skipping: {e}")

        # Coaching staff → assign by franchise name
        for line in _read_lines(DATA_DIR / "coaching_staff.txt"):
            try:
                s = CoachingStaff.from_line(line)
                team = self._find_franchise("team_name", s.franchise_team)
                if team:
                    team.staff.append(s)
            except ValueError as e:
                print(f"  Skipping: {e}")

    # ── City search ──

    def get_available_cities(self) -> list[str]:
        return [t.city for t in self._franchises]

    def display_city_info(self, city: str) -> None:
        team = self._find_franchise("city", city)
        if not team:
            print(f"\n  No franchise found for city: {city}")
            return

        print(f"\n{'=' * 60}")
        print(f"  {team.team_name} ({team.city})")
        print(f"{'=' * 60}")
        print(f"  Owner       : {team.owner}")
        print(f"  Home Ground : {team.home_ground}")
        print(f"  Founded     : {team.founded_year}")
        print(f"  Titles Won  : {team.titles_won}")
        print(f"  Jersey      : {team.jersey_color}")
        print(f"  Record      : P:{team.matches_played} W:{team.matches_won} L:{team.matches_lost}")
        print(f"  NRR         : {team.net_run_rate:+.3f}")

        city_venues = [v for v in self._venues if v.city.lower() == city.strip().lower()]
        if city_venues:
            print(f"\n  Venue(s) in {city}:")
            print(f"  {'-' * 50}")
            for v in city_venues:
                v.display()

        team.display_squad()
        team.display_staff()

    # ── Schedule & simulation ──

    def generate_schedule(self) -> None:
        self._schedule.clear()
        if len(self._franchises) < 2 or not self._venues:
            return
        match_no = 1
        for i in range(len(self._franchises)):
            for j in range(i + 1, len(self._franchises)):
                self._schedule.append(Match(
                    match_id=f"Match {match_no:02d}",
                    team_a=self._franchises[i],
                    team_b=self._franchises[j],
                    venue=self._venues[(match_no - 1) % len(self._venues)],
                    match_date=f"2025-04-{(match_no % 28) + 1:02d}",
                    match_type="Group Stage",
                ))
                match_no += 1

    def run_season(self) -> None:
        if not self._schedule:
            print("  Schedule is empty. Generate schedule first.")
            return
        print("\n--- Simulating Group Stage Matches ---")
        for match in self._schedule:
            match.simulate_match()
            match.display_scorecard()

    # ── Display ──

    def display_points_table(self) -> None:
        sorted_teams = sorted(self._franchises, key=lambda f: (f.points, f.net_run_rate), reverse=True)
        print("\n--- POINTS TABLE ---")
        print(f"  {'Pos':<4}{'Team':<22}{'P':<4}{'W':<4}{'L':<4}{'NRR':<8}{'Pts'}")
        for pos, t in enumerate(sorted_teams, start=1):
            print(f"  {pos:<4}{str(t):<22}{t.matches_played:<4}{t.matches_won:<4}"
                  f"{t.matches_lost:<4}{t.net_run_rate:<8.2f}{t.points}")

    def display_all_venues(self) -> None:
        print("\n--- VENUES ---")
        for v in self._venues:
            v.display()

    def display_all_franchises(self) -> None:
        print("\n--- ALL FRANCHISES ---")
        for t in self._franchises:
            t.display()

    def find_top_player(self, stat: str = "total_runs") -> Player | None:
        all_players = [p for f in self._franchises for p in f.squad]
        return max(all_players, key=lambda p: getattr(p, stat)) if all_players else None
