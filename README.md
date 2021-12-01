# A simple tutorial to use tree-sitter to parse code into ASTs.

- To understand what is tree-sitter, see https://github.com/tree-sitter/tree-sitter.
- Tree-sitter is written in C. In order to use it in Python, it must have a Python binding to interact with the C code, see https://github.com/tree-sitter/py-tree-sitter.
- However, the py-tree-sitter requires some complicated installation steps to make it work. This tutorial shows an easy way to make tree-sitter works with little effort. Go to to command line, follow these steps:

1) `pip3 install tree_sitter`
2) `git clone https://github.com/bdqnghi/tree-sitter-parsers`
3) `cd tree-sitter-parsers`
4) Execute these commands: 
```bash
rm -rf dist/*
python3 setup.py sdist bdist_wheel
pip uninstall tree_sitter_parsers -y
pip install dist/tree_sitter_parsers-*-py3-none-any.whl
rm -rf ~/.tree-sitter
python3 -c "import tree_sitter_parsers"
```
5) Check if the tree-sitters pre-installed libraries have been downloaded to your path in `~/.tree-sitter/bin`
6) Now you are ready to use tree-sitter, execute `python3 test_parsing.py` to see if it works, then you can explore the code by yourself.
