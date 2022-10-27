# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


    # Use a breakpoint in the code line below to debug your script.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   from tkinter import Label, Tk
   import time

   app_window = Tk()
   app_window.title("Digital Clock")
   app_window.geometry("1620x150")
   app_window.resizable(1, 1)

   text_font = ("Boulder", 68, 'bold')
   background = "#f2e750"
   foreground = "#363529"
   border_width = 25

   label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
   label.grid(row=0, column=1)


   def digital_clock():
      time_live = time.strftime("%H:%M:%S %p %A %B %d")
      label.config(text=time_live)
      label.after(200, digital_clock)

   digital_clock()
   app_window.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
