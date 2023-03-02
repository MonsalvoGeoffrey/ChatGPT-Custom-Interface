class Message():
    def __init__(self, role, content):
        self.role = role
        self.content = content

    def __repr__(self):
        return f"Message({self.role}, {self.content})"
    
    def asdict(self):
        return {"role": self.role, "content": self.content}