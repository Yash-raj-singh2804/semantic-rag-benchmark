from typing import List

def chunk_text(text: str) -> List[str]:
    paragraphs = [
        paragraph.strip()
        for paragraph in text.split("\n\n")
        if paragraph.strip()
    ]

    return paragraphs