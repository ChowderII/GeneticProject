import genetic
import datetime
import unittest
import random


def test_benchmark(self):
    genetic.Benchmark.run(lambda:self.test)


def display(candidate, startTime, counter):
    timeDiff = datetime.datetime.now() - startTime
    out = "{0}\t{1}\t{2}\t{3}".format(candidate.Genes, candidate.Fitness, str(timeDiff), counter)
    print(out)


def get_fitness(genes, target):
    return sum(1 for expected, actual in zip(target, genes)
               if expected == actual)


class GuessPasswordTests(unittest.TestCase):
    geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."

    def test_Random(self):
        length = 150
        target = ''.join(random.choice(self.geneSet) for _ in range(length))
        self.guess_password(target)

    def test_benchmark(self):
        genetic.Benchmark.run(self.test_Random)

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

        def fnDisplay(candidate, counter):
            display(candidate, startTime, counter)

        optimalFitness = len(target)
        best = genetic.get_best(fnGetFitness, len(target), optimalFitness, self.geneSet, fnDisplay, counter)
        self.assertEqual(best.Genes, target)

if __name__ == '__main__':
    unittest.main()
