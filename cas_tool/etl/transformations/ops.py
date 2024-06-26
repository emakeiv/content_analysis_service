import pandas as pd


def fillna(obj: pd.DataFrame) -> pd.DataFrame:
    obj.fillna(
        {
            "duration": 0,
            "name": "",
            "season": 0,
            "episode": 0,
            "description": "",
            "year:": 0,
            "actors": "",
            "director": "",
            "country": "unknown",
            "content_type": "unknown",
            "imdbid": "unknown",
            "genre": "unknown",
        },
        inplace=True,
    )

    return obj

def types(obj: pd.DataFrame) -> pd.DataFrame:
    try:
        obj["season"].astype(int)
        # obj["episode"].astype(int)
        # obj["year"].astype(int)
        # obj["duration"].astype(float)
    except Exception as e:
        print(f"error occurred: {e}")

    return obj