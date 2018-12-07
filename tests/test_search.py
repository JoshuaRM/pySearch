import pytest
from urllib.parse import quote

from ..search import Search

def test_builtLink():
    tmpSearch = Search()
    tmpSearch.setEngine("amazon")
    tmpSearch.setDomain("com")
    tmpSearch.setQuery(["test", "query"])
    assert tmpSearch.buildLink() == "http://www.amazon.com/s/keywords=test%20query"

def test_encoding():
    tmpSearch = Search()
    tmpSearch.setEngine("amazon")
    tmpSearch.setDomain("com")
    unsafe = "A <string> with {unsafe chars"
    unsafe = unsafe.split()
    safe = unsafe
    for term in range(len(safe)):
        safe[term] = quote(safe[term].encode('utf8'))
    tmpSearch.setQuery(unsafe)
    assert tmpSearch.searchRaw == safe
