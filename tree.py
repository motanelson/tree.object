def parse_tree(file_path):
    tree = {}
    stack = [tree]

    with open(file_path, 'r') as file:
        for line in file:
            line = line.rstrip()  # Remove espaços e quebras de linha no final
            if not line.strip():
                continue  # Ignora linhas vazias

            level = len(line) - len(line.lstrip())  # Conta espaços no início
            node_name = line.strip()

            # Garante que a pilha tem o tamanho correto para o nível atual
            while len(stack) > level + 1:
                stack.pop()

            # Adiciona o nó ao nível atual
            current_level = stack[-1]
            if node_name not in current_level:
                current_level[node_name] = {}

            # Adiciona o novo nó à pilha
            stack.append(current_level[node_name])

    return tree


def print_tree(tree, indent=0):
    for key, value in tree.items():
        print(' ' * indent + key)
        print_tree(value, indent + 4)


def main():
    file_name = input("Enter the name of the .txt file to load: ")

    try:
        tree = parse_tree(file_name)
        print("\nTree structure:")
        print_tree(tree)
        
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

