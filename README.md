# Document Formatter

## Overview

This repository contains scripts for converting Markdown files to formatted DOCX files and subsequently converting them to PDF. The scripts are designed to ensure ATS (Applicant Tracking System) friendly formatting, making it easier for job applications.

## Mission

The goal of this project is to provide a streamlined, efficient, and high-quality solution for converting Markdown content into professional documents. The focus is on maintaining ATS compatibility to enhance the chances of your resume or documents passing through automated recruitment systems like Taleo.

## Scripts

### `markdown_to_formatted_docx.py`

This script converts a Markdown file to a formatted DOCX file and then converts the DOCX file to a PDF. It uses the following modules:
- `markdown`: For converting Markdown to HTML.
- `docx`: For creating and manipulating DOCX files.
- `pypandoc`: For converting DOCX files to PDF.
- `beautifulsoup4`: For parsing HTML content.

#### How to Use

1. **Setup**:
   - Install the required packages:
     ```bash
     pip install markdown python-docx beautifulsoup4 pypandoc
     ```
   - Ensure Pandoc is installed. Download it from [Pandoc website](https://pandoc.org/installing.html).

   - For high-quality PDF conversion, install a LaTeX distribution like TeX Live or MikTeX:
     - **TeX Live** (Linux/macOS):
       ```sh
       sudo apt-get install texlive-full
       # or
       brew install --cask mactex
       ```
     - **MikTeX** (Windows):
       - Download from [MikTeX website](https://miktex.org/download).

2. **Run the Script**:
   - Execute the script to select a Markdown file, JSON configuration file, and save the DOCX and PDF files:
     ```bash
     python markdown_to_formatted_docx.py
     ```

3. **Functionality**:
   - The script will open file dialogs to select a Markdown file and a JSON formatting configuration file.
   - It will then convert the Markdown content to a formatted DOCX file.
   - Finally, it will convert the DOCX file to a PDF file using the `pdflatex` engine for high-quality output.

### Example Usage

1. **Markdown File**:
   ```markdown
   # Professional Summary
   Detail-oriented and analytical recent graduate with a B.A. in Economics and a certification in Elements of Computing from the University of Texas at Austin.
