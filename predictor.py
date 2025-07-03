from datetime import datetime

# Store the simulation's global start time
start_time = datetime.now()

def predict_cost(location, time):
    """
    Predicts time-based friction cost at a given location and time.
    E.g. Higher costs during simulated traffic peak.
    """
    if location == 'B' and 5 <= time.hour < 7:
        return 10  # Peak congestion
    return 1

# Attach start_time as an attribute for use by pfp_search
predict_cost.start_time = start_time
