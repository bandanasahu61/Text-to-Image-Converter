# Text to Image Converter

A simple GUI application to convert text into images using Python's **Tkinter** and **PIL** libraries. The application allows users to enter text, customize font size, colors, and alignment, preview the image, and save it as a PNG file.

## Features
- GUI-based text-to-image generation
- Customizable font size, text color, background color, and alignment
- Live preview before saving the image
- Save the generated image in PNG format

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/TextToImageConverter.git
   cd TextToImageConverter
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the application:
   ```sh
   python app.py
   ```

## Dependencies
- `tkinter` (for GUI)
- `Pillow` (for image processing)

## Usage
1. Enter text in the input box.
2. Select font size, text alignment, and colors.
3. Click **Generate Preview** to see how the image looks.
4. Click **Save Image** to export the image as a PNG file.

## File Structure
```
TextToImageConverter/
│── image_generator.py   # Handles text-to-image conversion
│── app.py               # Main Tkinter application
│── requirements.txt     # Python dependencies
│── README.md            # Documentation
```

## License
This project is open-source and available under the MIT License.
