from graphviz import Digraph

dot = Digraph()
dot.node("A")
dot.node("B")
dot.node("C")
dot.edges(["AB", "AC"])
dot.render("arbre", format="png", view=True)
