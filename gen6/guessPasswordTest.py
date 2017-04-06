import genetic
import datetime
import unittest
import random

queens = 8
#f = open('outputFile.txt', 'w')

def test_benchmark(self):
    genetic.Benchmark.run(lambda:self.test)


def display(candidate, startTime, counter):
    timeDiff = datetime.datetime.now() - startTime
    out = "{}\t{}\t{}\t{}\n".format(candidate.Genes, candidate.Fitness, str(timeDiff), counter)
    print(out)


def get_fitness(genes):
    sum = list(map(int, genes))
    sub = list(map(int, genes))
    INTGenes = list(map(int, genes))

    fitness = len(genes)

    for i in range(len(genes)):
        sum[i] = i + INTGenes[i]
        sub[i] = INTGenes[i] - i

    for i in range(len(genes)):
        for j in range(len(genes)):
            if (i == j):
                continue
            if sum[i] == sum[j]:
                fitness -= 1
            if sub[i] == sub[j]:
                fitness -= 1
    return fitness


class GuessPasswordTests(unittest.TestCase):
    geneSet = []
    for i in range(queens):
        geneSet.append(i)
    geneSet = ''.join(map(str, geneSet))

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

    def test_benchmark(self):
        genetic.Benchmark.run(self.guess_password)

def guess_password(geneSet):
    startTime = datetime.datetime.now()
    counter = 0

    def fnGetFitness (genes):
        return get_fitness(genes)

    def fnDisplay(candidate, counter):
        display(candidate, startTime, counter)

    optimalFitness = len(geneSet)
    best = genetic.get_best(fnGetFitness, len(geneSet), optimalFitness, geneSet, fnDisplay, counter)
    return best
if __name__ == '__main__':
    geneSet = []
    for i in range(queens):
        geneSet.append(i)
    geneSet = ''.join(map(str, geneSet))
    optimalFitness = len(geneSet)
    best = guess_password(geneSet)

    display(best, datetime.datetime.now(), -1)
