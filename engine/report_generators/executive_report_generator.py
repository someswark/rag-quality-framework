from pathlib import Path
from datetime import datetime

from utilities.template_engine import TemplateEngine


class ExecutiveReportGenerator:

    def __init__(self, context):

        self.context = context
        self.config_loader = context.get_config_loader()

    def generate(self, summary):

        values = self._build_values(summary)

        template_file = (
            Path(__file__).parent.parent
            / "templates"
            / "executive_report_template.html"
        )

        output_file = (
            Path(__file__).parent.parent.parent
            / "website"
            / "assets"
            / "reports"
            / "executive-report.html"
        )

        TemplateEngine.render(
            template_file,
            output_file,
            values
        )
        
        
        
        
    def _build_values(self, summary):

        framework = self.config_loader.get_framework()

        application = self.config_loader.get_application()

        execution = self.config_loader.get_execution()

        return {

            "CSS": self._load_css(),

            "FRAMEWORK_NAME": framework.get("name"),

            "FRAMEWORK_VERSION": framework.get("version"),

            "APPLICATION_NAME": application.get("name"),

            "EXECUTION_MODE": execution.get("mode").title(),

            "GENERATED_DATE": self._generated_date(),

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
    
    
    def _assessment(self, summary):

        score = summary.overall_score

        if score >= 95:
            return (
                "The evaluated AI application demonstrates excellent overall "
                "quality and is ready for enterprise production deployment. "
                "Overall risk is LOW."
                )

        elif score >= 85:
            return (
            "The evaluated AI application demonstrates good overall "
            "quality with only minor improvement opportunities. "
            "The framework recommends deployment after addressing the "
            "identified REVIEW and FAIL scenarios."
            )

        elif score >= 70:
            return (
            "The evaluated AI application provides acceptable quality "
            "but requires additional improvements before deployment."
            )

        else:
            return (
            "The evaluated AI application requires significant "
            "improvements before production deployment."
            )




        
        
    def _strengths(self, summary):

            strengths = []

            if summary.pass_count >= summary.total_questions * 0.70:
                strengths.append("<li>High percentage of successful evaluations.</li>")

            if summary.average_confidence >= 90:
                strengths.append("<li>High response confidence across evaluated questions.</li>")

            if summary.average_latency <= 500:
                strengths.append("<li>Good response latency for evaluated scenarios.</li>")

            strengths.append("<li>Configuration-driven and reusable evaluation framework.</li>")

            return "".join(strengths)
        
        


    def _improvements(self, summary):

            improvements = []

            if summary.review_count > 0:
                improvements.append(
                    "<li>Review medium-confidence responses to improve answer quality.</li>"
                )

            if summary.fail_count > 0:
                improvements.append(
                    "<li>Investigate failed scenarios and enhance the knowledge base.</li>"
                )

            improvements.append(
                "<li>Expand the Golden Dataset with additional edge-case scenarios.</li>"
            )

            return "".join(improvements)        
        
        


    def _recommendations(self, summary):

            recommendations = []

            if summary.overall_score >= 85:

                recommendations.append(
                    "<li>Recommended for User Acceptance Testing (UAT).</li>"
                )

            else:

                recommendations.append(
                    "<li>Improve evaluation quality before proceeding to UAT.</li>"
                )

            recommendations.append(
                "<li>Continue monitoring confidence and latency metrics.</li>"
            )

            recommendations.append(
                "<li>Re-run the evaluation after knowledge base or prompt updates.</li>"
            )

            return "".join(recommendations)