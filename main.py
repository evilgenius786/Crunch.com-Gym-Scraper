import pandas as pd
import requests


def main():
    url = 'https://www.crunch.com/load-clubs'
    res = requests.get(url).json()
    df = []
    for club in res['clubs']:
        row = {
            'id': club['id'],
            'name': club['name'],
            'club_type': club['club_type'],
            'slug': club['slug'],
            'map_image_url': club['map_image_url']['original'],
            'distance_away': club['distance_away'],
            'distance_away_string': club['distance_away_string'],
            'address_1': club['address']['address_1'],
            'address_2': club['address']['address_2'],
            'city': club['address']['city'],
            'state': club['address']['state'],
            'zip': club['address']['zip'],
            'country_code': club['address']['country_code'],
            'phone': club['phone'],
            'email': club['email'],
            'status': club['status'],
            'status_code': club['status_code'],
            'latitude': club['latitude'],
            'longitude': club['longitude'],
            'published_time': club['published_time'],
            'time_zone': club['time_zone'],
            'front_desk_email': club['front_desk_email'],
            'executive_email': club['executive_email'],
            'reporting_id': club['reporting_id'],
            'online_reservations': club['online_reservations'],
            'ideawork_id': club['ideawork_id'],
            'mms_id': club['mms_id'],
            'mms_api': club['mms_api'],
            'mms_instance': club['mms_instance'],
            'late_cancel_fee_amount': club['late_cancel_fee_amount'],
            'preferred_locale': club['preferred_locale'],
            'facebook_url': club['facebook_url'],
            'facebook_handle': club['facebook_handle'],
            'instagram_url': club['instagram_url'],
            'instagram_handle': club['instagram_handle'],
            'twitter_url': club['twitter_url'],
            'twitter_handle': club['twitter_handle'],
            'no_show_late_cancel_fees': club['no_show_late_cancel_fees'],
            'fee_configuration': club['fee_configuration'],
            'crunch_o_meter': club['crunch_o_meter'],
            'apple_watch_connected': club['apple_watch_connected'],
            'occupancy_status': club['occupancy_status'],
            'ownership_group_id': club['ownership_group']['id'],
            'ownership_group_name': club['ownership_group']['name']
        }
        df.append(row)
    df = pd.DataFrame(df)
    df.to_csv('crunch_clubs.csv', index=False)


if __name__ == '__main__':
    main()
