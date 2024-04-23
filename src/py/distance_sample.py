from geopy.distance import geodesic

# 基準地点
base_location = (35.681382, 139.766084)
# 対象地点
target_location = (35.170915, 136.881537)

# 基準地点と対象地点間の距離をメートルで計算
distance_meters = geodesic(base_location, target_location).meters
print(distance_meters)
# 出力: 267993.8255019876

# 基準地点と対象地点間の距離をキロメートルで計算
distance_kilometers = geodesic(base_location, target_location).km
print(distance_kilometers)
# 出力: 267.9938255019876
