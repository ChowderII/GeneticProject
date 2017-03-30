import genetic
import datetime
import unittest


def display(genes, target, startTime, counter):
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(genes, target)
    out = "{0}\t{1}\t{2}\t{3}".format(genes, fitness, str(timeDiff), counter)
    print(out)


def get_fitness(genes, target):
    return sum(1 for expected, actual in zip(target, genes)
               if expected == actual)

class GuessPasswordTests(unittest.TestCase):
    geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."

    def test_Hello_World(self):
        target = "Hello World!"
        self.guess_password(target)

    def test_BiggerPassword(self):
        target = "For I am fearfully and wonderfully made."
        self.guess_password(target)

    def guess_password(self, target):
        startTime = datetime.datetime.now()
        counter = 0

        def fnGetFitness (genes):
            return get_fitness(genes, target)

        def fnDisplay(genes, counter):
            display(genes, target, startTime, counter)

        optimalFitness = len(target)
        genetic.get_best(fnGetFitness, len(target), optimalFitness, self.geneSet, fnDisplay, counter)

if __name__ == '__main__':
    unittest.main()
