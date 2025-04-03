class Actor:
    """Representa un actor en el patrón Screenplay."""
    
    def __init__(self, name):
        self.name = name

    def attempts_to(self, task, *args, **kwargs):
        return task.perform(*args, **kwargs)
