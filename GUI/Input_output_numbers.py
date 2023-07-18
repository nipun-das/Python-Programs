from breezypythongui import EasyFrame
import math


class IntegerField(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Square root")

        self.addLabel(text="Input integer", row=0, column=0)
        self.inputField = self.addIntegerField(value=0, row=0, column=1, width=10)

        self.addLabel(text="Square root", row=1, column=0)
        self.outputField = self.addFloatField(value=0.0, row=1, column=1, width=8, precision=2, state="readonly")

        self.addButton(text="Convert", row=2, column=0, columnspan=2, command=self.compute)

    def compute(self):
        try:
            n = self.inputField.getNumber()
            result = math.sqrt(n)
            self.outputField.setNumber(result)
        except ValueError:
            self.messageBox(title="Error", message="Input must be an integer")


def main():
    IntegerField().mainloop()


if __name__ == "__main__":
    main()
