from probabilistic_hunting_target_found import ProbabilisticHunting_TargetFound

class ProbabilisticHunting_WithCost(ProbabilisticHunting_TargetFound):

    def __init__(self):
        self.cost = []
        for i in range(0, self.dimension):
            self.cost.append([])
            for j in range(0, self.dimension):
                self.cost[i].append()

    def initCostFromCell(self, i, j):
