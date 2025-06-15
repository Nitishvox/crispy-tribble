# strategy_model.py
def suggest_strategy(lap_time, tire_wear, weather):
    if tire_wear > 70 or (weather == 'Rainy' and lap_time > 90):
        return "Pit Now"
    elif tire_wear < 30 and weather == 'Clear':
        return "Push Harder"
    else:
        return "Hold Position"
