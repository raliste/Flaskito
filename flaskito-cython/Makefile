PYX_FILES := $(shell find -L . -name \*.pyx)
PYXSO_FILES := $(PYX_FILES:.pyx=.so)

all:	$(PYXSO_FILES)

$(PYXSO_FILES): %.so : %.pyx
	rm -f $(<:.pyx=.pyc)
	cython $<
	mkdir -p tmp
	PYTHONPATH=tmp python pyx_setup.py develop -d tmp -b tmp $<
	rm -r tmp
