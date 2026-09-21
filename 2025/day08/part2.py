from utils.input import get_lines
import math

class Node:
    def __init__(self, _x, _y, _z):
        self.x = _x
        self.y = _y
        self.z = _z

    def get_distance_to(self, node):
        return math.sqrt(
            ((self.x - node.x) ** 2) +
            ((self.y - node.y) ** 2) +
            ((self.z - node.z) ** 2)
        )

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        
        return (
            self.x == other.x and
            self.y == other.y and
            self.z == other.z
        )

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __repr__(self):
        return self.__str__()

def main():
    lines = get_lines("input.txt")

    nodes = []
    node_distances = {}

    for raw_line in lines:
        line = [int(num) for num in raw_line.split(",")]
        nodes.append(Node(line[0], line[1], line[2]))

    for node_a in nodes:
        for node_b in nodes:
            if node_a is node_b: 
                continue

            key = frozenset([node_a, node_b])
            if key not in node_distances:
                node_distances[key] = node_a.get_distance_to(node_b)

    sorted_node_distances = sorted(node_distances.items(), key=lambda item: item[1])

    circuits = []   
    for i, (key, value) in enumerate(sorted_node_distances):
        # if i >= 1000:
        #     break

        node_a, node_b = list(key)

        matching_circuits = []
        for c in circuits:
            if node_a in c or node_b in c:
                matching_circuits.append(c)

        if not matching_circuits:
            circuits.append({node_a, node_b})
        else:
            # Remove old circuits
            for c in matching_circuits:
                circuits.remove(c)

            # Merge circuits
            merged_circuit = set()
            for c in matching_circuits:
                for node in c:
                    merged_circuit.add(node)

            merged_circuit.add(node_a)
            merged_circuit.add(node_b)

            if len(merged_circuit) == len(nodes):
                print(f"result: {node_a.x * node_b.x}")
                break

            circuits.append(merged_circuit)


if __name__ == "__main__":
    main()