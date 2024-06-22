from typing import List


class MemorySection:
    """Single memory section with a reserved token count and handle."""

    # Note: should be possible to pre-define/save this to replace current Human/Persona objects
    def __init__(self, section: str, value: str | List[str], max_length: int = 2000):
        self.section = section
        self.value = value
        self.max_length = max_length  # maximum length of this module (chars)

    def __len__(self):
        # calculate list of memory
        if isinstance(self.value, str):
            return len(self.value)
        else:
            # is a list of strings
            assert isinstance(self.value, list), "Memory value must be a string or list of strings"
            return sum([len(v) + 1 for v in self.value])

    def __repr__(self):
        pass

    def __dict__(self):
        # JSON/dictionary representation of the memory
        return {"section": self.section, "value": self.value, "max_length": self.max_length}


class BaseMemory:

    def __init__(self):
        pass

    def __dict__(self):
        pass


class ChatMemory(BaseMemory):

    def __init__(self, human: str, persona: str):
        pass
