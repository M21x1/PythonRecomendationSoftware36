from node import Node

# create LinkedList class
class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value, sort_index=None):
        new_node = Node(new_value)
        if self.head_node.get_value() == None:
            self.head_node = new_node
        elif sort_index == None:
            new_node.set_next_node(self.head_node)
            self.head_node = new_node
        else:
            current_node = self.head_node
            while not new_node.get_next_node():
                sort_new_node = new_node.get_value()[sort_index]
                sort_current_node = current_node.get_value()[sort_index]
                next_node = current_node.get_next_node()
                if sort_new_node > sort_current_node: #this is first sort
                    if not current_node.get_next_node():
                        current_node.set_next_node(new_node)
                        return
                    else:
                        sort_next_node = next_node.get_value()[sort_index]
                        if sort_new_node < sort_next_node: #this is second sort
                            new_node.set_next_node(next_node)
                            current_node.set_next_node(new_node)
                        else:
                            current_node = current_node.get_next_node()
                else:
                    new_node.set_next_node(self.head_node)
                    self.head_node = new_node


    def stringify_list(self):
        string_list = ''
        current_node = self.get_head_node()
        while current_node is not None:
            string_list += str(current_node.value) + "\n" + '-------------------\n'
            current_node = current_node.get_next_node()
        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.head_node
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.next_node = next_node.get_next_node()
                    current_node = None
                else:
                    current_node = next_node