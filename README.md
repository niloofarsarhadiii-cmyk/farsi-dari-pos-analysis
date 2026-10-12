# Farsi vs. Dari: Evaluating a Persian POS Tagger on Dari Text

**Status:** In progress (started [month, year]). Results below are preliminary.

## Question
How well does a part-of-speech (POS) tagger trained on Farsi perform on Dari, and what kinds of errors does it make?

Dari and Farsi are closely related varieties of Persian, but Dari has far fewer NLP resources. This project is a first step toward studying discourse and coreference for Dari.

## Data
- **Farsi baseline:** the Persian-Seraji treebank from Universal Dependencies (gold-standard POS tags).
- **Dari test set:** [number] sentences collected from [describe sources, e.g., news websites, with links or citations], annotated by hand with Universal POS tags. Source texts are not republished here; only short sentences and citations are included.

## Method
1. Run the Stanza Persian POS tagger on the Farsi baseline and measure accuracy.
2. Run the same tagger on the Dari sentences and measure accuracy against my hand annotations.
3. Group the errors into types (for example vocabulary differences, verb forms, borrowed words, spelling) and count each type.

Tools: Python, Stanza.

## Results
- Farsi accuracy: [x]%
- Dari accuracy: [y]%
- Most common error types on Dari: [list, with one or two example words each]

## Limitations
- Small sample ([number] sentences) from limited sources.
- Annotated by one person, so annotation consistency has not been measured.
- Results are preliminary and should not be generalized to all Dari text.

## Next steps
- Have a second annotator tag a sample and report agreement.
- Extend the analysis to discourse and coreference.

## How to run
    pip install stanza
    python pos_tagging.py

## Author
Niloofar Sarhadi
[niloofar.sarhadiii@gmail.com]# farsi-dari-pos-analysis
Evaluating a Farsi POS tagger on Dari text
