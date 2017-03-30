import random
import datetime

geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!." # possible values of
target = "aAaA!" # wanted solution


def generate_parent(length):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet)) # i think this is the population size, but i cant change it, I'd like to lower it but it doesnt work when i lower it
        genes.extend(random.sample(geneSet, sampleSize))
    return ''.join(genes)


def get_fitness(guess):
    return sum(1 for expected, actual in zip(target, guess) if expected == actual)
    #why can i have an if in a return ?? theres a for loop and a if in a return statement ???

def mutate(parent):
    index = random.randint(0, len(parent) - 1) # chooses the index to change
    childGenes = list(parent) # turns the parent back into array of chars
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate \
        if newGene == childGenes[index] \
        else newGene
    return ''.join(childGenes)


def display(guess, counter, file): # just displays the gene, the iteration and the time, i think
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(guess)
    out = "{0}\t{1}\t{2}\t{3}".format(guess, fitness, str(timeDiff), counter)
    print >> file, out

# i'll read on that myself, it deals with the function itself
fileNotMatching = open('outNotMatch.txt', 'w')
fileMatching = open('outMatch.txt', 'w')
startTime = datetime.datetime.now() # got that :D
bestParent = generate_parent(len(target)) # creates a the parent(s) ? with the length of the target
bestFitness = get_fitness(bestParent)
display(bestParent, 0, fileNotMatching)


counter = 1

while True:
    child = mutate(bestParent)
    display(child, counter, fileNotMatching)
    counter += 1
    childFitness = get_fitness(child)

    if bestFitness >= childFitness:
        continue
    display(child, counter, fileMatching)
    if childFitness >= len(bestParent):
        break
    bestFitness = childFitness
    bestParent = child
