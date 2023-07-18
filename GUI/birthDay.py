from datetime import date
from breezypythongui import EasyFrame


class a5(EasyFrame):
    def _init_(self):
        EasyFrame._init_(self)
        self.addLabel(text="birthdate(yyy-mm-dd", row=0, column=0)
        self.day = self.addTextField(text="", row=0, column=1)
        
        self.addLabel(text="AGE", row=1, column=0)
        self.out = self.addTextField(text="", row=1, column=1)
        
        self.addButton(text="calculate", row=2, column=0, columnspan=2, command=self.find)

    def find(self):
        a1 = self.day.getText()
        a2 = date.fromisoformat(a1)
        today = date.today()
        age = today.year - a2.year

        if today < date(today.year, a2.month, a2.day):
            age -= 1
        self.out.setText(age)


def main():
    a5().mainloop()


if _name__ == "__main_":
    main()
