PDFLATEX ?= pdflatex
BIBTEX ?= bibtex

.DEFAULT_GOAL: default
.PHONY: clean default

default: resume.pdf

clean:
	-$(RM) *.aux *.log *.out

%.pdf: %.tex cv.sty
	$(PDFLATEX) $(basename $<)
	$(PDFLATEX) $(basename $<)
