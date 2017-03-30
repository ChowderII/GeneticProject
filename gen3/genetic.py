import random

def _generate_parent(length, geneSet):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    return ''.join(genes)


def _mutate(parent, geneSet):
    index = random.randint(0, len(parent) -1)
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate \
        if newGene == childGenes[index] \
        else newGene
    return ''.join(childGenes)


def get_best(get_fitness, targetLen, optimalFitness, geneSet, display, counter):
    bestParent = _generate_parent(targetLen, geneSet)
    bestFitness = get_fitness(bestParent)
    display(bestParent, counter)
    if bestFitness >= optimalFitness:
        return bestParent

    while True:
        counter += 1
        child = _mutate(bestParent, geneSet)
        childFitness = get_fitness(child)

        if bestFitness >= childFitness:
            continue
        display(child, counter)
        if childFitness >= optimalFitness:
            return child
        bestFitness = childFitness
        bestParent = child
