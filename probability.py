"""
Probability calculations for genetic trait inheritance using Bayesian networks.
"""

# Constantes de probabilidad
PROBS = {
    "gene": {2: 0.01, 1: 0.03, 0: 0.96}, 
    "trait": { 
        2: {True: 0.65, False: 0.35},
        1: {True: 0.56, False: 0.44},
        0: {True: 0.01, False: 0.99}
    },
    "mutation": 0.01 
}


def powerset(s):
    """
    Return a list of all possible subsets of set s.

    Input:
        powerset({1, 2, 3})

    Output:
        [set(), {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]
    """
    elements = list(s)
    result = []

    n = len(elements)
    
    for i in range(2**n):
        subset = set()
        for j in range(n):
            if i & (1 << j): 
                subset.add(elements[j])
        result.append(subset)
    
    return result


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set one_gene has one copy of the gene, and
        * everyone in set two_genes has two copies of the gene, and
        * everyone not in one_gene or two_gene does not have the gene, and
        * everyone in set have_trait has the trait, and
        * everyone not in set have_trait does not have the trait.

    Input:
        people = {
            "Harry": {"name": "Harry", "mother": None, "father": None, "trait": None}
        }
        one_gene = set()
        two_genes = {"Harry"}
        have_trait = {"Harry"}

    Output:
        0.0065
    """
    probability = 1.0
    
    for person in people:
        if person in two_genes:
            genes = 2
        elif person in one_gene:
            genes = 1
        else:
            genes = 0
        
        has_trait = person in have_trait
        
        mother = people[person]["mother"]
        father = people[person]["father"]
        
        if mother is None and father is None:
            gene_probability = PROBS["gene"][genes]
        else:
            pass_probabilities = []
            
            for parent in [mother, father]:
                if parent in two_genes:
                    parent_genes = 2
                elif parent in one_gene:
                    parent_genes = 1
                else:
                    parent_genes = 0
                
                if parent_genes == 2:
                    pass_prob = 1 - PROBS["mutation"]
                elif parent_genes == 1:
                    pass_prob = 0.5
                else:  
                    pass_prob = PROBS["mutation"]
                
                pass_probabilities.append(pass_prob)
            
            prob_mother = pass_probabilities[0]
            prob_father = pass_probabilities[1]
            
            if genes == 2:
                gene_probability = prob_mother * prob_father
            elif genes == 1:
                gene_probability = (prob_mother * (1 - prob_father)) + ((1 - prob_mother) * prob_father)
            else:  
                gene_probability = (1 - prob_mother) * (1 - prob_father)
        
        probability *= gene_probability * PROBS["trait"][genes][has_trait]
    
    return probability


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to probabilities a new joint probability p.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in have_gene and have_trait, respectively.

    Input:
        probabilities = {
            "Harry": {
                "gene": {2: 0, 1: 0, 0: 0},
                "trait": {True: 0, False: 0}
            }
        }
        one_gene = {"Harry"}
        two_genes = set()
        have_trait = {"Harry"}
        p = 0.5

    Output:
        {
            "Harry": {
                "gene": {2: 0, 1: 0.5, 0: 0},
                "trait": {True: 0.5, False: 0}
            }
        }
    """
    for person in probabilities:
        if person in two_genes:
            genes = 2
        elif person in one_gene:
            genes = 1
        else:
            genes = 0
        
        has_trait = person in have_trait
        
        probabilities[person]["gene"][genes] += p
        probabilities[person]["trait"][has_trait] += p


def normalize(probabilities):
    """
    Update probabilities such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).

    Input:
        probabilities = {
            "Harry": {
                "gene": {2: 2, 1: 2, 0: 6},
                "trait": {True: 1, False: 3}
            }
        }

    Output:
        {
            "Harry": {
                "gene": {2: 0.2, 1: 0.2, 0: 0.6},
                "trait": {True: 0.25, False: 0.75}
            }
        }
    """
    for person in probabilities:
        total_gene = sum(probabilities[person]["gene"].values())
        if total_gene > 0:
            for gene_count in probabilities[person]["gene"]:
                probabilities[person]["gene"][gene_count] /= total_gene
        
        total_trait = sum(probabilities[person]["trait"].values())
        if total_trait > 0:
            for trait_value in probabilities[person]["trait"]:
                probabilities[person]["trait"][trait_value] /= total_trait


def calculate_probabilities(people):
    """
    Calculate normalized gene and trait probability distributions for each person.

    Input:
        people = {
            "Person": {"mother": None, "father": None, "trait": None}
        }

    Output:
        {
            "Person": {
                "gene": {2: 0.01, 1: 0.03, 0: 0.96},
                "trait": {True: 0.0329, False: 0.9671}
            }
        }
    """
    probabilities = {}
    for person in people:
        probabilities[person] = {
            "gene": {2: 0.0, 1: 0.0, 0: 0.0},
            "trait": {True: 0.0, False: 0.0}
        }
    
    names = set(people.keys())

    for have_trait in powerset(names):
        skip = False
        for person in names:
            known_trait = people[person]["trait"]
            if known_trait is not None:
                if (person in have_trait) != known_trait:
                    skip = True
                    break
        if skip:
            continue
        
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)
    
    normalize(probabilities)
    
    return probabilities