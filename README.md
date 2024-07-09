# Document Formatter

## Overview

This repository contains scripts for converting Markdown files to formatted DOCX files and subsequently converting them to PDF. The scripts are designed to ensure ATS (Applicant Tracking System) friendly formatting, making it easier for job applications.

## Scripts

### `text_to_pretty_docx.py`

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

2. **Run the Script**:
   - Execute the script to select a Markdown file and save the DOCX and PDF files:
     ```bash
     python text_to_pretty_docx.py
     ```

3. **Functionality**:
   - The script will open a file dialog to select a Markdown file.
   - It will then convert the Markdown content to a formatted DOCX file.
   - Finally, it will convert the DOCX file to a PDF file.

## Example Usage

1. **Markdown File**:
   ```markdown
   # Professional Summary
   Detail-oriented and analytical recent graduate with a B.A. in Economics and a certification in Elements of Computing from the University of Texas at Austin.
