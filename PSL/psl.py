from pathlib import Path


def _to_bool(text: str) -> bool:
	return text.strip().lower() in {"1", "true", "yes", "y"}


class Player:
	def __init__(self) -> None:
		self._player_id = ""
		self._full_name = ""
		self._nationality = ""
		self._age = 0
		self._role = ""
		self._batting_style = ""
		self._bowling_style = ""
		self._total_runs = 0
		self._total_wickets = 0
		self._matches_played = 0
		self._batting_avg = 0.0
		self._bowling_avg = 0.0
		self._salary = 0.0
		self._is_captain = False

	@classmethod
	def from_data(
		cls,
		player_id: str,
		full_name: str,
		nationality: str,
		age: str,
		role: str,
		bat_style: str,
		bowl_style: str,
		runs: str,
		wickets: str,
		matches: str,
		salary: str,
	) -> "Player":
		p = cls()
		p._player_id = player_id.strip()
		p._full_name = full_name.strip()
		p._nationality = nationality.strip()
		p._age = int(age)
		p._role = role.strip()
		p._batting_style = bat_style.strip()
		p._bowling_style = bowl_style.strip()
		p.total_runs = int(runs)
		p.total_wickets = int(wickets)
		p._matches_played = int(matches)
		p.salary = float(salary)
		p.compute_averages()
		return p

	@classmethod
	def load_from_line(cls, line: str) -> "Player":
		parts = [x.strip() for x in line.split("|")]
		if len(parts) != 11:
			raise ValueError(f"Malformed player line: {line}")
		return cls.from_data(*parts)

	@property
	def player_id(self) -> str:
		return self._player_id

	@property
	def full_name(self) -> str:
		return self._full_name

	@property
	def role(self) -> str:
		return self._role

	@property
	def total_runs(self) -> int:
		return self._total_runs

	@total_runs.setter
	def total_runs(self, value: int) -> None:
		if value < 0:
			raise ValueError("Runs cannot be negative")
		self._total_runs = value

	@property
	def total_wickets(self) -> int:
		return self._total_wickets

	@total_wickets.setter
	def total_wickets(self, value: int) -> None:
		if value < 0:
			raise ValueError("Wickets cannot be negative")
		self._total_wickets = value

	@property
	def matches_played(self) -> int:
		return self._matches_played

	@property
	def batting_avg(self) -> float:
		return self._batting_avg

	@property
	def bowling_avg(self) -> float:
		return self._bowling_avg

	@property
	def salary(self) -> float:
		return self._salary

	@salary.setter
	def salary(self, value: float) -> None:
		if value < 0:
			raise ValueError("Salary cannot be negative")
		self._salary = value

	def compute_averages(self) -> None:
		if self._matches_played > 0:
			self._batting_avg = round(self._total_runs / self._matches_played, 2)
			if self._total_wickets > 0:
				self._bowling_avg = round(self._matches_played / self._total_wickets, 2)
			else:
				self._bowling_avg = 0.0
		else:
			self._batting_avg = 0.0
			self._bowling_avg = 0.0

	def display(self) -> None:
		print(
			f"{self._full_name:<24} {self._role:<14} Runs:{self._total_runs:<5} "
			f"Wkts:{self._total_wickets:<4} Avg:{self._batting_avg:<6}"
		)

	def __eq__(self, other: object) -> bool:
		if not isinstance(other, Player):
			return NotImplemented
		return self._player_id == other._player_id

	def __lt__(self, other: "Player") -> bool:
		return self._total_runs < other._total_runs

	def __str__(self) -> str:
		return f"{self._full_name} ({self._role})"


class CoachingStaff:
	def __init__(self) -> None:
		self._staff_id = ""
		self._full_name = ""
		self._nationality = ""
		self._role = ""
		self._experience_years = 0
		self._qualifications = ""
		self._franchise_team = ""
		self._salary = 0.0

	@classmethod
	def from_data(
		cls,
		staff_id: str,
		full_name: str,
		nationality: str,
		role: str,
		experience_years: str,
		qualifications: str,
		franchise_team: str,
		salary: str,
	) -> "CoachingStaff":
		s = cls()
		s._staff_id = staff_id.strip()
		s._full_name = full_name.strip()
		s._nationality = nationality.strip()
		s._role = role.strip()
		s._experience_years = int(experience_years)
		s._qualifications = qualifications.strip()
		s._franchise_team = franchise_team.strip()
		s.salary = float(salary)
		return s

	@classmethod
	def load_from_line(cls, line: str) -> "CoachingStaff":
		parts = [x.strip() for x in line.split("|")]
		if len(parts) != 8:
			raise ValueError(f"Malformed staff line: {line}")
		return cls.from_data(*parts)

	@property
	def full_name(self) -> str:
		return self._full_name

	@property
	def role(self) -> str:
		return self._role

	@property
	def franchise_team(self) -> str:
		return self._franchise_team

	@property
	def salary(self) -> float:
		return self._salary

	@salary.setter
	def salary(self, value: float) -> None:
		if value < 0:
			raise ValueError("Salary cannot be negative")
		self._salary = value

	def display(self) -> None:
		print(f"{self._full_name:<24} {self._role:<18} Exp:{self._experience_years:>2}y")

	def __str__(self) -> str:
		return f"{self._full_name} ({self._role})"


class Franchise:
	def __init__(self, franchise_id: str = "", team_name: str = "", city: str = "", owner: str = "") -> None:
		self._franchise_id = franchise_id
		self._team_name = team_name
		self._city = city
		self._owner = owner
		self._titles_won = 0
		self._matches_played = 0
		self._matches_won = 0
		self._matches_lost = 0
		self._net_run_rate = 0.0
		self._points = 0
		self._squad: list[Player] = []
		self._staff: list[CoachingStaff] = []

	@property
	def franchise_id(self) -> str:
		return self._franchise_id

	@property
	def team_name(self) -> str:
		return self._team_name

	@property
	def matches_played(self) -> int:
		return self._matches_played

	@property
	def matches_won(self) -> int:
		return self._matches_won

	@property
	def matches_lost(self) -> int:
		return self._matches_lost

	@property
	def net_run_rate(self) -> float:
		return self._net_run_rate

	@property
	def points(self) -> int:
		return self._points

	@property
	def squad(self) -> list[Player]:
		return self._squad

	def add_player(self, player: Player) -> None:
		if len(self._squad) < 25:
			self._squad.append(player)

	def add_staff(self, staff_member: CoachingStaff) -> None:
		self._staff.append(staff_member)

	def remove_player(self, player_id: str) -> None:
		self._squad = [p for p in self._squad if p.player_id != player_id]

	def find_player(self, name: str) -> Player | None:
		target = name.strip().lower()
		for player in self._squad:
			if player.full_name.lower() == target:
				return player
		return None

	def update_result(self, won: bool, nrr_change: float) -> None:
		self._matches_played += 1
		self._net_run_rate = round(self._net_run_rate + nrr_change, 2)
		if won:
			self._matches_won += 1
			self._points += 2
		else:
			self._matches_lost += 1

	def display_squad(self) -> None:
		print(f"\nSquad - {self._team_name} ({len(self._squad)} players)")
		print("-" * 70)
		for player in sorted(self._squad, reverse=True):
			player.display()

	def display_staff(self) -> None:
		print(f"\nStaff - {self._team_name}")
		print("-" * 50)
		for staff_member in self._staff:
			staff_member.display()

	def display(self) -> None:
		print(
			f"{self._team_name:<22} City:{self._city:<12} "
			f"P:{self._matches_played:<2} W:{self._matches_won:<2} "
			f"L:{self._matches_lost:<2} NRR:{self._net_run_rate:>5.2f} Pts:{self._points}"
		)

	def __bool__(self) -> bool:
		return True

	def __len__(self) -> int:
		return len(self._squad)

	def __contains__(self, player: Player) -> bool:
		return player in self._squad

	def __str__(self) -> str:
		return self._team_name


class Venue:
	def __init__(self) -> None:
		self._venue_id = ""
		self._stadium_name = ""
		self._city = ""
		self._country = ""
		self._capacity = 0
		self._pitch_type = ""
		self._has_floodlights = False
		self._matches_hosted = 0

	@classmethod
	def from_data(
		cls,
		venue_id: str,
		stadium_name: str,
		city: str,
		country: str,
		capacity: str,
		pitch_type: str,
		has_floodlights: str,
		matches_hosted: str,
	) -> "Venue":
		v = cls()
		v._venue_id = venue_id.strip()
		v._stadium_name = stadium_name.strip()
		v._city = city.strip()
		v._country = country.strip()
		v._capacity = int(capacity)
		v._pitch_type = pitch_type.strip()
		v._has_floodlights = _to_bool(has_floodlights)
		v._matches_hosted = int(matches_hosted)
		return v

	@classmethod
	def load_from_line(cls, line: str) -> "Venue":
		parts = [x.strip() for x in line.split("|")]
		if len(parts) != 8:
			raise ValueError(f"Malformed venue line: {line}")
		return cls.from_data(*parts)

	@property
	def city(self) -> str:
		return self._city

	@property
	def stadium_name(self) -> str:
		return self._stadium_name

	def increment_matches_hosted(self) -> None:
		self._matches_hosted += 1

	def display(self) -> None:
		lights = "Yes" if self._has_floodlights else "No"
		print(
			f"{self._stadium_name:<28} {self._city:<12} "
			f"Cap:{self._capacity:<6} Pitch:{self._pitch_type:<17} Lights:{lights}"
		)

	def __str__(self) -> str:
		return f"{self._stadium_name}, {self._city}"


class Match:
	def __init__(
		self,
		match_id: str,
		team_a: Franchise,
		team_b: Franchise,
		venue: Venue,
		match_date: str,
		match_type: str,
	) -> None:
		self._match_id = match_id
		self._team_a = team_a
		self._team_b = team_b
		self._venue = venue
		self._match_date = match_date
		self._match_type = match_type
		self._score_a = 0
		self._score_b = 0
		self._wickets_a = 0
		self._wickets_b = 0
		self._result = ""
		self._is_completed = False

	def simulate_match(self) -> None:
		self._score_a = random.randint(110, 220)
		self._score_b = random.randint(110, 220)
		self._wickets_a = random.randint(1, 10)
		self._wickets_b = random.randint(1, 10)

		if self._score_a >= self._score_b:
			winner = self._team_a
		else:
			winner = self._team_b

		diff = abs(self._score_a - self._score_b)
		self._result = f"{winner} won by {diff} runs"
		self._is_completed = True

		nrr_delta = round((self._score_a - self._score_b) / 100.0, 2)
		self._team_a.update_result(self._score_a >= self._score_b, nrr_delta)
		self._team_b.update_result(self._score_b > self._score_a, -nrr_delta)
		self._venue.increment_matches_hosted()

	def get_winner(self) -> Franchise | None:
		if not self._is_completed:
			return None
		return self._team_a if self._score_a >= self._score_b else self._team_b

	def display_scorecard(self) -> None:
		if not self._is_completed:
			print(f"{self._match_id}: not completed yet")
			return
		print(
			f"{self._match_id} | {self._team_a} vs {self._team_b} | {self._venue}\n"
			f"  {self._team_a.franchise_id}: {self._score_a}/{self._wickets_a}  "
			f"{self._team_b.franchise_id}: {self._score_b}/{self._wickets_b}\n"
			f"  Result: {self._result}"
		)

	def __str__(self) -> str:
		return f"{self._match_id}: {self._team_a} vs {self._team_b} @ {self._venue}"


class PSL:
	def __init__(self, season: str, year: int) -> None:
		self._season = season
		self._year = year
		self._franchises: list[Franchise] = []
		self._venues: list[Venue] = []
		self._schedule: list[Match] = []

	def add_franchise(self, franchise: Franchise) -> None:
		self._franchises.append(franchise)

	def _find_franchise_by_id_code(self, code: str) -> Franchise | None:
		code = code.strip().upper()
		for team in self._franchises:
			if team.franchise_id.upper() == code:
				return team
		return None

	def _find_franchise_by_name(self, team_name: str) -> Franchise | None:
		target = team_name.strip().lower()
		for team in self._franchises:
			if team.team_name.lower() == target:
				return team
		return None

	def load_franchises(self, filename: str | None = None) -> None:
		self._franchises = []

		# Default source: franchise data defined in franchise.py
		if filename is None:
			from franchise import FRANCHISES_DATA, Franchise as ExternalFranchise

			for line in FRANCHISES_DATA:
				try:
					franchise = ExternalFranchise.from_line(line)
					self._franchises.append(franchise)
				except ValueError:
					print(f"Skipping malformed franchise row: {line}")
			return

		path = Path(filename)
		if not path.exists():
			print(f"Warning: {filename} not found.")
			return
		with path.open("r", encoding="utf-8") as fh:
			from franchise import Franchise as ExternalFranchise

			for raw in fh:
				line = raw.strip()
				if not line or line.startswith("#"):
					continue
				try:
					franchise = ExternalFranchise.from_line(line)
					self._franchises.append(franchise)
				except ValueError:
					print(f"Skipping malformed franchise row: {line}")

	def load_venues(self, filename: str | None = None) -> None:
		self._venues = []

		# Default source: venues data defined in venue.py
		if filename is None:
			from venue import VENUES_DATA

			for line in VENUES_DATA:
				try:
					self._venues.append(Venue.load_from_line(line))
				except ValueError:
					print(f"Skipping malformed venue row: {line}")
			return

		path = Path(filename)
		if not path.exists():
			print(f"Warning: {filename} not found.")
			return
		with path.open("r", encoding="utf-8") as fh:
			for raw in fh:
				line = raw.strip()
				if not line or line.startswith("#"):
					continue
				try:
					self._venues.append(Venue.load_from_line(line))
				except ValueError:
					print(f"Skipping malformed venue row: {line}")

	def load_players(self, filename: str | None = None) -> None:
		# Default source: player data defined in player.py
		if filename is None:
			from player import PLAYERS_DATA, Player as ExternalPlayer

			for line in PLAYERS_DATA:
				try:
					player = ExternalPlayer.from_line(line)
				except ValueError:
					print(f"Skipping malformed player row: {line}")
					continue

				parts = [x.strip() for x in line.split("|")]
				# Format: PSL-XX-001 -> XX is franchise code.
				code = parts[0].split("-")[1] if "-" in parts[0] else ""
				team = self._find_franchise_by_id_code(code)
				if team:
					team.add_player(player)
			return

		path = Path(filename)
		if not path.exists():
			print(f"Warning: {filename} not found.")
			return
		with path.open("r", encoding="utf-8") as fh:
			for raw in fh:
				line = raw.strip()
				if not line or line.startswith("#"):
					continue
				try:
					player = Player.load_from_line(line)
				except ValueError:
					print(f"Skipping malformed player row: {line}")
					continue

				parts = [x.strip() for x in line.split("|")]
				# Format: PSL-XX-001 -> XX is franchise code.
				code = parts[0].split("-")[1] if "-" in parts[0] else ""
				team = self._find_franchise_by_id_code(code)
				if team:
					team.add_player(player)

	def load_coaching_staff(self, filename: str | None = None) -> None:
		self.staff = []

		# Default source: coaching staff data defined in coaching_staff.py
		if filename is None:
			from coaching_staff import COACHING_STAFF_DATA, CoachingStaff as ExternalCoachingStaff

			for line in COACHING_STAFF_DATA:
				try:
					staff_member = ExternalCoachingStaff.from_line(line)
					self.staff.append(staff_member)
				except ValueError:
					print(f"Skipping malformed staff row: {line}")
			self._assign_staff_to_franchises()
			return

		path = Path(filename)
		if not path.exists():
			print(f"Warning: {filename} not found.")
			return
		with path.open("r", encoding="utf-8") as fh:
			for raw in fh:
				line = raw.strip()
				if not line or line.startswith("#"):
					continue
				try:
					staff = CoachingStaff.from_line(line)
					self.staff.append(staff)
				except ValueError:
					print(f"Skipping malformed staff row: {line}")
					continue
		self._assign_staff_to_franchises()

	def _assign_staff_to_franchises(self) -> None:
		"""Assign coaching staff to their respective franchises based on franchise name."""
		for staff_member in self.staff:
			franchise = self._find_franchise_by_name(staff_member.franchise_name)
			if franchise:
				franchise.add_staff(staff_member)

	def generate_schedule(self) -> None:
		self._schedule.clear()
		if len(self._franchises) < 2 or not self._venues:
			return

		match_no = 1
		for i in range(len(self._franchises)):
			for j in range(i + 1, len(self._franchises)):
				venue = self._venues[(match_no - 1) % len(self._venues)]
				match = Match(
					match_id=f"Match {match_no:02d}",
					team_a=self._franchises[i],
					team_b=self._franchises[j],
					venue=venue,
					match_date=f"2025-04-{(match_no % 28) + 1:02d}",
					match_type="Group Stage",
				)
				self._schedule.append(match)
				match_no += 1

	def run_season(self) -> None:
		if not self._schedule:
			print("Schedule is empty. Generate schedule first.")
			return
		print("\n--- Simulating Group Stage Matches ---")
		for match in self._schedule:
			match.simulate_match()
			match.display_scorecard()

	def display_points_table(self) -> None:
		sorted_teams = sorted(
			self._franchises,
			key=lambda f: (f.points, f.net_run_rate),
			reverse=True,
		)
		print("\n--- POINTS TABLE ---")
		print(f"{'Pos':<4}{'Team':<22}{'P':<4}{'W':<4}{'L':<4}{'NRR':<8}{'Pts'}")
		for pos, team in enumerate(sorted_teams, start=1):
			print(
				f"{pos:<4}{str(team):<22}{team.matches_played:<4}"
				f"{team.matches_won:<4}{team.matches_lost:<4}"
				f"{team.net_run_rate:<8.2f}{team.points}"
			)

	def display_all_venues(self) -> None:
		print("\n--- VENUES ---")
		for venue in self._venues:
			venue.display()

	def display_all_franchises(self) -> None:
		print("\n--- FRANCHISES ---")
		for team in self._franchises:
			team.display()
			team.display_squad()
			team.display_staff()

	def find_top_scorer(self) -> Player | None:
		all_players = [player for f in self._franchises for player in f.squad]
		return max(all_players, key=lambda p: p.total_runs) if all_players else None

	def find_top_wicket_taker(self) -> Player | None:
		all_players = [player for f in self._franchises for player in f.squad]
		return max(all_players, key=lambda p: p.total_wickets) if all_players else None


def print_banner() -> None:
	print("=" * 58)
	print("   PSL SEASON 10 MANAGEMENT SYSTEM  |  Python OOP")
	print("=" * 58)


def seed_default_franchises(league: PSL) -> None:
	defaults = [
		("LQ", "Lahore Qalandars", "Lahore", "Fawad Rana"),
		("KK", "Karachi Kings", "Karachi", "Salman Iqbal"),
		("IU", "Islamabad United", "Islamabad", "Ali Naqvi"),
		("MS", "Multan Sultans", "Multan", "Ali Tareen"),
		("PZ", "Peshawar Zalmi", "Peshawar", "Javed Afridi"),
		("QG", "Quetta Gladiators", "Quetta", "Nadeem Omar"),
	]
	for code, name, city, owner in defaults:
		league.add_franchise(Franchise(code, name, city, owner))


def main() -> None:
	league = PSL("Season 10", 2025)
	seed_default_franchises(league)

	league.load_venues("data/venues.txt")
	league.load_players("data/players.txt")
	league.load_coaching_staff("data/coaching_staff.txt")
	league.generate_schedule()

	print_banner()
	while True:
		print("\n1. View All Franchises & Squads")
		print("2. View All Venues")
		print("3. Run Full Season Simulation")
		print("4. Display Points Table")
		print("5. Show Top Scorer & Top Wicket-Taker")
		print("0. Exit")

		choice = input("\nEnter choice: ").strip()
		if choice == "1":
			league.display_all_franchises()
		elif choice == "2":
			league.display_all_venues()
		elif choice == "3":
			league.run_season()
		elif choice == "4":
			league.display_points_table()
		elif choice == "5":
			top_scorer = league.find_top_scorer()
			top_bowler = league.find_top_wicket_taker()
			print(f"Top Scorer: {top_scorer if top_scorer else 'N/A'}")
			print(f"Top Wicket-Taker: {top_bowler if top_bowler else 'N/A'}")
		elif choice == "0":
			print("Goodbye")
			break
		else:
			print("Invalid choice. Try again.")


if __name__ == "__main__":
	main()
