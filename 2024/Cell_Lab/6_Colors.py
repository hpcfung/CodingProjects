from math import factorial

class Simulation:
    def __init__(self):
        self.conv = {'green': ('yellow', 'red'),
            'yellow': ('cyan', 'red'),
            'red': ('cyan', 'blue'),
            'cyan': ('pink', 'blue'),
            'pink': ('yellow', 'green'),
            'blue': ('pink', 'green')}
        self.attempt_itr = [0]*9
        self.init_state = ['green']
        
    def solve(self):
        for _ in range(factorial(9)):
            self.state = self.init_state.copy()
            for itr in range(9):
                self.apply_booster(self.attempt_itr[itr])
            if self.is_right_state():
                self.explain_sol()
                return 'Sol found'
            self.increment_itr(0)
        print('Warning: sol not found')
        print(_, self.attempt_itr)

    def apply_booster(self, idx):
        target_cell = self.state[idx]
        cell1, cell2 = self.conv[target_cell]
        self.state[idx] = cell2
        self.state.insert(idx, cell1)
    
    def is_right_state(self):
        num_red = 0
        num_yellow = 0
        for cell in self.state:
            if cell == 'red':
                num_red += 1
            if cell == 'yellow':
                num_yellow += 1
        return num_red == 5 and num_yellow == 5
    
    def increment_itr(self, idx):
        self.attempt_itr[idx] = (self.attempt_itr[idx] + 1) % (idx + 1)
        if self.attempt_itr[idx] == 0 and idx < 8:
            self.increment_itr(idx+1)
    
    def explain_sol(self):
        print('Final sol:')
        self.state = self.init_state.copy()
        print(f"cells: {self.state}")
        for itr in range(9):
            print(f"Itr {itr}   boost cell: {self.attempt_itr[itr]}, {self.state[self.attempt_itr[itr]]}")
            self.apply_booster(self.attempt_itr[itr])
            print(f"cells: {self.state}")
    

if __name__ == "__main__":
    mySim = Simulation()
    mySim.solve()
    
