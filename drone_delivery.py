print("Drone Delivery Simulator")
x1=float(input("Enter starting X coordinate: "))
y1=float(input("Enter starting Y coordinate: "))
x2=float(input("Enter destination X coordinate: "))
y2=float(input("Enter destination Y coordinate: "))
distance = ((x2-x1)**2 + (y2-y1)**2) ** 0.5
speed = 40
time= distance/speed
print("Distance:", round(distance,2))
print("Estimated travel time:", round(time,2), "hours")
