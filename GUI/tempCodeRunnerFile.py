def clear(self):
    self.label["text"] = ""
    self.clearBtn["state"] = "disabled"
    self.restoreBtn["state"] = "normal"


def restore(self):
    self.label["text"] = "Hello World!"
    self.clearBtn["state"] = "normal"
    self.restoreBtn["state"] = "disabled"