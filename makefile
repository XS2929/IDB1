FILES :=                       \           
    overwatchdb/models_test.py    \
    overwatchdb/test_runner.py    \
    overwatchdb/models.py      
    
ifeq ($(shell uname), Darwin)          # Apple
    PYTHON   := python3.5
    PIP      := pip3.5
    MYPY     := mypy
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else ifeq ($(CI), true)                # Travis CI
    PYTHON   := python3.5
    PIP      := pip3.5
    MYPY     := mypy
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else ifeq ($(shell uname -p), unknown) # Docker
    PYTHON   := python3.5
    PIP      := pip3.5
    MYPY     := mypy
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else                                   # UTCS
    PYTHON   := python3
    PIP      := pip3
    MYPY     := mypy
    PYLINT   := pylint3
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
endif

.PHONY: testsout.tmp
testsout.tmp: .pylintrc
	-$(MYPY) overwatchdb/test_runner.py
	-$(PYLINT) overwatchdb/test_runner.py
	-$(COVERAGE) run    --branch overwatchdb/test_runner.py >  testsout.tmp 2>&1
	-$(COVERAGE) report -m                      >> testsout.tmp
	cat TestCollatz.tm

