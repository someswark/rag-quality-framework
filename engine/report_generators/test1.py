from pathlib import Path


class ExecutiveReportGenerator:

    def __init__(self, context):

        self.context = context

    def generate(self, summary):

        output_path = (
            Path(__file__).parent.parent.parent
            / "website"
            / "assets"
            / "reports"
            / "executive-report.html"
        )

        html = f"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<title>Executive AI Quality Report</title>

{self._get_css()}

</head>

<body>

<div class="container">

{self._build_header()}

{self._build_application(summary)}

</div>

</body>

</html>
"""

        with open(output_path, "w", encoding="utf-8") as file:

            file.write(html)

        print()

        print("✓ Executive Report generated successfully")

    def _build_header(self):

        return """
<div class="header">

<h1>Enterprise AI Quality Framework</h1>

<hr>

</div>
"""

    def _build_application(self, summary):

        return f"""
<div class="section">

<h3>Application Information</h3>

</div>
"""

    def _get_css(self):

        return """
<style>

body{
    font-family: Arial;
}

.container{
    width:90%;
    margin:auto;
}

</style>
"""