import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class OCRApplication:
    def __init__(self, master):
        self.master = master
        master.title("Image OCR")

        self.label = tk.Label(master, text="Click below to select an image for OCR:")
        self.label.pack()

        self.select_button = tk.Button(master, text="Select Image", command=self.select_image)
        self.select_button.pack()

    def select_image(self):
        file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        if file_path:
            extracted_text = self.perform_ocr(file_path)
            if extracted_text:
                messagebox.showinfo("OCR Result", "Text Extracted Successfully:\n\n" + extracted_text)
            else:
                messagebox.showwarning("OCR Error", "No text could be extracted from the selected image.")
        else:
            messagebox.showwarning("Image Selection", "No image selected.")

    def perform_ocr(self, image_path):
        try:
            image = Image.open(image_path)
            
            # Preprocessing
            processed_image = self.preprocess_image(image)
            
            # Perform OCR on the preprocessed image
            extracted_text = pytesseract.image_to_string(processed_image)
            
            if extracted_text.strip():
                return extracted_text.strip()
            else:
                messagebox.showwarning("OCR Error", "No text could be extracted from the image.")
                return None
        except Exception as e:
            messagebox.showerror("OCR Error", f"An error occurred during OCR: {str(e)}")
            return None

    def preprocess_image(self, image):
        # Convert to grayscale
        grayscale_image = image.convert('L')
        
        # Enhance contrast
        enhanced_image = ImageEnhance.Contrast(grayscale_image).enhance(2.0)
        
        # Apply sharpening
        sharpened_image = enhanced_image.filter(ImageFilter.SHARPEN)
        
        return sharpened_image

def main():
    root = tk.Tk()
    app = OCRApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()
