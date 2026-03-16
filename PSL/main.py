from psl import PSL


def print_banner() -> None:
    print("=" * 58)
    print("   PSL SEASON 10 MANAGEMENT SYSTEM  |  Python OOP")
    print("=" * 58)


def city_search_menu(league: PSL) -> None:
    """Let the user pick a city and view that franchise's complete data."""
    cities = league.get_available_cities()
    if not cities:
        print("\n  No franchises loaded.")
        return

    print("\n--- Select a City ---")
    for i, city in enumerate(cities, 1):
        print(f"  {i}. {city}")
    print(f"  0. Back")

    choice = input("\nEnter choice: ").strip()
    if choice == "0":
        return
    if choice.isdigit() and 1 <= int(choice) <= len(cities):
        league.display_city_info(cities[int(choice) - 1])
    else:
        print("  Invalid choice.")


def main() -> None:
    league = PSL("Season 10", 2025)

    # Load all data from .txt files
    league.load_all()

    print_banner()
    while True:
        print("\n1. View All Franchises")
        print("2. View All Venues")
        print("3. Search by City (Team, Players, Coach, Venue)")
        print("4. Display Points Table")
        print("5. Show Top Scorer & Top Wicket-Taker")
        print("0. Exit")

        choice = input("\nEnter choice: ").strip()
        if choice == "1":
            league.display_all_franchises()
        elif choice == "2":
            league.display_all_venues()
        elif choice == "3":
            city_search_menu(league)
        elif choice == "4":
            league.display_points_table()
        elif choice == "5":
            top_scorer = league.find_top_player("total_runs")
            top_bowler = league.find_top_player("total_wickets")
            print(f"  Top Scorer       : {top_scorer if top_scorer else 'N/A'}")
            print(f"  Top Wicket-Taker : {top_bowler if top_bowler else 'N/A'}")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("  Invalid choice. Try again.")


if __name__ == "__main__":
    main()
