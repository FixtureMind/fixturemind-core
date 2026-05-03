from pathlib import Path

import pandas as pd
from statsbombpy import sb


DATA_DIR = Path(__file__).resolve().parents[1] / "data"
RAW_DIR = DATA_DIR / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)


def get_competitions() -> pd.DataFrame:
    """
    Загрузить список соревнований из StatsBomb Open Data.
    """
    comps = sb.competitions()
    return comps


def get_matches(competition_id: int, season_id: int) -> pd.DataFrame:
    """
    Загрузить матчи для выбранного соревнования и сезона.
    """
    matches = sb.matches(competition_id=competition_id, season_id=season_id)
    return matches


def save_matches_to_csv(
    competition_id: int,
    season_id: int,
    filename: str | None = None,
) -> Path:
    """
    Выгрузить матчи в CSV в data/raw и вернуть путь к файлу.
    """
    matches = get_matches(competition_id, season_id)

    if filename is None:
        filename = f"statsbomb_matches_comp{competition_id}_season{season_id}.csv"

    output_path = RAW_DIR / filename
    matches.to_csv(output_path, index=False)

    return output_path
