
class BinaryTreeNode:
    print


class TreeNode:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children is not None else []


class TreeDict:

    @staticmethod
    def tree_dict_1():

        return ({
            1: [2, 3],
            2: [4, 5],
            3: [6],
            4: [],
            5: [],
            6: []
        }, 1)

def build_tree_map_from_file(filename):
    tree = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        
        # First line contains the number of nodes
        num_nodes = int(lines[0].strip())
        ROOT, _ = map(int, lines[1].strip().split())
        
        # Initialize tree with empty lists for each node
        for i in range(1, num_nodes + 1):
            tree[i] = []
        
        # Populate the tree with edges
        for line in lines[1:]:
            parent, child = map(int, line.strip().split())
            tree[parent].append(child)
    
    return tree, ROOT

def build_tree_from_dict(tree_dict, root_int: int):
    # Create a dictionary to hold all nodes
    nodes = {val: TreeNode(val) for val in tree_dict}
    
    # Populate the children for each node
    for parent, children in tree_dict.items():
        nodes[parent].children = [nodes[child] for child in children]
    
    # The root is usually the first node (1 in this case)
    return nodes[root_int]

tree_dict = TreeDict()

def path_tree(tree_type: str, n: int) -> str:
    PATH_TREE = f'data_structure_database/tree_database/{tree_type}_tree/{tree_type}_tree_{n}.txt'
    return PATH_TREE

# TREE_MAP
# static
TREE_MAP_1 = tree_dict.tree_dict_1()

# dynamic
TREE_MAP_2 = build_tree_map_from_file(path_tree('n', 1))

# TREES
TREE_1 = build_tree_from_dict(* TREE_MAP_1)
N_TREE_2 = build_tree_from_dict(* TREE_MAP_2)

# Function to print the tree for verification
def print_tree(node, level=0):
    if node is not None:
        print(' ' * level * 2 + str(node.val))
        for child in node.children:
            print_tree(child, level + 1)


def main():
    print_tree(N_TREE_2)

if __name__ == "__main__":
    main()
