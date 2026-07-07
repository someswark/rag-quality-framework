from pathlib import Path
from datetime import datetime

from utilities.template_engine import TemplateEngine


class DetailedReportGenerator:

    def __init__(self, context):

        self.context = context
        self.config_loader = context.get_config_loader()

    def generate(self, summary, results):

        values = self._build_values(summary, results)

        template_file = (
            Path(__file__).parent.parent
            / "templates"
            / "detailed_report_template.html"
        )

        output_file = (
            Path(__file__).parent.parent.parent
            / "website"
            / "assets"
            / "reports"
            / "detailed-report.html"
        )

        TemplateEngine.render(
            template_file,
            output_file,
            values
        )

    def _build_values(self, summary, results):

        framework = self.config_loader.get_framework()

        application = self.config_loader.get_application()

        execution = self.config_loader.get_execution()

        return {

            "CSS": self._load_css(),

            "FRAMEWORK_NAME": framework.get("name"),

            "FRAMEWORK_VERSION": framework.get("version"),

            "APPLICATION_NAME": application.get("name"),

            "EXECUTION_MODE": execution.get("mode").title(),

            "TOTAL_QUESTIONS": summary.total_questions,

            "GENERATED_DATE": self._generated_date(),

            "QUESTION_CARDS": self._build_question_cards(results)

        }

    def _load_css(self):

        css_file = (
            Path(__file__).parent.parent
            / "templates"
            / "report.css"
        )

        return css_file.read_text(
            encoding="utf-8"
        )

    def _generated_date(self):

        return datetime.now().strftime(
            "%d-%b-%Y %H:%M"
        )

    def _build_question_cards(self, results):

        cards = ""

        for result in results:

            badge = self._status_class(result.status)

            cards += f"""

<div class="question-card">

<h3>{result.category}</h3>

<p>
<strong>Question</strong>
</p>

<div class="answer">
{result.question}
</div>

<p>
<strong>Expected Answer</strong>
</p>

<div class="answer">
{result.expected_answer}
</div>

<p>
<strong>Generated Answer</strong>
</p>

<div class="answer">
{result.generated_answer}
</div>

<div class="metrics">

    <div class="metric">
        <span class="{badge}">
            {result.status}
        </span>
    </div>

    <div class="metric">
        Confidence : {result.confidence}%
    </div>

    <div class="metric">
        Latency : {result.latency_ms} ms
    </div>

</div>

</div>

"""

        return cards

    def _status_class(self, status):

        if status == "PASS":

            return "status status-pass"

        elif status == "REVIEW":

            return "status status-review"

        return "status status-fail"