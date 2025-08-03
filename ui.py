
import ttkbootstrap as ttk
import function


def main():
    # Create window
    window = ttk.Window(themename="superhero")
    # Set window Title
    window.title("Arrange files in Folder")
    # Set Window size
    window.geometry("500x250")

    # Variable declaration
    user_input = ttk.StringVar()
    output = ttk.StringVar(value="Result :")

    # Creating an entry field
    entry = ttk.Entry(window, width=50, background="#aaccaa", font=("Arial", 12), textvariable=user_input)
    entry.pack(pady=20, padx=20)

    func = function.Sorter(user_input, output)

    # Creating a button to perform the task
    calculate_button = ttk.Button(window, text="Arrange", command=lambda: func.sort())
    calculate_button.pack()

    # Show text in the window
    result_label = ttk.Label(window, textvariable=output)
    result_label.pack()

    # Start the window
    window.mainloop()