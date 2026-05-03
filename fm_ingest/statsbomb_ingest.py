from __future__ import annotations

from pathlib import Path
from typing import Optional

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
    filename: Optional[str] = None,
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
from statsbombpy import sb  # если уже есть импорт – второй не нужен


def get_events(match_id: int):
    """
    Загрузить события для одного матча StatsBomb Open Data.
    Возвращает pandas.DataFrame.
    """
    print(f"Loading events for match_id={match_id} ...")
    events = sb.events(match_id=match_id)
    print(f"Loaded {len(events)} events.")
    return events


def save_events_to_parquet(match_id: int, filename: str | None = None) -> str:
    """
    Сохранить события матча в data/raw/events_*.parquet и вернуть путь.
    """
    import pandas as pd
    from pathlib import Path

    events = get_events(match_id)

    if filename is None:
        filename = f"statsbomb_events_match_{match_id}.parquet"

    out_path = Path("data") / "raw" / filename
    out_path.parent.mkdir(parents=True, exist_ok=True)
    events.to_parquet(out_path, index=False)

    print(f"Saved events to {out_path}")
    return str(out_path)
