from GReNMlin import grn, simulator
import numpy as np

class Repressilator:
    def __init__(self, delta_X, delta_Y, delta_Z, Kd, alpha, n):
        self.grn = grn.grn()
        
        self.grn.add_species("X", delta_X)
        self.grn.add_species("Y", delta_Y)
        self.grn.add_species("Z", delta_Z)
        
        # Z represses X
        regulators = [{'name': 'Z', 'type': -1, 'Kd': Kd, 'n': n}]
        products = [{'name': 'X'}]
        self.grn.add_gene(alpha, regulators, products)

        # X represses Y
        regulators = [{'name': 'X', 'type': -1, 'Kd': Kd, 'n': n}]
        products = [{'name': 'Y'}]
        self.grn.add_gene(alpha, regulators, products)

        # Y represses Z
        regulators = [{'name': 'Y', 'type': -1, 'Kd': Kd, 'n': n}]
        products = [{'name': 'Z'}]
        self.grn.add_gene(alpha, regulators, products)
    
    def plot_network(self):
        self.grn.plot_network()
        
    def simulate(self, initial_conditions):
        T, Y = simulator.simulate_single(self.grn, initial_conditions)

if __name__ == "__main__":
    repressilator = Repressilator(delta_X=0.1, delta_Y=0.1, delta_Z=0.1, Kd=1, alpha=10, n=2)
    
    # repressilator.plot_network()
    
    initial_conditions = np.zeros(0)
    repressilator.simulate(initial_conditions)