import flet as ft

class NodoArbol:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ArbolBinario:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = NodoArbol(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = NodoArbol(value)
            else:
                self._insert_recursively(node.left, value)
        else:
            if node.right is None:
                node.right = NodoArbol(value)
            else:
                self._insert_recursively(node.right, value)

    def display(self):
        nodes = []
        self._in_order_traversal(self.root, nodes)
        return nodes

    def _in_order_traversal(self, node, nodes):
        if node is not None:
            self._in_order_traversal(node.left, nodes)
            nodes.append(node.value)
            self._in_order_traversal(node.right, nodes)

def main(page: ft.Page):
    page.title = "App De Árbol Binario"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    tree = ArbolBinario()

    def on_add_node(e):
        try:
            value = int(node_value_input.value)
            tree.insert(value)
            update_tree_display()
        except ValueError:
            print("Por favor introduzca un entero válido")

    def update_tree_display():
        tree_nodes = tree.display()
        tree_display.value = "Nodos Del Árbol: " + " ".join(map(str, tree_nodes))
        page.update()

    node_value_input = ft.TextField(label="Valor Del Nodo")
    add_node_button = ft.ElevatedButton(text="Añadir nodo", on_click=on_add_node)
    tree_display = ft.Text(value="Nodos Del Árbol: ", size=20)

    page.add(
        ft.Column(
            [
                node_value_input,
                add_node_button,
                tree_display,
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
