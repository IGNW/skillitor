# Skillitor
Extensible skill-tracking microservice

![Skillitor logo](skillitor_250x250.png)


## ANTLR parser generator

[ANTLR](https://www.antlr.org/) is used to generate code to parse our
interactive query language (skillquery).

macos install

    brew install antlr   
    pip install antlr4-python3-runtime

If you just cloned the repository the or '.g4' grammar file has changed then
you need to re-generating the parser code.

    cd src/skillquery
    antlr -o antlr_files skillquery.g4
