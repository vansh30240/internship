import re
import json
import spacy
from PyPDF2 import PdfReader


nlp = spacy.load("en_core_web_sm")


def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text


email_regex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
phone_regex = r"\+?\d[\d -]{8,}\d"


skills_list = ["Python","Java","C++","Machine Learning","Data Science",
               "Excel","Power BI","SQL","NLP","Django","React","AWS","Git"]


def parse_resume(text):
    doc = nlp(text)

   
    name = None
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text
            break

    
    email = re.findall(email_regex, text)
    phone = re.findall(phone_regex, text)

    
    education_keywords = ["Bachelor", "B.Tech", "B.E", "M.Tech", "Master", "BSc", "MSc", "Diploma"]
    education = [line for line in text.split("\n") if any(kw in line for kw in education_keywords)]

    
    experience_keywords = ["experience", "intern", "internship", "worked", "company"]
    experience = [line for line in text.split("\n") if any(kw.lower() in line.lower() for kw in experience_keywords)]

    
    skills = [skill for skill in skills_list if skill.lower() in text.lower()]

   
    data = {
        "Name": name,
        "Email": email[0] if email else None,
        "Phone": phone[0] if phone else None,
        "Education": education,
        "Experience": experience,
        "Skills": list(set(skills)) 
    }

    return json.dumps(data, indent=4)


if __name__ == "__main__":
    file = "sample_resume.pdf"
    resume_text = read_pdf(file)
    result = parse_resume(resume_text)
    print("\n📌 Extracted Resume Data:")
    print(result)
