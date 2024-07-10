import markdown

def markdown_to_html(markdown_text):
    return markdown.markdown(markdown_text)

if __name__ == "__main__":
    sample_md = """
    # Sample Title

    This is a sample markdown file to test the conversion to HTML.

    ## Sample Heading

    - Item 1
    - Item 2
    - Item 3
    """
    html = markdown_to_html(sample_md)
    print(html)
