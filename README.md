# Optical_Character_Recognition

## Overview

This is a simple Optical Character Recognition (OCR) application built using Python. The application allows users to select an image file and extracts text from the image using the Tesseract OCR engine.

## Features

- Select an image file (PNG, JPG, JPEG, GIF, BMP) for OCR.
- Preprocess the image (grayscale conversion, contrast enhancement, sharpening) to improve OCR accuracy.
- Display the extracted text in a message box.

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- Pillow (Python Imaging Library)
- Pytesseract (Python wrapper for Google's Tesseract-OCR Engine)
- Tesseract-OCR (must be installed separately)

## Installation

1. Install Tesseract-OCR:

   Download and install Tesseract-OCR from [here](https://github.com/tesseract-ocr/tesseract). Make sure to note the installation path, as you will need it later.

2. Clone this repository:

   ```bash
   git clone https://github.com/A1tiJoshi/ocr-application.git
   cd ocr-application

3. Install required Python packages:
    pip install pillow pytesseract

4. Update the Tesseract-OCR path:
     pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

