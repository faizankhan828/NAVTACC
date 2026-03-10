from psl import PSL


def main():
    system = PSL("Season 10", 2025)

    # Load data from embedded Python constants
    system.load_franchises()  # Uses embedded FRANCHISES_DATA
    system.load_players()  # Uses embedded PLAYERS_DATA
    system.load_venues()  # Uses embedded VENUES_DATA
    system.load_coaching_staff()  # Uses embedded COACHING_STAFF_DATA

    print("PSL System")
    print("-" * 30)
    system.display_all_franchises()
    system.display_all_venues()


if __name__ == "__main__":
    main()
