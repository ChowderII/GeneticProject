import random
import statistics
import time
import sys


class Chromosome:
    Genes = None
    Fitness = None

    def __init__(self, genes, fitness):
        self.Genes = genes
        self.Fitness = fitness

class Benchmark:
    @staticmethod
    def run(function):
        timings = []
        #stdout = sys.stdout
        for i in range(100):
            #sys.stdout = None
            startTime = time.time()
            function()
            seconds = time.time() - startTime
            #sys.stdout = stdout
            timings.append(seconds)
            mean = statistics.mean(timings)
            if i < 10 or i % 10 == 9:
                print("{} {:3.2f} {:3.2f}".format(1+i, mean, statistics.stdev(timings, mean) if i > 1 else 0))


def _generate_parent(length, geneSet, get_fitness):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    genes = ''.join(genes)
    fitness = get_fitness(genes)
    return Chromosome(genes, fitness)


def _mutate(parent, geneSet, get_fitness):
    index = random.randint(0, len(parent.Genes) -1)
    childGenes = list(parent.Genes)
    newGene, alternate = random.sample(geneSet, 2)

    if (newGene == childGenes[index]):
        temp = childGenes[index]
        tempIndex = childGenes.index(alternate)
        childGenes[index] = alternate
        childGenes[tempIndex] = temp

    else:
        temp = childGenes[index]
        tempIndex = childGenes.index(newGene)
        childGenes[index] = alternate
        childGenes[tempIndex] = temp

    genes = ''.join(childGenes)
    fitness = get_fitness(genes)
    return Chromosome(genes, fitness)

def get_best(get_fitness, targetLen, optimalFitness, geneSet, display, counter):
    bestParent = _generate_parent(targetLen, geneSet, get_fitness)
    display(bestParent, counter)
    if bestParent.Fitness >= optimalFitness:
        return bestParent

    while True:
        counter += 1
        child = _mutate(bestParent, geneSet, get_fitness)

        if bestParent.Fitness >= child.Fitness:
            continue
        display(child, counter)
        if child.Fitness >= optimalFitness:
            return child
        bestParent = child
