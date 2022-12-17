class Vertex:
    def __init__(self, id):
        self.id = id
        self.adjectives = {}  # {vert: weight}

    def get_adjectives(self):
        return list(self.adjectives.keys())

    def get_cost_to(self, vert):
        if type(vert) == Vertex:
            if vert not in self.adjectives.keys():
                return
            return self.adjectives[vert]
        else:
            adjective_ids = list(map(lambda v: v.id, self.adjectives.keys()))
            if vert in adjective_ids:
                return self.adjectives.values()[adjective_ids.index(vert)]


class Graph:
    def __init__(self):
        self.vert_dict = []

    def add_vertex(self, vert):
        if type(vert) == Vertex:
            if vert.id not in map(lambda v: v.id, self.vert_dict):
                self.vert_dict.append(vert)

    def add_edge(self, first_vert, second_vert, cost):
        if cost < 1:
            raise ValueError('Cost has to be natural digit')
        vert_dict_ids = list(map(lambda v: v.id, self.vert_dict))
        if type(first_vert) == Vertex:
            if first_vert not in self.vert_dict:
                return
        else:
            if first_vert not in vert_dict_ids:
                return
            vert_index = vert_dict_ids.index(first_vert)
            first_vert = self.vert_dict[vert_index]
        if type(second_vert) == Vertex:
            if second_vert not in self.vert_dict:
                return
        else:
            if second_vert not in vert_dict_ids:
                return
            vert_index = vert_dict_ids.index(second_vert)
            second_vert = self.vert_dict[vert_index]
        first_vert.adjectives[second_vert] = cost
        second_vert.adjectives[first_vert] = cost


def findShortPath(source, prev_path=[], prev_weight_sum=0, res=None):
    # {node: {'weight': 10, 'path': [node1, node2, node3]}}
    res = res or {source: {'weight': 0, 'path': []}}
    neighbors = source.get_adjectives()
    for neighbor in neighbors:
        if neighbor in res.keys():
            weight_to_neighbor = source.get_cost_to(neighbor) + prev_weight_sum
            if res[neighbor]['weight'] > weight_to_neighbor:
                res[neighbor] = {
                    'weight': weight_to_neighbor,
                    'path': prev_path + [source]
                }
                findShortPath(
                    neighbor,
                    prev_path=prev_path + [source],
                    prev_weight_sum=weight_to_neighbor,
                    res=res
                )
        else:
            weight_to_neighbor = source.get_cost_to(neighbor) + prev_weight_sum
            res[neighbor] = {
                'weight': weight_to_neighbor,
                'path': prev_path + [source]
            }
            findShortPath(
                neighbor,
                prev_path=prev_path + [source],
                prev_weight_sum=weight_to_neighbor,
                res=res
            )
    return res


node0 = Vertex(0)
node1 = Vertex(1)
node2 = Vertex(2)
node3 = Vertex(3)
node4 = Vertex(4)
node5 = Vertex(5)
node6 = Vertex(6)
node7 = Vertex(7)
node8 = Vertex(8)
graph = Graph()
graph.add_vertex(node0)
graph.add_vertex(node1)
graph.add_vertex(node2)
graph.add_vertex(node3)
graph.add_vertex(node4)
graph.add_vertex(node5)
graph.add_vertex(node6)
graph.add_vertex(node7)
graph.add_vertex(node8)
graph.add_edge(node0, node1, 4)
graph.add_edge(node0, node7, 8)
graph.add_edge(node1, node7, 11)
graph.add_edge(node1, node2, 8)
graph.add_edge(node7, node8, 7)
graph.add_edge(node7, node6, 1)
graph.add_edge(node6, node8, 6)
graph.add_edge(node8, node2, 2)
graph.add_edge(node2, node3, 7)
graph.add_edge(node2, node5, 4)
graph.add_edge(node6, node5, 2)
graph.add_edge(node3, node5, 14)
graph.add_edge(node3, node4, 9)
graph.add_edge(node4, node5, 10)

r = findShortPath(node0)
# {node_id: {'weight': 10, 'path': [node_id1, node_id2, node_id3]}}
print(list(map(lambda node: [
    node.id,
    {
        'weight': r[node]['weight'],
        'path': list(map(lambda n: n.id, r[node]['path']))
    }
], r.keys())))
