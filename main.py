from fm_ingest import get_competitions, save_matches_to_csv


def main():
    print("=== FixtureMind core ===")

    comps = get_competitions()
    print("Available competitions (first 10):")
    print(comps[["competition_id", "season_id", "competition_name", "season_name"]].head(10))

    first = comps.iloc[0]
    comp_id = int(first["competition_id"])
    season_id = int(first["season_id"])

    csv_path = save_matches_to_csv(comp_id, season_id)
    print(f"\nSaved matches for comp={comp_id}, season={season_id} to {csv_path}")


if __name__ == "__main__":
    main()
