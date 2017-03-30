import genetic
import datetime
import sys


def test_Hello_World():
    print("What is your target string ? : ")
    target = raw_input()
    guess_password(target)


def guess_password(target):
    geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
    startTime = datetime.datetime.now()
    counter = 0

    def fnGetFitness (genes):
        return get_fitness(genes, target)

    def fnDisplay(genes, counter):
        display(genes, target, startTime, counter)

    optimalFitness = len(target)
    genetic.get_best(fnGetFitness, len(target), optimalFitness, geneSet, fnDisplay, counter)


def display(genes, target, startTime, counter):
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(genes, target)
    out = "{0}\t{1}\t{2}\t{3}".format(genes, fitness, str(timeDiff), counter)
    print(out)


def get_fitness(genes, target):
    return sum(1 for expected, actual in zip(target, genes)
               if expected == actual)

if __name__ == '__main__':
    test_Hello_World()
