import genetic
import datetime
import unittest
import random

queens = 4

def test_benchmark(self):
    genetic.Benchmark.run(lambda:self.test)


def display(candidate, startTime, counter):
    timeDiff = datetime.datetime.now() - startTime
    out = "{}\t{}\t{}\t{}".format(candidate.Genes, candidate.Fitness, str(timeDiff), counter)
    print(out)


def get_fitness(genes):
    sum = list(genes)
    sub = list(genes)

    fitness = len(genes)

    for i in range(len(genes)):
        sum[i] = i + genes[i]
        sub[i] = genes[i] - i

    for i in range(len(genes)):
        for j in range(len(genes)):
            if (i == j):
                continue
            if (sum[i] == sum[j]):
                fitness -= 1
            if (sub[i] == sub[j]):
                fitness -= 1
    return fitness


class GuessPasswordTests(unittest.TestCase):
    geneSet = []
    for i in range(queens):
        geneSet.append(i)
    geneSet = ''.join(map(str, geneSet))

    def test_benchmark(self):
        genetic.Benchmark.run(self.guess_password)

    def guess_password(self):
        startTime = datetime.datetime.now()
        counter = 0

        def fnGetFitness (genes):
            return get_fitness(genes)

        def fnDisplay(candidate, counter):
            display(candidate, startTime, counter)

        optimalFitness = len(self.geneSet)
        best = genetic.get_best(fnGetFitness, len(self.geneSet), optimalFitness, self.geneSet, fnDisplay, counter)
        self.assertEqual(best.Fitness, len(best.Genes))

if __name__ == '__main__':
    unittest.main()

