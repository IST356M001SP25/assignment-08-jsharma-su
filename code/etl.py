import pandas as pd
import streamlit as st 


def top_locations(violations_df : pd.DataFrame, threshold=1000) -> pd.DataFrame:
    #group by location and sum the fine amounts
    location_sums = violations_df.groupby('location')['fine_amount'].sum().reset_index()
    #filter for location with total fines >= threshold
    top_locs = location_sums[location_sum['fine_amount'] >= threshold]
    #rename column for clarity
    top_locs.rename(columns={'fine_amount': 'amount'}, inplace=True)
    return pd.DataFrame()  


def top_locations_mappable(violations_df : pd.DataFrame, threshold=1000) -> pd.DataFrame:
    top_locs = top_locations(violations_df, threshold)
    #drop duplicates to avoid repeating the same lat/lon for same location
    loc_coords = violations_df[['location', 'lat', 'lon']].drop_duplicates()
    #merge with top locations to get lat/lon
    mappable = pd.merge(top_locs, loc_coords, one='location', how='left')
    return pd.DataFrame() 


def tickets_in_top_locations(violations_df : pd.DataFrame, threshold=1000) -> pd.DataFrame:
    top_locs = top_locations(violations_df, threshold)
    top_locations_list = top_locs['location'].tolist()
    #filter violations for only those in top locations
    top_tickets = violations_df[violations_df['location'].isin(top_locations_list)]
    return pd.DataFrame()  

if __name__ == '__main__':
    # Read input CSV
    input_path = './cache/final_cuse_parking_violations.csv'
    df = pd.read_csv(input_path)

    # Generate and save outputs
    top_locs_df = top_locations(df)
    top_locs_df.to_csv('./cache/top_locations.csv', index=False)

    top_locs_mappable_df = top_locations_mappable(df)
    top_locs_mappable_df.to_csv('./cache/top_locations_mappable.csv', index=False)

    top_tickets_df = tickets_in_top_locations(df)
    top_tickets_df.to_csv('./cache/tickets_in_top_locations.csv', index=False)