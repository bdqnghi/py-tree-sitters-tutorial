from ast_parser import ASTParser
from ast_util import ASTUtil

def main():

	parser = ASTParser(language="java")
	ast_util = ASTUtil()
	sample_code = """
		public class Main {
			public static void main(String[] args) {
				int var1 = 15;
				int var2 = 20;
				int var3 = var1 + var2;
			}
		}
		"""
	tree = parser.parse(str.encode(sample_code))
	# print the ast object of tree-sitter
	print(tree)

	"""
	Simple traversals on the tree-sitter's ast, refer to https://github.com/tree-sitter/py-tree-sitter
	for more information
	"""
	root_node = tree.root_node
	print(root_node)
	class_declaration_node = root_node.children[0]
	print(class_declaration_node)

	#-----------------------------

	"""
	simplfy_ast is a function to traverse the ast using Breadth First Traversal to convert the ast into 
	a simpler format, which is as a Python dictionary.
	"""
	simplified_ast = ast_util.simplify_ast(tree, sample_code)
	print(simplified_ast)


if __name__ == "__main__":
    main()
