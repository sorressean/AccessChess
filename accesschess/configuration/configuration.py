from typing import Any

import ujson

from .value import ConfigurationValue


class Configuration:
    """
    The configuration class serves multiple responsibilities.
    It interfaces with ConfigurationValue objects and handles saving/loading configuration values to and from JSON.
    It also manages a tree of configuration values organized by category, enabling tree-based dialogs.
    """

    def __init__(self) -> None:
        """
        Initializes the configuration object.
        `tree` holds the configuration hierarchy, and `filename` can be used for saving/loading JSON files.
        """
        self.filename = ""
        self.tree = {}

    def find_or_create_leaf_helper(self, names: list, node: dict, value: ConfigurationValue) -> dict:
        """
        A recursive helper function that creates or finds a leaf node in the tree structure.

        :param names: A list of keys representing the path to the value (reversed).
        :param node: The current node in the tree.
        :param value: The value to be added as a leaf (should be a ConfigurationValue).
        :return: The node where the value has been added or updated.
        """
        name = names.pop()

        # If we've reached the leaf, set the value and return
        if not names:
            node[name] = value
            return node

        # Ensure the next node exists and continue recursion
        if name not in node:
            node[name] = {}

        return self.find_or_create_leaf_helper(names, node[name], value)

    def add_value(self, key: str, value: ConfigurationValue) -> bool:
        """
        Adds a value to the configuration tree at the specified key path.

        :param key: A dotted string representing the path to the configuration value (e.g., 'a.b.value').
        :param value: A ConfigurationValue object to be added.
        :return: True if the value was successfully added, False otherwise.
        """
        key = key.strip()
        if not key:
            raise ValueError("Key must be a valid configuration path.")

        names = key.split(".")
        names.reverse()  # We reverse the list to pop from it.

        if not names:
            raise ValueError("Key must be a valid configuration path.")

        self.find_or_create_leaf_helper(names, self.tree, value)
        return True

    def collect_values(self, root) -> list:
        values = []
        for k, v in root.items():
            if isinstance(v, dict):
                values.extend(self.collect_values(v))
            else:
                values.append(v)
        return values

    def to_json(self) -> str:
        """
        Serializes the configuration tree to a JSON string, ensuring that ConfigurationValue objects
        are serialized using their `get()` method.

        :return: A JSON string representation of the configuration tree.
        """

        def serialize_node(node: Any) -> Any:
            # If the node is a ConfigurationValue, return its value using get()
            if isinstance(node, ConfigurationValue):
                return node.get()
            # If the node is a dictionary, recursively serialize its children
            elif isinstance(node, dict):
                return {key: serialize_node(value) for key, value in node.items()}
            # Otherwise, return the node as-is
            return node

        # Serialize the entire tree using ujson
        return ujson.dumps(serialize_node(self.tree))

    def build_category_tree(self) -> dict:
        """
        Builds a nested category tree where ConfigurationValues are grouped under their categories.

        :return: A nested dictionary representing the category tree structure.
        """
        category_tree = {}

        for value in self.collect_values(self.tree):
            category_parts = value.category.split(".")
            current_node = category_tree

            # Traverse the category path, creating nested dictionaries if necessary
            for part in category_parts:
                if part not in current_node:
                    current_node[part] = {}  # Create a new nested category
                current_node = current_node[part]

            # Append the ConfigurationValue to the leaf node, under the correct category
            if "values" not in current_node:
                current_node["values"] = []
            current_node["values"].append(value)

        return category_tree
