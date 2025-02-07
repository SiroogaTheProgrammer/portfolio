import tkinter as tk
from tkinter import filedialog
import fitz
import requests


def fetch_word_data(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    data = response.json()

    # Extract word meaning and format it
    if isinstance(data, list):
        meanings = data[0]['meanings']
        word_info = f"Word: {word}\n\n"
        for meaning in meanings:
            part_of_speech = meaning['partOfSpeech']
            word_info += f"Part of speech: {part_of_speech}\n"
            for definition in meaning['definitions']:
                word_info += f"Definition: {definition['definition']}\n\n"
    else:
        word_info = f"No definition found for: {word}"

    return word_info

# Function to display the fetched word info in a Tkinter window
def display_word_info(word):
    # Fetch word data from API
    word_data = fetch_word_data(word)

    # Create a new Tkinter window to display word info
    info_window = tk.Toplevel(root)
    info_window.title(f"Definition of {word}")

    # Create a Text widget to display word info
    text_widget = tk.Text(info_window, wrap="word", padx=10, pady=10, font=("Helvetica", 12))
    text_widget.pack(expand=True, fill="both")

    # Insert word data into the Text widget
    text_widget.insert(tk.END, word_data)

    # Add color for specific parts of speech
    highlight_color(text_widget, "noun", "blue")
    highlight_color(text_widget, "adjective", "green")
    highlight_color(text_widget, "verb", "red")
    highlight_color(text_widget, "Definition:", "purple")

    # Make the text widget read-only
    text_widget.config(state=tk.DISABLED)

# Function to highlight specific words (parts of speech or "Definition:") in the Text widget
def highlight_color(text_widget, word, color):
    start_idx = "1.0"
    while True:
        start_idx = text_widget.search(word, start_idx, stopindex=tk.END)
        if not start_idx:
            break
        end_idx = f"{start_idx}+{len(word)}c"
        text_widget.tag_add(word, start_idx, end_idx)
        text_widget.tag_config(word, foreground=color)
        start_idx = end_idx


def open_text_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, content)

def open_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        doc = fitz.open(file_path)  # Open the PDF file
        text = ""

    # Loop through each page in the PDF
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)  # Load each page
            text += page.get_text()  # Extract text from the page
        
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, text)
        
def get_selected_text(event):
    # Get the selected text
    try:
        selected_text = text_area.get(tk.SEL_FIRST, tk.SEL_LAST)
        display_word_info(selected_text)

    except tk.TclError:
        # This exception is raised if no text is selected
        pass

# Create the main application window
root = tk.Tk()
root.title("File Viewer")

# Create a text area widget for displaying text files
text_area = tk.Text(root, wrap='word', height=25, width=80)
text_area.pack(padx=10, pady=10)

text_area.bind("<ButtonRelease-1>", get_selected_text)

# Create a frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Create the "Open Text File" button
text_button = tk.Button(button_frame, text="Open Text File", command=open_text_file, width=20)
text_button.pack(side=tk.LEFT, padx=10)

# Create the "Open PDF File" button
pdf_button = tk.Button(button_frame, text="Open PDF File", command=open_pdf_file, width=20)
pdf_button.pack(side=tk.LEFT, padx=10)

# Run the Tkinter event loop
root.mainloop()
