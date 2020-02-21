Function to read a string and parse it to SGF Format.

Example:

INPUT: "(;A[B](;B[C])(;C[D]))"

OUTPUT:SgfTree(properties={"A": ["B"]}, children=[SgfTree({"B": ["C"]}), SgfTree({"C": ["D"]})])

More info about the SGF format in (https://en.wikipedia.org/wiki/Smart_Game_Format)

  


