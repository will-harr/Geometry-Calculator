from gui import *

def main():
    window = Tk()
    window.title('Geometry Calculator')
    window.geometry('250x240')
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()

if __name__ == '__main__':
    main()