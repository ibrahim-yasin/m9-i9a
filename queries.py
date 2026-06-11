def q1():
    """Q1 — List all authors who have published at venue :NeurIPS."""
    return """
    PREFIX : <http://aispire.example.org/publications/>

    SELECT DISTINCT ?author
    WHERE {
        ?paper :publishedIn :NeurIPS ;
               :authoredBy ?author .
    }
    """


def q2():
    """Q2 — For each topic, count the number of papers on that topic."""
    return """
    PREFIX : <http://aispire.example.org/publications/>

    SELECT ?topic (COUNT(?paper) AS ?n)
    WHERE {
        ?paper :topic ?topic .
    }
    GROUP BY ?topic
    """
    

def q3():
    """Q3 — All author-coauthor pairs in canonical form."""
    return """
    PREFIX : <http://aispire.example.org/publications/>

    SELECT DISTINCT ?a ?b
    WHERE {
        ?p :authoredBy ?a , ?b .
        FILTER (?a != ?b)
        FILTER (STR(?a) < STR(?b))
    }
    """


def q4():
    """Q4 — Every paper and its DOI, DOI OPTIONAL."""
    return """
    PREFIX : <http://aispire.example.org/publications/>

    SELECT ?paper ?doi
    WHERE {
        ?paper a :Paper .
        OPTIONAL {
            ?paper :doi ?doi .
        }
    }
    """


def q5():
    """Q5 — ASK whether any author has more than 10 papers."""
    return """
    PREFIX : <http://aispire.example.org/publications/>

    ASK {
        {
            SELECT ?author
            WHERE {
                ?paper :authoredBy ?author .
            }
            GROUP BY ?author
            HAVING (COUNT(?paper) > 10)
        }
    }
    """


def q6():
    """Q6 — CONSTRUCT a graph of 2023 papers and their authors."""
    return """
    PREFIX : <http://aispire.example.org/publications/>

    CONSTRUCT {
        ?paper :authoredBy ?author .
    }
    WHERE {
        ?paper :year 2023 ;
               :authoredBy ?author .
    }
    """


def q7():
    """Q7 — Top 5 most-cited papers by literal :citationCount, DESC."""
    return """
    PREFIX : <http://aispire.example.org/publications/>

    SELECT ?paper ?cc
    WHERE {
        ?paper :citationCount ?cc .
    }
    ORDER BY DESC(?cc)
    LIMIT 5
    """


def q8():
    """Q8 — Authors whose name matches "Hinton" via skos:prefLabel OR skos:altLabel."""
    return """
   PREFIX : <http://aispire.example.org/publications/>
   PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

  SELECT ?author
  WHERE {
    ?author ?label "Hinton" .
    FILTER (?label = skos:prefLabel || ?label = skos:altLabel)
    }
    """