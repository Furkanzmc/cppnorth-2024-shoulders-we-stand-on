import yaml
import networkx as nx
import argparse
import sys


def yaml_to_gexf(yaml_data, output_file):
    G = nx.DiGraph()

    for act, people in yaml_data["Acts"].items():
        for person in people:
            G.add_node(person["name"], act=act)

            for influence in person.setdefault("influences", []):
                G.add_node(influence["name"], act=act)
                G.add_edge(
                    person["name"],
                    influence["name"],
                    description=influence["description"],
                )

            for influence in person.setdefault("influenced-by", []):
                G.add_node(influence["name"], act=act)
                G.add_edge(
                    person["name"],
                    influence["name"],
                    description=influence["description"],
                )

    nx.write_gexf(G, output_file)


def main():
    parser = argparse.ArgumentParser(description="Convert a YAML file to GEXF format.")
    parser.add_argument(
        "input_file",
        nargs="?",
        type=argparse.FileType("r"),
        default=sys.stdin,
        help="Input YAML file",
    )
    parser.add_argument("output_file", type=str, help="Output GEXF file")
    args = parser.parse_args()

    with args.input_file as f:
        yaml_data = yaml.safe_load(f)

    yaml_to_gexf(yaml_data, args.output_file)


if __name__ == "__main__":
    main()
