# Graph without direction and without weight
graph = [
    [1, 2, 5],  # 0 vertex => 1, 0 => 2, 0 => 5
    [0, 2],     # 1 vertex => 0, 1 => 2
    [0, 1, 3],  # 2 vertex => 0, 2 => 1, 2 => 3
    [2, 4, 5],  # 3 vertex => 2, 3 => 4, 3 => 5
    [3, 5],     # 4 vertex => 3, 4 => 5
    [0, 3, 4]   # 5 vertex => 0, 5 => 3, 5 => 4
]


# Graph with direction and without weight
graph = [
    [1],    # 0 vertex => 1
    [2],    # 1 vertex => 2
    [3],    # 2 vertex => 3
    [4],    # 3 vertex => 4
    [5],    # 4 vertex => 5
    [0, 1]   # 5 vertex => 0, 5 => 1
]


# Graph without direction and with weight
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


# Graph with direction and with weight
class Vertex:
    def __init__(self, id):
        self.id = id
        self.directs = {}  # {vert: weight}

    def get_directs(self):
        return list(self.directs.keys())

    def get_cost_to(self, vert):
        if type(vert) == Vertex:
            if vert not in self.directs.keys():
                return
            return self.directs[vert]
        else:
            directs_ids = list(map(lambda v: v.id, self.directs.keys()))
            if vert in directs_ids:
                return self.directs.values()[directs_ids.index(vert)]


class Graph:
    def __init__(self):
        self.vert_dict = []

    def add_vertex(self, vert):
        if type(vert) == Vertex:
            if vert.id not in map(lambda v: v.id, self.vert_dict):
                self.vert_dict.append(vert)

    def add_edge(self, frm, to, cost):
        vert_dict_ids = list(map(lambda v: v.id, self.vert_dict))
        if type(frm) == Vertex:
            if frm not in self.vert_dict:
                return
        else:
            if frm not in vert_dict_ids:
                return
            vert_index = vert_dict_ids.index(frm)
            frm = self.vert_dict[vert_index]
        if type(to) == Vertex:
            if to not in self.vert_dict:
                return
        else:
            if to not in vert_dict_ids:
                return
            vert_index = vert_dict_ids.index(to)
            to = self.vert_dict[vert_index]
        frm.directs[to] = cost
