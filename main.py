import pandas as pd
import requests
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def fetch_clubs(url: str) -> list[dict]:
    """Fetch clubs JSON data from API."""
    try:
        res = requests.get(url, timeout=15)
        res.raise_for_status()
        return res.json().get("clubs", [])
    except requests.RequestException as e:
        logging.error(f"Error fetching data: {e}")
        return []


def parse_club(club: dict) -> dict:
    """Extract relevant fields from a single club record."""
    return {
        "id": club.get("id"),
        "name": club.get("name"),
        "club_type": club.get("club_type"),
        "slug": club.get("slug"),
        "map_image_url": club.get("map_image_url", {}).get("original"),
        "distance_away": club.get("distance_away"),
        "distance_away_string": club.get("distance_away_string"),
        "address_1": club.get("address", {}).get("address_1"),
        "address_2": club.get("address", {}).get("address_2"),
        "city": club.get("address", {}).get("city"),
        "state": club.get("address", {}).get("state"),
        "zip": club.get("address", {}).get("zip"),
        "country_code": club.get("address", {}).get("country_code"),
        "phone": club.get("phone"),
        "email": club.get("email"),
        "status": club.get("status"),
        "status_code": club.get("status_code"),
        "latitude": club.get("latitude"),
        "longitude": club.get("longitude"),
        "published_time": club.get("published_time"),
        "time_zone": club.get("time_zone"),
        "front_desk_email": club.get("front_desk_email"),
        "executive_email": club.get("executive_email"),
        "reporting_id": club.get("reporting_id"),
        "online_reservations": club.get("online_reservations"),
        "ideawork_id": club.get("ideawork_id"),
        "mms_id": club.get("mms_id"),
        "mms_api": club.get("mms_api"),
        "mms_instance": club.get("mms_instance"),
        "late_cancel_fee_amount": club.get("late_cancel_fee_amount"),
        "preferred_locale": club.get("preferred_locale"),
        "facebook_url": club.get("facebook_url"),
        "facebook_handle": club.get("facebook_handle"),
        "instagram_url": club.get("instagram_url"),
        "instagram_handle": club.get("instagram_handle"),
        "twitter_url": club.get("twitter_url"),
        "twitter_handle": club.get("twitter_handle"),
        "no_show_late_cancel_fees": club.get("no_show_late_cancel_fees"),
        "fee_configuration": club.get("fee_configuration"),
        "crunch_o_meter": club.get("crunch_o_meter"),
        "apple_watch_connected": club.get("apple_watch_connected"),
        "occupancy_status": club.get("occupancy_status"),
        "ownership_group_id": club.get("ownership_group", {}).get("id"),
        "ownership_group_name": club.get("ownership_group", {}).get("name"),
    }


def main():
    url = "https://www.crunch.com/load-clubs"
    clubs = fetch_clubs(url)

    if not clubs:
        logging.warning("No clubs data retrieved.")
        return

    df = pd.DataFrame([parse_club(club) for club in clubs])

    out_file = Path("crunch_clubs.csv")
    df.to_csv(out_file, index=False)
    logging.info(f"Saved {len(df)} clubs to {out_file}")


if __name__ == "__main__":
    main()