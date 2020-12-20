BLENDER_DOWNLOAD=https://ftp.halifax.rwth-aachen.de/blender/release/Blender2.83/blender-2.83.9-linux64.tar.xz
PIP_DOWNLOAD=https://bootstrap.pypa.io/get-pip.py

PYTHON_PATH=blender/2.83/python/bin/

PIP3=$(PYTHON_PATH:=pip3)
PYTHON3=$(PYTHON_PATH:=python3.7m)

# maybe we could install blender directly in setup.py
# https://stackoverflow.com/questions/20288711/post-install-script-with-python-setuptools
# For example, if I want to install the package in developer mode. I would run
# `pip install -e .`. Yet, this Makefile uses `python setup.py install`.
all: blender $(wildcard two4two/**/*)
	$(PYTHON3) setup.py install
	python setup.py install

blender: blender.tar.xz get-pip.py
	tar -xf blender.tar.xz
	mv blender-2.83.9-linux64 blender
	$(PYTHON3) get-pip.py
	$(PIP3) install -U pip
	$(PIP3) install numpy scipy matplotlib ipykernel

blender.tar.xz:
	curl $(BLENDER_DOWNLOAD) -o blender.tar.xz

get-pip.py:
	curl $(PIP_DOWNLOAD) -o get-pip.py

clean:
	rm -f blender.tar.xz
	rm -f get-pip.py

remove: clean
	rm -rf blender dist build two4two_laserschwelle.egg-info
