from collections import deque 

route_stack = []
current_route = []
bus_queue = deque()
available_buses = []

# Change Route
route_stack.append(current_route)  
current_route = ['Stop A', 'Stop B', 'Stop C']  # New route
route_stack.append(current_route) 
current_route = ['Stop D', 'Stop E']  # Another new route

# Undo Route
if route_stack:
    current_route = route_stack.pop()
    print("Route undone:", current_route)

# Bus Arrivals
bus_queue.append('ALPHA')
bus_queue.append('OMEGA')
bus_queue.append('HORIZON')
print("Buses arrived :", list(bus_queue))

# Bus Departures 
if bus_queue:
    departed = bus_queue.popleft()
    print(f"{departed} has departed.")

# Add new buses Buses
available_buses.append('RITCO')
available_buses.append('VOLCANO')
print("Available Buses:", available_buses)

# Remove Bus
available_buses.remove('RITCO')
print("Available Buses after removal:", available_buses)

# Show Current Route and Buses in Queue
print("Current Route:", current_route)
print("Buses in Queue:", list(bus_queue))