import tkinter as tk
from tkinter import ttk, colorchooser, filedialog, messagebox
from image_generator import ImageGenerator
from PIL import Image, ImageTk
import os

class TextToImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Image Converter")
        self.root.geometry("800x700")
        self.root.configure(bg="#f0f0f0")
        
        self.image_generator = ImageGenerator()
        self.setup_ui()
        
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(
            main_frame, 
            text="Text to Image Converter", 
            font=("Helvetica", 16, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Text input
        input_frame = ttk.LabelFrame(main_frame, text="Text Input", padding="5")
        input_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        self.text_input = tk.Text(input_frame, height=4, width=50)
        self.text_input.grid(row=0, column=0, padx=5, pady=5)
        
        # Settings frame
        settings_frame = ttk.LabelFrame(main_frame, text="Settings", padding="5")
        settings_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        # Font size
        ttk.Label(settings_frame, text="Font Size:").grid(row=0, column=0, padx=5, pady=5)
        self.font_size = ttk.Spinbox(settings_frame, from_=8, to=120, width=10)
        self.font_size.set(48)
        self.font_size.grid(row=0, column=1, padx=5, pady=5)
        
        # Text alignment
        ttk.Label(settings_frame, text="Text Alignment:").grid(row=0, column=2, padx=5, pady=5)
        self.text_alignment = ttk.Combobox(settings_frame, values=["left", "center", "right"], width=10)
        self.text_alignment.set("center")
        self.text_alignment.grid(row=0, column=3, padx=5, pady=5)
        
        # Colors
        self.text_color = tk.StringVar(value="#000000")
        self.bg_color = tk.StringVar(value="#FFFFFF")
        
        color_frame = ttk.Frame(settings_frame)
        color_frame.grid(row=1, column=0, columnspan=4, pady=5)
        
        ttk.Button(
            color_frame, 
            text="Choose Text Color", 
            command=self.choose_text_color
        ).grid(row=0, column=0, padx=5)
        
        ttk.Button(
            color_frame, 
            text="Choose Background Color", 
            command=self.choose_bg_color
        ).grid(row=0, column=1, padx=5)
        
        # Preview frame
        preview_frame = ttk.LabelFrame(main_frame, text="Preview", padding="5")
        preview_frame.grid(row=3, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
        
        self.preview_label = ttk.Label(preview_frame)
        self.preview_label.grid(row=0, column=0, padx=5, pady=5)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=10)
        
        ttk.Button(
            button_frame, 
            text="Generate Preview", 
            command=self.generate_preview,
            style="Accent.TButton"
        ).grid(row=0, column=0, padx=5)
        
        ttk.Button(
            button_frame, 
            text="Save Image", 
            command=self.save_image
        ).grid(row=0, column=1, padx=5)
        
    def choose_text_color(self):
        color = colorchooser.askcolor(title="Choose Text Color", color=self.text_color.get())
        if color[1]:
            self.text_color.set(color[1])
            
    def choose_bg_color(self):
        color = colorchooser.askcolor(title="Choose Background Color", color=self.bg_color.get())
        if color[1]:
            self.bg_color.set(color[1])
            
    def generate_preview(self):
        text = self.text_input.get("1.0", tk.END).strip()
        if text:
            try:
                font_size = int(self.font_size.get())
                img = self.image_generator.create_image(
                    text,
                    font_size=font_size,
                    text_color=self.text_color.get(),
                    bg_color=self.bg_color.get(),
                    alignment=self.text_alignment.get()
                )
                
                # Resize for preview if necessary
                display_size = (400, 300)
                preview_img = img.copy()
                preview_img.thumbnail(display_size)
                
                # Convert to PhotoImage for display
                photo = ImageTk.PhotoImage(preview_img)
                self.preview_label.configure(image=photo)
                self.preview_label.image = photo  # Keep a reference
                self.current_image = img  # Store the full-size image
            except Exception as e:
                messagebox.showerror("Error", f"Error generating image: {str(e)}")
        else:
            messagebox.showwarning("Warning", "Please enter some text first!")
                
    def save_image(self):
        if hasattr(self, 'current_image'):
            file_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
            )
            if file_path:
                try:
                    self.current_image.save(file_path)
                    messagebox.showinfo("Success", "Image saved successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"Error saving image: {str(e)}")
        else:
            messagebox.showwarning("Warning", "Generate a preview first!")

def main():
    root = tk.Tk()
    app = TextToImageApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
