from pathlib import Path
from utilities.template_engine import TemplateEngine

template_file = Path("templates/test_template.html")
output_file = Path("templates/test_output.html")

values = {
    "TITLE": "Template Engine Test",
    "MESSAGE": "Congratulations! Template engine is working.",
    "SCORE": 89.2
}

TemplateEngine.render(
    template_file,
    output_file,
    values
)