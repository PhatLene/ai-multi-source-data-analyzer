import pandas as pd


def load_dataset(file_path: str) -> pd.DataFrame:
    """Load the unified profile dataset."""
    return pd.read_csv(file_path)


def safe_get(row: dict, key: str, default=""):
    """Safely return a value from a row dict, replacing NaN with a default."""
    value = row.get(key, default)
    if pd.isna(value):
        return default
    return value


def build_profile_payload(row: dict) -> dict:
    """
    Build a clean, structured payload for the LLM using the current project columns.
    This version intentionally excludes Twitter/X so the project can run without paid X API access.
    """
    return {
        "Person": safe_get(row, "Person"),
        "Citizenship": safe_get(row, "citizenship"),
        "DateOfBirth": safe_get(row, "date_of_birth"),

        "YouTubeChannel": safe_get(row, "YT_ChannelTitle"),
        "YouTubeSubscribers": safe_get(row, "YT_SubscriberCount"),
        "YouTubeTotalVideos": safe_get(row, "YT_TotalVideos"),
        "YouTubeTotalViews": safe_get(row, "YT_TotalViews"),

        "InstagramFollowers": safe_get(row, "InstagramFollowers"),
        "InstagramPosts": safe_get(row, "InstagramPosts"),
        "InstagramBio": safe_get(row, "InstagramBiography"),

        "KnowledgeGraphDescription": safe_get(row, "KG_Description"),
        "KnowledgeGraphSummary": safe_get(row, "KG_DetailedSummary"),

        "WikipediaSummary": safe_get(row, "Wiki_Summary"),
        "WikipediaURL": safe_get(row, "Wiki_URL"),
    }


def prepare_profiles(df: pd.DataFrame, limit: int | None = None) -> list[dict]:
    """Convert a DataFrame into a list of row dictionaries."""
    records = df.to_dict(orient="records")
    if limit is not None:
        records = records[:limit]
    return records
