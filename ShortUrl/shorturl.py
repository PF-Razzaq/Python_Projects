import tkinter as tk
import pyshorteners as short
import pyperclip as clip

def shortenerurl():
    url = entry.get()
    if url:
        s = short.Shortener()
        shortened_url = s.tinyurl.short(url)
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, shortened_url)
        result_text.config(state=tk.DISABLED)
        clip.copy(shortened_url)
        status_label.config(text="URL copied to clipboard.")
    else:
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please enter a URL.")
        result_text.config(state=tk.DISABLED)
        status_label.config(text="")

# Create the main Tkinter window
app = tk.Tk()
app.title("URL Shortener")

# Create and place the components
label = tk.Label(app, text="Enter the URL:")
label.pack(pady=10)

entry = tk.Entry(app, width=40)
entry.pack(pady=10)

button = tk.Button(app, text="Shorten URL", command=shortenerurl)
button.pack(pady=10)

result_text = tk.Text(app, height=1, width=40, state=tk.DISABLED)
result_text.pack(pady=10)

status_label = tk.Label(app, text="")
status_label.pack(pady=10)

# Start the Tkinter event loop
app.mainloop()
