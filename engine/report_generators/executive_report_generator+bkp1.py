from pathlib import Path
from datetime import datetime

from utilities.template_engine import TemplateEngine


class ExecutiveReportGenerator:

    def __init__(self, context):

        self.context = context
        self.config_loader = context.get_config_loader()

    def generate(self, summary):

        framework = self.config_loader.get_framework()
        application = self.config_loader.get_application()
        execution = self.config_loader.get_execution()

        template_file = (
            Path(__file__).parent.parent
            / "templates"
            / "executive_report_template.html"
        )

        css_file = (
            Path(__file__).parent.parent
            / "templates"
            / "report.css"
        )

        output_file = (
            Path(__file__).parent.parent.parent
            / "website"
            / "assets"
            / "reports"
            / "executive-report.html"
        )

        css = css_file.read_text(encoding="utf-8")

        values = {

            "CSS": css,

            "FRAMEWORK_NAME": framework.get("name"),

            "FRAMEWORK_VERSION": framework.get("version"),

            "APPLICATION_NAME": application.get("name"),

            "EXECUTION_MODE": execution.get("mode").title(),

            "GENERATED_DATE": datetime.now().strftime("%d-%b-%Y %H:%M"),

            "TOTAL_QUESTIONS": summary.total_questions,

            "PASS_COUNT": summary.pass_count,

            "REVIEW_COUNT": summary.review_count,

            "FAIL_COUNT": summary.fail_count,

            "OVERALL_SCORE": summary.overall_score,

            "QUALITY_RATING": summary.quality_rating,

            "AVERAGE_CONFIDENCE": summary.average_confidence,

            "AVERAGE_LATENCY": summary.average_latency,

            "ASSESSMENT": self._assessment(summary),

            "STRENGTHS": self._strengths(summary),

            "IMPROVEMENTS": self._improvements(summary),

            "RECOMMENDATIONS": self._recommendations(summary)

        }

        TemplateEngine.render(
            template_file,
            output_file,
            values
        )

    def _assessment(self, summary):

        score = summary.overall_score

        if score >= 95:
            return (
                "The evaluated AI application demonstrates excellent "
                "quality and is suitable for enterprise production deployment."
            )

        elif score >= 85:
            return (
                "The evaluated AI application demonstrates good overall "
                "quality with only minor improvement opportunities."
            )

        elif score >= 70:
            return (
                "The evaluated AI application provides acceptable quality "
                "but requires additional improvements before deployment."
            )

        return (
            "The evaluated AI application requires significant improvements "
            "before production deployment."
        )

    def _strengths(self, summary):

        strengths = []

        if summary.average_confidence >= 90:
            strengths.append("<li>High response confidence.</li>")

        if summary.average_latency <= 500:
            strengths.append("<li>Good response latency.</li>")

        if summary.pass_count >= summary.total_questions * 0.70:
            strengths.append("<li>Strong PASS percentage.</li>")

        strengths.append("<li>Configuration-driven evaluation framework.</li>")

        return "".join(strengths)

    def _improvements(self, summary):

        improvements = []

        if summary.review_count > 0:
            improvements.append(
                "<li>Review medium-confidence responses.</li>"
            )

        if summary.fail_count > 0:
            improvements.append(
                "<li>Improve failed evaluation scenarios.</li>"
            )

        improvements.append(
            "<li>Expand the Golden Dataset with more edge cases.</li>"
        )

        return "".join(improvements)

    def _recommendations(self, summary):

        recommendations = []

        if summary.overall_score >= 85:

            recommendations.append(
                "<li>Recommended for User Acceptance Testing.</li>"
            )

        else:

            recommendations.append(
                "<li>Improve evaluation quality before UAT.</li>"
            )

        recommendations.append(
            "<li>Continue monitoring evaluation metrics.</li>"
        )

        recommendations.append(
            "<li>Re-run evaluation after knowledge base updates.</li>"
        )

        return "".join(recommendations)