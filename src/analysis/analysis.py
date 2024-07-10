import spacy

def analyze_resume_with_spacy(text):
    """
    Analyzes the resume text using spaCy to extract key phrases and keywords.
    
    Args:
        text (str): The resume text to analyze.
    
    Returns:
        dict: A dictionary containing extracted key phrases and keywords.
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    
    key_phrases = [chunk.text for chunk in doc.noun_chunks]
    keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]
    
    analysis_result = {
        "key_phrases": key_phrases,
        "keywords": keywords
    }
    
    print(f"Key phrases extracted: {key_phrases}")
    print(f"Keywords extracted: {keywords}")
    
    return analysis_result

def save_analysis_to_file(analysis_result, output_path):
    """
    Saves the analysis result to a file.
    
    Args:
        analysis_result (dict): The analysis result containing key phrases and keywords.
        output_path (str): The path to the output file.
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        for key, values in analysis_result.items():
            f.write(f"{key.capitalize()}:\n")
            for value in values:
                f.write(f"- {value}\n")
            f.write("\n")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        text_path = sys.argv[1]
        output_path = sys.argv[2]
        with open(text_path, 'r', encoding='utf-8') as f:
            text = f.read()
        result = analyze_resume_with_spacy(text)
        save_analysis_to_file(result, output_path)
    else:
        print("Please provide the path to the text file and the output file.")
