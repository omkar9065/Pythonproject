from tkinter import *
from tkinter import messagebox


def clearAll():
    dayField.delete(0, END)
    monthField.delete(0, END)
    yearField.delete(0, END)
    givenDayField.delete(0, END)
    givenMonthField.delete(0, END)
    givenYearField.delete(0, END)
    rsltDayField.delete(0, END)
    rsltMonthField.delete(0, END)
    rsltYearField.delete(0, END)


def checkError():
    if (dayField.get() == "" or monthField.get() == "" or yearField.get() == "" or
        givenDayField.get() == "" or givenMonthField.get() == "" or givenYearField.get() == ""):
        messagebox.showerror("Input Error", "All fields are required!")
        clearAll()
        return -1


def calculateAge():
    value = checkError()
    if value == -1:
        return
    else:
        birth_day = int(dayField.get())
        birth_month = int(monthField.get())
        birth_year = int(yearField.get())

        given_day = int(givenDayField.get())
        given_month = int(givenMonthField.get())
        given_year = int(givenYearField.get())

        # Days in each month
        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Borrow days
        if birth_day > given_day:
            given_month -= 1
            given_day += month[birth_month - 1]

        # Borrow months
        if birth_month > given_month:
            given_year -= 1
            given_month += 12

        calculated_day = given_day - birth_day
        calculated_month = given_month - birth_month
        calculated_year = given_year - birth_year

        rsltDayField.insert(10, str(calculated_day))
        rsltMonthField.insert(10, str(calculated_month))
        rsltYearField.insert(10, str(calculated_year))


if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="light green")
    gui.title("Age Calculator")
    gui.geometry("525x300")

    # Labels
    dob = Label(gui, text="Date of Birth", bg="blue", fg="white")
    givenDate = Label(gui, text="Given Date", bg="blue", fg="white")

    day = Label(gui, text="Day", bg="light green")
    month = Label(gui, text="Month", bg="light green")
    year = Label(gui, text="Year", bg="light green")

    givenDay = Label(gui, text="Given Day", bg="light green")
    givenMonth = Label(gui, text="Given Month", bg="light green")
    givenYear = Label(gui, text="Given Year", bg="light green")

    rsltYear = Label(gui, text="Years", bg="light green")
    rsltMonth = Label(gui, text="Months", bg="light green")
    rsltDay = Label(gui, text="Days", bg="light green")

    # Buttons
    resultantAge = Button(gui, text="Resultant Age", fg="Black", bg="Red", command=calculateAge)
    clearAllEntry = Button(gui, text="Clear All", fg="Black", bg="Red", command=clearAll)

    # Entry fields
    dayField = Entry(gui)
    monthField = Entry(gui)
    yearField = Entry(gui)

    givenDayField = Entry(gui)
    givenMonthField = Entry(gui)
    givenYearField = Entry(gui)

    rsltYearField = Entry(gui)
    rsltMonthField = Entry(gui)
    rsltDayField = Entry(gui)

    # Positioning
    dob.grid(row=0, column=1, pady=5)
    givenDate.grid(row=0, column=4, pady=5)

    day.grid(row=1, column=0)
    dayField.grid(row=1, column=1)

    month.grid(row=2, column=0)
    monthField.grid(row=2, column=1)

    year.grid(row=3, column=0)
    yearField.grid(row=3, column=1)

    givenDay.grid(row=1, column=3)
    givenDayField.grid(row=1, column=4)

    givenMonth.grid(row=2, column=3)
    givenMonthField.grid(row=2, column=4)

    givenYear.grid(row=3, column=3)
    givenYearField.grid(row=3, column=4)

    resultantAge.grid(row=4, column=2, pady=10)

    rsltYear.grid(row=5, column=1)
    rsltYearField.grid(row=5, column=2)

    rsltMonth.grid(row=6, column=1)
    rsltMonthField.grid(row=6, column=2)

    rsltDay.grid(row=7, column=1)
    rsltDayField.grid(row=7, column=2)

    clearAllEntry.grid(row=8, column=2, pady=10)

    gui.mainloop()
