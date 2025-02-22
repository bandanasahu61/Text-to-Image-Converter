from PIL import Image, ImageDraw, ImageFont

class ImageGenerator:
    def __init__(self):
        self.default_font_size = 48
        try:
            # Try to use Arial font
            self.default_font = "arial.ttf"
            # Test if font works
            ImageFont.truetype(self.default_font, self.default_font_size)
        except:
            # Fallback to default system font
            try:
                # For Windows
                self.default_font = "C:\\Windows\\Fonts\\arial.ttf"
            except:
                try:
                    # For Linux/Mac
                    self.default_font = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
                except:
                    # Final fallback
                    self.default_font = ImageFont.load_default()

    def create_image(self, text, font_size=None, text_color="black", bg_color="white", alignment="center"):
        if font_size is None:
            font_size = self.default_font_size

        # Create font object
        if isinstance(self.default_font, str):
            font = ImageFont.truetype(self.default_font, font_size)
        else:
            font = self.default_font

        # Split text into lines
        lines = text.split('\n')
        
        # Calculate the maximum width and total height
        max_width = 0
        total_height = 0
        line_heights = []
        line_widths = []

        for line in lines:
            # Get text bbox
            left, top, right, bottom = font.getbbox(line)
            line_width = right - left
            line_height = bottom - top
            max_width = max(max_width, line_width)
            total_height += line_height
            line_heights.append(line_height)
            line_widths.append(line_width)

        # Add padding
        padding = 20
        img_width = max_width + (2 * padding)
        img_height = total_height + (2 * padding) + (len(lines) - 1) * 5

        # Create actual image
        img = Image.new('RGB', (img_width, img_height), bg_color)
        draw = ImageDraw.Draw(img)

        # Draw text line by line
        y = padding
        for i, line in enumerate(lines):
            # Calculate x position based on alignment
            if alignment == "left":
                x = padding
            elif alignment == "right":
                x = img_width - line_widths[i] - padding
            else:  # center
                x = (img_width - line_widths[i]) // 2

            # Draw the text
            draw.text((x, y), line, font=font, fill=text_color)
            y += line_heights[i] + 5  # Add 5 pixels spacing between lines

        return img
