class TemplateStats:
    def __init__(self):
        self.usage = 0
        self.success = 0

    def record(self, success: bool):
        self.usage += 1
        if success:
            self.success += 1

    @property
    def success_rate(self):
        return self.success / max(1, self.usage)
