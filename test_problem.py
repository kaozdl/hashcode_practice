def generate_column(string):
    return [x for x in string if x != '\n']

class Pizza():
    def __init__(self):
        inp = open('a_example.in','r')
        restrictions = [int(x) for x in inp.readline().replace('\n','').split(' ')]
        self.rows = restrictions[0]
        self.columns = restrictions[1]
        self.minumum = restrictions[2]
        self.max_cells = restrictions[3]
        rows = inp.readlines()
        self.pizza = []
        for row in rows:
            self.pizza.append(generate_column(row))
        

