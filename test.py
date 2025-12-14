from GReNMlin import grn

my_grn = grn.grn()

my_grn.add_input_species("X1")
my_grn.add_input_species("X2")

my_grn.add_species("Y", 0.1)

regulators = [{'name': 'X1', 'type': -1, 'Kd': 5, 'n': 2},
              {'name': 'X2', 'type': 1, 'Kd': 5, 'n': 3}]

products = [{'name': 'Y'}]

my_grn.add_gene(10, regulators, products)

regulators = [{'name': 'X1', 'type': 1, 'Kd': 5, 'n': 2},
              {'name': 'X2', 'type': -1, 'Kd': 5, 'n': 3}]

my_grn.add_gene(10, regulators, products)

my_grn.plot_network()