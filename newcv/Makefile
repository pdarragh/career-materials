LATEX ?= lualatex
BIBTEX ?= bibtex

TARGET := newcv.pdf

.DEFAULT_GOAL: default
.PHONY: clean default

default: $(TARGET)

clean:
	-$(RM) *.aux *.log *.out

clean-all: clean
	-$(RM) $(TARGET)

%.pdf: %.tex
	$(LATEX) $(basename $<)
	$(LATEX) $(basename $<)
