from breezypythongui import EasyFrame


class a5(EasyFrame):
    def _init_(self):
        EasyFrame._init_(self)
        self.addLabel(text="rupee", row=0, column=0)
        self.rupp = self.addFloatField(value="", row=0, column=1)

        self.addLabel(text="euro", row=1, column=0)
        self.euro = self.addFloatField(value="", row=1, column=1)

        self.addButton(text="R to E", row=2, column=0, command=self.RtoE)
        self.addButton(text="e to r", row=2, column=1, command=self.EtoR)

    def RtoE(self):
        r = self.rupp.getNumber()
        e = r / 92
        self.euro.setNumber(e)

    def EtoR(self):
        e = self.euro.getNumber()
        r = e * 92
        self.rupp.setNumber(r)


def main():
    a5().mainloop()


if __name__ == "__main_":
    main()
