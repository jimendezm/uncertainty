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
def powerset(s):
    """
    Return a list of all possible subsets of set s.

    Input:
        powerset({1, 2, 3})

    Output:
        [set(), {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]
    """
def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set one_gene has one copy of the gene, and
        * everyone in set two_genes has two copies of the gene, and
        * everyone not in one_gene or two_gene does not have the gene, and
        * everyone in set have_trait has the trait, and
        * everyone not in set` have_trait` does not have the trait.

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