metamodel_dict = {
    "nodes": [
        {
            "Type": "Person",
            "edges": ["Friends", "Parents", "Child", "Sibling", "Colleague"]
        },
        {
            "Type": "Pets",
            "edges": ["Owned", "Friends"]
        }
    ],
    "edges": ["Friends", "Parents", "Child", "Sibling", "Colleague", "Owned"]
}
