from Structures.stack import Stack

class UndoRedoManager:
    def __init__(self):
        self.undo_stack = Stack()
        self.redo_stack = Stack()

    def save_state(self, current_text):
        # Save state for undo, clear redo when a new action happens
        self.undo_stack.push(current_text)
        self.redo_stack.clear()

    def undo(self, current_text):
        if self.undo_stack.is_empty():
            return current_text
        
        # Move current state to redo, then get previous state
        self.redo_stack.push(current_text)
        return self.undo_stack.pop()

    def redo(self, current_text):
        if self.redo_stack.is_empty():
            return current_text
            
        # Move current state back to undo, then get next state
        self.undo_stack.push(current_text)
        return self.redo_stack.pop()
