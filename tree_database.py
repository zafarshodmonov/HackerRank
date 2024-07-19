
class BinaryTreeNode:
    def __init__(self, value = 0, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def read_binary_tree_from_file(filename: str, symbol: str):
    """
    1. Summary Line:
        A.

    2. Description:
        A.

    3. Parameters:
        filename (str): 
            A.

        symbol (str): 
            A symbol representing the 'None' value of the tree data structure in file.

    4. Returns:
        A.

    5. Raises:
        A.

    6. Examples:
        A.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    if not lines:
        return None
    
    node_dict = {}
    root = None

    for line in lines:
        value, left_value, right_value = line.strip().split()
        value = int(value)
        
        if value not in node_dict:
            node_dict[value] = BinaryTreeNode(value)
        
        current = node_dict[value]
        
        if not root:
            root = current
        
        if left_value != symbol:
            left_value = int(left_value)
            if left_value not in node_dict:
                node_dict[left_value] = BinaryTreeNode(left_value)
            current.left = node_dict[left_value]
        
        if right_value != symbol:
            right_value = int(right_value)
            if right_value not in node_dict:
                node_dict[right_value] = BinaryTreeNode(right_value)
            current.right = node_dict[right_value]
    
    return root

def write_binary_tree_to_file(root, filename, symbol):
    if not root:
        return
    
    with open(filename, 'w') as file:
        queue = [root]
        while queue:
            current = queue.pop(0)
            left_value = current.left.value if current.left else symbol
            right_value = current.right.value if current.right else symbol
            file.write(f"{current.value} {left_value} {right_value}\n")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)


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

# Function to print the tree for verification
def print_tree(node, level=0):
    if node is not None:
        print(' ' * level * 2 + str(node.val))
        for child in node.children:
            print_tree(child, level + 1)

path_binary_tree = "data_structure_database/tree_database/binary_tree/"
path_nary_tree = "data_structure_database/tree_database/nary_tree/"

# Declare a function that represents the name of a file containing a 'tree' data structure
def tree_file_name(type_tree: str, name: str | int) -> str:
    """
    1. Summary Line:
        Declare a function that represents the name of a file containing a 'tree' data structure.

    2. Description:
        Declare a function that represents the name of a file containing a 'tree' data structure.

    3. Parameters:
        type_tree (str): 
            Represents type 'Binary Tree'. 'b' if the tree is 'Binary Tree'. Accepts the value 'n' 
            if the tree is an 'N-ary Tree'.

        name (str | int): 
            Represents the name of 'Tree'. A '_' between each word of the tree name is 
            mandatory!

    4. Returns:
        str: A tree data structure represents a file name.

    5. Raises:
        ValueError: Occurs if the parameter 'type_tree' accepts a type other than the data type 'str'.

    6. Examples:
        >>> tree_file_name('b', 1)
        'binary__tree__1.txt'

        >>> name = 'heap_tree_2'
        >>> tree_file_name('b', name)
        'binary__tree__heap_tree_2.txt'  
    """
    
    type_tree = 'binary' if (type_tree == 'b') else 'nary'
    
    return f'{type_tree}__tree__{name}.txt'

write_binary_tree_to_file(
    read_binary_tree_from_file(f'{path_binary_tree}{tree_file_name('b', 5)}', 'Zafar'),
    f'{path_binary_tree}{tree_file_name('b', 6)}',
    'x'
    )


