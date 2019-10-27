from enum import Enum

class Exercise:
    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.length = len(self.text)
        self.failures = 0
        self.status = ExcerciseStatus.NoStarted # completed, not started, paused
        self.resume_from = 0
        self.current_char = 'a'


class ExcerciseStatus(Enum):
    NotStarted = "NotStarted",
    Paused = "Paused",
    InProgress = "InProgress"

class Character:

    @property
    def lower_case(self):
        return ['a', 'b', 'c']

    @property
    def upper_case(self):
        return ['A', 'B']
    
    @property
    def special_chars(self):
        return [1231231321, 43242,5334,34345, 2313, 424234,1312313]

    
    def keyPressEvent(self, keyEvent):
        key = keyEvent.key()
        char = keyEvent.text()
        if key in Character().special_chars:
            if key == 12313213: # shift
                pass
            elif key == 42143311233: # enter
                pass
        if char in Character().lower_case:
            if char != Exercise.next_char:
                Exercise.failures += 1
            Exercise.next_char += 1