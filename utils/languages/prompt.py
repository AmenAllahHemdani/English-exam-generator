
PROMPT_EXERCICE1 = """
You are an educational assistant creating a high school-level English exam.

## TASK

Using the context below, do the following:

1. Write one academic-style paragraph with:
   - Length: 180 to 250 words  
   - Tone: Educational, formal, and suitable for high school students  
   - **No blanks and no words in parentheses**  

2. Select exactly **6 one-word content words** (adjectives, verbs, or prepositions) that are:
   - **Used only once** in the paragraph  
   - **Not adjacent to each other (at least 5 words apart)** 
   - **Evenly distributed across the paragraph**  
   - **Not located in the first or last sentence**

3. Then, choose **two (2) distractor words**:
   - Each must be a **single word** (noun, verb, adjective, or adverb)  
   - Must **not appear anywhere** in the paragraph  
   - Must be plausible in the context but clearly incorrect choices  

4. Output your result as a valid **JSON object** with three fields: `paragraph`, `correct_words`, and `distractors`.

## OUTPUT FORMAT (STRICTLY THIS, NO EXTRA TEXT):

{{
  "paragraph": "Your generated paragraph here ",
  "correct_words": ["word1", "word2", "word3", "word4", "word5", "word6"],
  "distractors": ["distractor1", "distractor2"]
}}

## RULES
- Do **not** use any correct word more than once.
- Do **not** include correct or distractor words in the first or last sentence.
- Ensure correct words are **well spaced** (at least 4 unrelated words between them).
- Ensure paragraph content is original and clearly based on the context.
- Ensure all correct words are used **exactly as they appear** in the paragraph with same form and tense.

## CONTEXT
{context}

"""




PROMPT_EXERCICE2 = """
You are an educational assistant generating high school-level English exam exercises.

TASK:
Create ONE “Put the bracketed words in the right form or tense” exercise based on the chapter theme provided. Follow the instructions below exactly:

Paragraph Instructions:
- Write one coherent academic-style paragraph between 180 to 250 words.
- Use a formal, educational tone suitable for high school students.
- Do not include any blanks, parentheses, or special formatting in the paragraph.
- The paragraph must clearly reflect the theme of the provided chapter.

Target Word Instructions:
- Select exactly 6 one-word content words (verbs, adjectives, or adverbs) from the paragraph.
- Ensure:
  - At least 3 words require tense changes (e.g., past, future, passive, perfect).
  - At least 3 words require form changes (e.g., verb → noun, adjective → adverb).
  - All words are unique and appear only once in the paragraph.
  - The words are not adjacent to each other.
  - Distribute them evenly:
    - 2 in the first third,
    - 2 in the middle third,
    - 2 in the last third of the paragraph.
- Do not modify the words in the output list. Return them exactly as they appear in the paragraph with same form and tense.

INPUT:
Chapter: {context}

OUTPUT FORMAT (JSON):
{{
  "question": "Put the bracketed words in the right form or tense.",
  "paragraph": "Your generated paragraph goes here.",
  "words": ["word1", "word2", "word3", "word4", "word5", "word6"]
}}

Notes:
- Do not include explanations, notes, or formatting instructions in the output.
- Do not use any parentheses or blanks in the paragraph text.
- Ensure all words are witted **exactly as they appear** in the paragraph with same form and tense.

"""
