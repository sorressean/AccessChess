"""
This module defines the ConfigurationValue class, which stores and manages configuration values
with support for type validation and metadata-based constraints, including string, integer, and boolean types.
"""

from typing import Any, Optional


class ConfigurationValue:
    """
    A class that represents a configuration value with support for type validation and metadata constraints.

    Attributes:
        category (str): The category for the configuration, useful for organizing options.
        name (str): The name/key for the configuration value.
        value (Any): The stored value.
        value_type (Type): The expected type of the value (e.g., str, int, bool).
        metadata (Dict[str, Any]): Metadata such as length constraints for strings, or min/max for integers.
        ui (bool): Flag indicating if the value should be shown in the UI.
    """

    def __init__(
        self, category: str, name: str, value: Any, value_type: type, metadata: dict[str, Any], ui: bool = True
    ) -> None:
        """
        Initializes a ConfigurationValue object.

        :param category: The category of configuration for organization.
        :param name: The name of the key (can include dots for hierarchy).
        :param value: The value to store.
        :param value_type: The type of the value (used for casting/validation).
        :param metadata: Metadata such as min/max for integers, or length constraints for strings.
        :param ui: Whether the value should be rendered in the UI (default is True).
        """
        self.category = category
        self.name = name
        self.value_type = value_type
        self.metadata = metadata
        self.ui = ui
        self.set(value)

    def _validate_value(self, value: Any) -> None:
        """
        Validates the value based on its type and metadata constraints.
        Calls specific validation methods based on the value type.
        """
        if self.value_type == str:
            self._validate_string(value)
        elif self.value_type == int:
            self._validate_int(value)
        elif self.value_type == bool:
            self._validate_bool(value)
        else:
            raise TypeError(f"Unsupported type: {self.value_type}")

    def _convert_value(self, value: Any) -> Any:
        """
        Converts the given value to the appropriate type based on the stored value_type.

        :param value: The value to convert.
        :return: The converted value in the appropriate type (str, int, or bool).
        :raises TypeError: If the value_type is unsupported.
        """
        if self.value_type == str:
            return self._convert_to_string(value)
        elif self.value_type == int:
            return self._convert_to_int(value)
        elif self.value_type == bool:
            return self._convert_to_bool(value)
        else:
            raise TypeError(f"Unsupported type: {self.value_type}")

    def _validate_string(self, value: str) -> None:
        """
        Validates the string value based on metadata constraints for minimum and maximum length.

        :param value: The string value to validate.
        :raises ValueError: If the string length is outside the allowed range.
        """
        min_length: Optional[int] = self.metadata.get("min_length")
        max_length: Optional[int] = self.metadata.get("max_length")

        if min_length is not None and len(value) < min_length:
            raise ValueError(f"Value must have a minimum length of {min_length}.")
        if max_length is not None and len(value) > max_length:
            raise ValueError(f"Value must have a maximum length of {max_length}.")

    def _validate_int(self, value: int) -> None:
        """
        Validates the integer value based on metadata constraints for minimum and maximum values.

        :param value: The integer value to validate.
        :raises ValueError: If the integer is outside the allowed range.
        """
        min_value: Optional[int] = self.metadata.get("min")
        max_value: Optional[int] = self.metadata.get("max")

        if min_value is not None and value < min_value:
            raise ValueError(f"Value must be at least {min_value}.")
        if max_value is not None and value > max_value:
            raise ValueError(f"Value must be at most {max_value}.")

    def _validate_bool(self, value: bool) -> None:
        """
        Validates a boolean value. For booleans, it simply ensures the value is either True or False.

        :param value: The boolean value to validate.
        :raises ValueError: If the value is not a boolean.
        """
        return

    def _convert_to_string(self, value: Any) -> str:
        """
        Converts the value to its string representation.

        :param value: The value to convert.
        :return: The string representation of the value.
        """
        return str(value)

    def _convert_to_int(self, value: Any) -> int:
        """
        Converts the value to an integer.

        :param value: The value to convert.
        :return: The integer representation of the value.
        :raises ValueError: If the value cannot be cast to an integer.
        """
        try:
            return int(value)
        except (ValueError, TypeError):
            raise ValueError(f"Cannot convert value {value} to integer.")

    def _convert_to_bool(self, value: Any) -> bool:
        """
        Converts the value to a boolean. Always returns True for boolean values.

        :param value: The value to convert.
        :return: The boolean representation of the value (True or False).
        :raises ValueError: If the value cannot be cast to a boolean.
        """
        return bool(value)

    def get(self) -> Any:
        """
        Returns the stored value.

        :return: The stored value.
        """
        return self.value

    def set(self, value):
        """
        Sets the stored value, after validation and conversion of that value.

        :param value the value to set.
        """
        self._validate_value(value)
        self.value = self._convert_value(value)
        return self.value
