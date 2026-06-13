import argparse
import sys

# =========================
# SPARQL QUERIES (mocked / reusable from your integration)
# =========================

INTENTS = {
    "list authors at neurips": {
        "type": "SELECT",
        "query": """
SELECT DISTINCT ?author WHERE {
  ?paper <publishedAt> "NeurIPS" .
  ?paper <hasAuthor> ?author .
}
"""
    },

    "papers per topic": {
        "type": "SELECT",
        "query": """
SELECT ?topic (COUNT(?paper) AS ?count) WHERE {
  ?paper <hasTopic> ?topic .
}
GROUP BY ?topic
"""
    },

    "top 5 cited": {
        "type": "SELECT",
        "query": """
SELECT ?paper ?citations WHERE {
  ?paper <citationCount> ?citations .
}
ORDER BY DESC(?citations)
LIMIT 5
"""
    },

    "is ai research available": {
        "type": "ASK",
        "query": """
ASK {
  ?paper <hasTopic> "AI" .
}
"""
    },

    "citation graph": {
        "type": "CONSTRUCT",
        "query": """
CONSTRUCT {
  ?paper <cites> ?citedPaper .
}
WHERE {
  ?paper <cites> ?citedPaper .
}
"""
    }
}


# =========================
# MAIN DISPATCHER
# =========================

def main():
    parser = argparse.ArgumentParser(description="SPARQL CLI Dispatcher")
    parser.add_argument("intent", type=str, help="Natural language intent")
    args = parser.parse_args()

    intent = args.intent.lower().strip()

    if intent in INTENTS:
        print(INTENTS[intent]["query"].strip())
        sys.exit(0)

    # Unknown intent handling
    print("\nUnknown intent!\n")
    print("Supported intents:\n")

    for key in INTENTS.keys():
        print(f"- {key}")

    sys.exit(1)


if __name__ == "__main__":
    main()