import random

class randTrials:
    """Model: a misogynistic couple keeps having children until a boy is born. 
    What is the average number of boys and girls per couple?
    Theoretical analysis here:
    https://twitter.com/alpha_narcos/status/1737785127193780669"""
    def __init__(self, num_trials):
        self.num_trials = num_trials
        self.num_boys = 0
        self.num_girls = 0
        self.history = {}
        
        for j in range(self.num_trials):
            self.one_trial()
        print(f"num trials = {self.num_trials}")
        print(f"num boys = {self.num_boys}")
        print(f"num girls = {self.num_girls}")
        print(f"history = {self.history}")
        
    def one_trial(self):
        k = 0
        while True:
            k += 1
            if self.one_iter(): # if boy
                break
        if k in self.history:
            self.history[k] += 1
        else:
            self.history[k] = 1
    
    def one_iter(self):
        outcome = random.randint(0, 1) # 0 = girl
        if outcome: # boy
            self.num_boys += 1
        else:
            self.num_girls += 1
        return outcome

        
myExperiment = randTrials(num_trials = 1000)
