import numpy as np


class Markov:
	def __init__(self, day_zero_weather = None):
		self.data = np.array([])
		self.weather =  {'sunny': 0, 'cloudy': 1, 'rainy': 2, 'snowy': 3, 'windy': 4, 'hailing': 5}
		self.day_zero_weather = day_zero_weather
		self._current_day_weather = day_zero_weather

	def load_data(self, file_path='./weather.csv'):
		self.data = np.genfromtxt(file_path, delimiter = ',')

	def get_prob(self, current_day_weather, next_day_weather): 
		if current_day_weather.lower() not in self.weather or next_day_weather.lower() not in self.weather:
			raise Exception("Please enter a valid weather type!")
		else:
			return self.data[self.weather[current_day_weather], self.weather[next_day_weather]]

	def __iter__(self):
		return MarkovIterator(self, self.day_zero_weather)

	def _simulate_weather_for_day(self, day):
		if day < 0:
			raise Exception("Please enter a valid number of days!")
		if day == 0:
			return self._current_day_weather
		for d in range(day):
			next_weather = next(iter(self))
		return next_weather

	def get_weather_for_day(self, day, trials = 10):
		if trials <= 0:
			raise Exception("Please enter a valid number of trials!")
		list_weather = []
		for t in range(trials):
			list_weather.append(self._simulate_weather_for_day(day))
		return list_weather


class MarkovIterator:
    def __init__(self, markov, current_weather):
        self.markov = markov
        self.current = current_weather

    def __iter__(self):
        return self

    def __next__(self):
        proba = [self.markov.get_prob(self.current, w) for w in self.markov.weather]
        self.current = np.random.choice(list(self.markov.weather), p = proba)
        return self.current
