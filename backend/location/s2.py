from math import radians, sin, cos, sqrt, atan2
import s2sphere
import string

def haversine(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude to radians
    rlat1, rlon1, rlat2, rlon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula to calculate distance between two points
    dlat = rlat2 - rlat1
    dlon = rlon2 - rlon1
    a = sin(dlat/2)**2 + cos(rlat1) * cos(rlat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    r = 6371 # Radius of Earth in kilometers
    distance = r * c
    return distance

if __name__ == "__main__":
    print("Eiffel Tower: 48.858093, 2.294694")

    lat, lon, altitud, resolution = 48.858093, 2.294694, 1000, 1000
    
    # Encode including altitude
    point = s2sphere.LatLng.from_degrees(lat, lon)
    cell = s2sphere.CellId.from_lat_lng(point)
    encoded = cell.to_token() # + "@" + str(altitud)

    # Decode
    cell = s2sphere.CellId.from_token(encoded) #.split("@")[0]
    decoded = cell.to_lat_lng()


    for i in range(1, 30):

        distance = haversine(lat, lon, cell.parent(i).to_lat_lng().lat().degrees, cell.parent(i).to_lat_lng().lng().degrees) * 1000 # convert to meters

        hello = cell.parent(i)
        

        print(f"Level {i:2}: {str(hello).upper()} - m: {distance:.10} - {cell.parent(i).to_lat_lng()}")

        # get the exact area of the cell using s2sphere
        center_lat, center_lon = cell.parent(i).to_lat_lng().lat().degrees, cell.parent(i).to_lat_lng().lng().degrees

        # measure the error of the cell

        # error = haversine(lat, lon, center_lat, center_lon) * 1000 # convert to meters

    print(encoded)

    print(decoded)
