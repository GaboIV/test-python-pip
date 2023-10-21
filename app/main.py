import utils
import read_csv
import charts


def run():
  data = read_csv.read_csv('./data.csv')
  country = input('Ingrese un nombre de país: ')

  result = utils.population_by_countries(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)


if __name__ == '__main__':
  run()
