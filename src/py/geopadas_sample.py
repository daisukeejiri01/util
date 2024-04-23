# library
import geopandas as gpd
from shapely.geometry import Polygon
from geopy.distance import geodesic
import pandas as pd

# functions
def create_circle(center, radius=1.0):
    """
    Create a polygon representing a circle based on a center point and a radius.

    Parameters:
    center (tuple): The latitude and longitude of the center point (lat, lon).
    radius (float): The radius of the circle in kilometers.

    Returns:
    Polygon: A polygon representing the circle.
    """
    lat, lon = center
    circle_points = [
        (geodesic(kilometers=radius).destination((lat, lon), bearing).longitude,
         geodesic(kilometers=radius).destination((lat, lon), bearing).latitude)
        for bearing in range(360)
    ]
    return Polygon(circle_points)


def main():
    """
    Main function to load population data, create a circle of specified radius,
    and calculate the total population within that circle.
    """
    # Load population data (dummy data for example)
    data = {
        'Latitude': [35.681, 35.685, 35.690],
        'Longitude': [139.767, 139.765, 139.770],
        'Population': [1000, 500, 1200]
    }
    df = pd.DataFrame(data)
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df['Longitude'], df['Latitude']))

    # Specify the center coordinates and radius
    center = (35.685, 139.765)  # Example: coordinates of Tokyo Station
    radius_km = 1.0  # Radius of 1 km

    # Generate a circle with a specified radius
    circle = create_circle(center, radius=radius_km)
    circle_gdf = gpd.GeoDataFrame(geometry=[circle], crs="EPSG:4326")

    # Filter points within the circle
    within_circle = gdf[gdf.within(circle)]

    # Calculate the total population within the circle
    total_population = within_circle['Population'].sum()
    print(f"Total population within {radius_km} km: {total_population}")


if __name__ == "__main__":
    main()
