from queue import PriorityQueue
from dists import dists, straight_line_dists_from_bucharest

# goal sempre sera 'bucharest'


def a_star(start, goal='Bucharest'):
    """
    Retorna uma lista com o caminho de start até 
    goal segundo o algoritmo A*
    """
    border = PriorityQueue()
    exploited = {}
    cities = dists
    heuristics = straight_line_dists_from_bucharest
    dist = 0

    border.put((evaluation_function(dist, heuristics[start]), start, [start]))
    exploited[start] = evaluation_function(dist, heuristics[start])

    while is_bucharest(border):
        (evaluation, node, road) = border.get()
        if node == goal:
            return road
        for next_node in cities[node]:
            city_name = next_node[0]
            city_dist = next_node[1]
            new_evaluation = evaluation_function(
                city_dist, heuristics[city_name])

            if city_name not in exploited or evaluation >= new_evaluation:
                exploited[city_name] = new_evaluation
                border.put((new_evaluation, city_name, road + [city_name]))
                dist = city_dist + dist


def is_bucharest(priority_queue: PriorityQueue):
    """Verifica se a lista de prioridades não está vazia.
    Ou seja, se todos os nós já foram avaliados."""
    return not priority_queue.empty()


def evaluation_function(cost, heuristic):
    """Realiza soma de custo e heurística para
    função de avaliação."""
    return cost + heuristic

def main():
    origin = ''
    while origin not in dists.keys():
        origin = input('Digite a origem: ').capitalize()
    road = a_star(origin)
    print('Caminho encontrado por busca A*')
    print(' -> '.join(city for city in road))

if __name__ == '__main__':
    main()
