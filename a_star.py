from dis import dis
import math
from dists import dists, straight_line_dists_from_bucharest

# goal sempre sera 'bucharest'


def a_star(start, goal='Bucharest'):
    """
    Retorna uma lista com o caminho de start até 
    goal segundo o algoritmo A*
    """
    road = []
    border = {}
    heuristics = straight_line_dists_from_bucharest
    cities = dists
    node = start
    dist = 0

    while not is_bucharest(node, goal):
        try:

            for city in cities[node]:
                city_name = city[0]
                total_dist = dist + city[1]
                heuristic = heuristics[city_name]
                value_valuation = valuation_calculation(total_dist, heuristic)
                border[city_name] = [value_valuation, total_dist, heuristic]

            best_city = min(border, key=border.get)
            node = best_city
            dist = border[node][1]
            print(border)
            print(node)
            print(dist)
            border.pop(node)

        except:
            print('Fail')

    return road


def valuation_calculation(cost, heuristic):
    """
    Retorna o valor da função de avaliação,
    a soma entre custo e heurística"""
    return cost + heuristic


def is_bucharest(node, goal):
    """
    Testa se a cidade no nó é o objetivo.
    Se for Bucharest, retorna True;"""
    if node == goal:
        return True
    else:
        return False


a_star('Arad')
