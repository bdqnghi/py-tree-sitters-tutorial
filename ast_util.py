import sys


class ASTUtil():
    import logging
    LOGGER = logging.getLogger('ASTUtil')

    # Simplify the AST 
    def simplify_ast(self, tree, text):
        # tree = self.ast_parser.parse(text)
        root = tree.root_node

        ignore_types = ["\n"]
        num_nodes = 0
        root_type = str(root.type)
        queue = [root]

        root_json = {
            "node_type": root_type,
            "node_token": "", # usually root does not contain token
            "children": []
        }

        queue_json = [root_json]
        while queue:
            
            current_node = queue.pop(0)
            current_node_json = queue_json.pop(0)
            num_nodes += 1


            for child in current_node.children:
                child_type = str(child.type)
                if child_type not in ignore_types:
                    queue.append(child)

                    child_token = ""
                    has_child = len(child.children) > 0

                    if not has_child:
                        child_token = text[child.start_byte:child.end_byte]

                    child_json = {
                        "node_type": child_type,
                        "node_token": child_token,
                        "children": []
                    }

                    current_node_json['children'].append(child_json)
                    queue_json.append(child_json)

        return root_json, num_nodes