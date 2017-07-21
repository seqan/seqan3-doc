# Introduction
This repostitory contains scripts and files for generating API documenations automatically.
We are using

* Doxygen: http://www.stack.nl/~dimitri/doxygen/
* Breathe: https://github.com/michaeljones/breathe
* Sphinx: http://www.sphinx-doc.org/en/stable/
* ReadTheDocs: https://readthedocs.org/

# Why ?
The core team will be freed from maintaining in-house documentation systems and html / javascript works. :)

# How it works ?
1. Clone the SeqAn3 repository.
2. Run Doxygen to generate .xml files.
3. Run make_source.py to generate .rst files from .xml files.
4. Run Sphinx with Breathe exntension to generate .html files.
5. The API documentation will be available at: https://seqan3-api.readthedocs.org

* Github will send a signal to ReadTheDocs when the SeqAn3 repository has a update. Therefore, step 2-5 will be ran on ReadTheDocs.

# Contact
Please feel free to contact to the author (seqan3-doc@jongkyu.kim) if you have a question.
