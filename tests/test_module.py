import pytest
import os
import pylog

def test_log():
    pylog.log("pytest.log","Test Log")

def test_debug():
    pylog.debug("pytest.log","Test Log")

def test_info():
    pylog.info("pytest.log","Test Log")

def test_warn():
    pylog.warn("pytest.log","Test Log")

def test_error():
    pylog.error("pytest.log","Test Log")

def test_cerror():
    pylog.cerror("pytest.log","Test Log")

def test_ferror():
    pylog.ferror("pytest.log","Test Log")

def test_message():
    pylog.message("pytest.log","Test Log")
