from breezypythongui import EasyFrame


class TextField(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Small to Caps")

        self.addLabel(text="Input", row=0, column=0)
        self.inputField = self.addTextField(text="", row=0, column=1)

        self.addLabel(text="Output", row=1, column=0)
        self.outputField = self.addTextField(text="", row=1, column=1, state="readonly")

        self.addButton(
            text="Convert", row=2, column=0, columnspan=2, command=self.convert
        )

    def convert(self):
        text = self.inputField.getText()
        result = text.upper()
        self.outputField.setText(result)


def main():
    TextField().mainloop()


if __name__ == "__main__":
    main()
