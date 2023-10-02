LATEX ?= lualatex
BIBTEX ?= bibtex

.DEFAULT_GOAL: default
.PHONY: clean default

default: cv.pdf

clean:
	-$(RM) *.aux *.log *.out

%.pdf: %.tex cv.sty
	$(LATEX) $(basename $<)
	$(LATEX) $(basename $<)
