import pandas as pd
import matplotlib.pyplot as plt
import statistics as stat

data = pd.read_json (r'jobs.json')

min_salaries = data.loc[:, 'min_salary'].to_list()
max_salaries = data.loc[:, 'max_salary'].to_list()
min_salaries.sort()
max_salaries.sort()


min_mean = int(stat.mean(min_salaries))
max_mean = int(stat.mean(max_salaries))
min_median = int(stat.median(min_salaries))
max_median = int(stat.median(max_salaries))

print(f'Średnia dla kwot minimalnych wyniosła {min_mean}')
print(f'Średnia dla kwot maksymalnych wyniosła {max_mean}')
print(f'Mediana dla kwot minimalnych wyniosła {min_median}')
print(f'Mediana dla kwot maksymalnych wyniosła {max_median}')

plt.plot(min_salaries)
plt.plot(max_salaries)
plt.xlabel('Ilość ofert')
plt.ylabel('Kwota ofert')

plt.show()