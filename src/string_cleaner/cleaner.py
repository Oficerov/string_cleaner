from .config import entity_map


class TakeString:
    """
    Make clean string from dirty.
    Receive string with special chars, replace this chars by html-entity and return it.
    """
    __entity_map: dict = dict()
    __clean_string: str = str()

    def __init__(self, string: str, new_rule: str | dict = 's'):
        """
        Receive dirty string and call clea n method for clean it.
        `:param` rule: can have value:

        - ***MVP:*** 's': string:type. It'll change all special chars by html-entity in string.
        - ***0.3.1:*** new_rule could be dict:type and make additional custom rule to replace. New rule have
        priority using if it's replacing default rule.

        `Example additional replace rule by custom dict:` ```{"<": "some_new", ">": "some_new", "a": "b"}```

        It'll change specified chars by specified rules.
        `:type` rule: `str:param` or `dict:param`
        """
        self.__string: str = string
        if type(new_rule) is dict:
            self.__entity_map = entity_map(new_rule=new_rule)
        else:
            self.__entity_map = entity_map()
        self.__rule: str = new_rule


    def __enter__(self):
        """Provide work with context manager. Return clean string"""
        return self.make_clean_string()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Remove all created data from memory after work module"""
        if self.__entity_map:
            del self.__entity_map
        if self.__clean_string:
            del self.__clean_string
        if self.__string:
            del self.__string
        if self.__rule:
            del self.__rule
        if self.__clean_string:
            del self.__clean_string

    def make_clean_string(self) -> str:
        """Replace special charts by html-entity and return clean string."""
        if self.__rule == 's' or type(self.__rule) is dict:
            for symbol in self.__string:
                if symbol in self.__entity_map:
                    self.__clean_string += self.__entity_map[symbol]
                else:
                    self.__clean_string += symbol
            return self.__clean_string
        elif type(self.__rule) is not str:
            raise TypeError(f'Rule \'{self.__rule}\' have wrong ({type(self.__rule)}) type, when need str')
        else:
            raise ValueError(f'Rule: \'{self.__rule}\' is incorrect')
