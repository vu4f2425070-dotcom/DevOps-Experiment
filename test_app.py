
from pathlib import Path

def test_homepage_contains_welcome_message():
    html = Path("index.html").read_text(encoding="utf-8")
    assert "Welcome to DevOps Pipeline!" in html

def test_homepage_has_html_structure():
    html = Path("index.html").read_text(encoding="utf-8")
    assert "<html>" in html
    assert "</html>" in html
