import genetic
import datetime
import unittest
import random


def test_benchmark(self):
    genetic.Benchmark.run(lambda:self.test)


def display(candidate, startTime, counter):
    timeDiff = datetime.datetime.now() - startTime
    out = "{}\t{}\t{}\t{}".format(candidate.Genes, candidate.Fitness, str(timeDiff), counter)
    print(out)


def get_fitness(genes):
    for i in range(genes):



class GuessPasswordTests(unittest.TestCase):
    geneSet = []
    for i in range(queens):
        geneSet.append(i)

    def test_benchmark(self):
        genetic.Benchmark.run(self.test_Random)

    def guess_password(self, target):
        startTime = datetime.datetime.now()
        counter = 0

        def fnGetFitness (genes):
            return get_fitness(genes)

        def fnDisplay(candidate, counter):
            display(candidate, startTime, counter)

        optimalFitness = len(self.geneSet)
        best = genetic.get_best(fnGetFitness, len(self.geneSet), optimalFitness, self.geneSet, fnDisplay, counter)
        self.assertEqual(best.Genes, target)# change

if __name__ == '__main__':
    queens = input("How many queens do you want to fit ? : ")
    unittest.main()
