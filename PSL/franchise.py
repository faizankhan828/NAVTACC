# PSL Franchise (Team) Data
# Format: FranchiseID|TeamName|City|HomeGround|Owner|TitlesWon|MatchesPlayed|MatchesWon|MatchesLost|NetRunRate|Points|JerseyColor|Founded
FRANCHISES_DATA = [
    "LQ|Lahore Qalandars|Lahore|Gaddafi Stadium|Fawad Rana|1|98|52|46|+0.142|0|Green and Black|2015",
    "KK|Karachi Kings|Karachi|National Stadium|Salman Iqbal|1|98|47|51|-0.089|0|Blue and Gold|2015",
    "MS|Multan Sultans|Multan|Multan Cricket Stadium|Ali Khan Tareen|2|62|38|24|+0.312|0|Purple and Gold|2018",
    "PZ|Peshawar Zalmi|Peshawar|Arbab Niaz Stadium|Javed Afridi|1|98|50|48|+0.056|0|Yellow and Orange|2015",
    "IU|Islamabad United|Islamabad|Rawalpindi Cricket Stadium|Ali Naqvi & Amna Naqvi|2|98|55|43|+0.198|0|Red and Navy|2015",
    "QG|Quetta Gladiators|Quetta|Bugti Stadium|Nadeem Omar|1|98|48|50|-0.078|0|Red and Black|2015",
]


class Franchise:
    def __init__(
        self,
        franchise_id,
        team_name,
        city,
        home_ground,
        owner,
        titles_won,
        matches_played,
        matches_won,
        matches_lost,
        net_run_rate,
        points,
        jersey_color,
        founded_year,
    ):
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

        self._squad = []
        self._staff = []
    
    @property
    def squad(self):
        return self._squad
    
    @property
    def players(self):
        return self._squad
    
    @property
    def coaching_staff(self):
        return self._staff

    @classmethod
    def from_line(cls, line):
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != 13:
            raise ValueError(f"Invalid franchise row: {line}")
        return cls(*parts)

    def add_player(self, player):
        self._squad.append(player)

    def add_staff(self, staff):
        self._staff.append(staff)

    def display_squad(self):
        print(f"\nSquad - {self.team_name} ({len(self._squad)} players)")
        print("-" * 70)
        for player in self._squad:
            print(f"{player.full_name:<24} {player.role}")

    def display_staff(self):
        print(f"\nStaff - {self.team_name}")
        print("-" * 50)
        for staff_member in self._staff:
            print(f"{staff_member.full_name:<24} {staff_member.role}")

    def display(self):
        print(
            f"{self.team_name:<22} City:{self.city:<12} "
            f"P:{self.matches_played:<3} W:{self.matches_won:<3} "
            f"L:{self.matches_lost:<3} NRR:{self.net_run_rate:>6.2f} Pts:{self.points}"
        )

    def __str__(self):
        return f"{self.team_name} ({self.city})"
