import re

# Domain-specific keywords (can expand)
DOMAIN_KEYWORDS = {
    "SALES": ["sales", "leads", "revenue", "target", "pitch", "CRM", "pipeline"],
    "HR": ["recruitment", "employee", "onboarding", "hrms", "talent", "benefits"],
    "ENGINEERING": ["design", "development", "system", "python", "java", "hardware"],
    "IT": ["software", "cloud", "network", "cybersecurity", "infrastructure", "linux"],
    "MARKETING": ["campaign", "seo", "branding", "digital", "ads", "content"],
}

CERTIFICATIONS = ["certified", "certificate", "certification", "pmp", "aws", "azure", "scrum"]
TOOLS = ["excel", "tableau", "sql", "jira", "powerbi", "hadoop", "git"]

def count_matches(words, text):
    return sum(1 for word in words if word.lower() in text.lower())

def estimate_experience(text):
    # Match things like 'X years', 'X+ years', 'X yrs', etc.
    match = re.findall(r"(\\d+)[+ ]*(?:years|yrs)", text.lower())
    if match:
        return min(20, sum(int(m) for m in match))  # Cap at 20 years
    return 0

from typing import Tuple

def compute_capability_score(text: str, predicted_category: str) -> Tuple[int, int]:
    score = 0
    max_score = 100

    # 1. Keyword score (40 pts)
    keyword_hits = count_matches(DOMAIN_KEYWORDS.get(predicted_category, []), text)
    score += min(keyword_hits * 5, 40)

    # 2. Experience score (30 pts)
    years = estimate_experience(text)
    score += min(years * 3, 30)

    # 3. Certification score (15 pts)
    certs = count_matches(CERTIFICATIONS, text)
    score += min(certs * 5, 15)

    # 4. Tools score (15 pts)
    tools = count_matches(TOOLS, text)
    score += min(tools * 3, 15)

    return round(min(score, max_score)), years
