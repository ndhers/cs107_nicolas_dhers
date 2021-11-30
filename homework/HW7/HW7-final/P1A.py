from Markov import Markov


weather_today = Markov()
weather_today.load_data()
print(
    f"The probability that a windy day follows a cloudy day is given by {weather_today.get_prob('cloudy','windy')}.")
