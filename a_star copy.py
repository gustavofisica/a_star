import math
import dists


# goal sempre sera 'bucharest'
def a_star(start, goal='Bucharest'):
    """
    Retorna uma lista com o caminho de start até 
    goal segundo o algoritmo A*
    """
    road = []
    border = []
    costs = dists.straight_line_dists_from_bucharest
    cities = dists.dists
    node = start

    while not is_bucharest(node, goal):
        try:
            print(cities[node])
            node = goal
        except:
            print('Fail')

    return road


def valuation_calculation(cost, heuristic):
    """
    Retorna o valor da função de avaliação,
    a soma entre custo e heurística"""
    return sum(cost, heuristic)

def is_bucharest(node, goal):
    """
    Testa se a cidade no nó é o objetivo.
    Se for Bucharest, retorna True;"""
    if node == goal:
        return True
    else:
        return False

a_star('Lugoj')
