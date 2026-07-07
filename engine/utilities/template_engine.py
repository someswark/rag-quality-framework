from pathlib import Path


class TemplateEngine:

    @staticmethod
    def render(template_file, output_file, values):

        # Read template
        template = Path(template_file).read_text(
            encoding="utf-8"
        )

        # Replace placeholders
        for key, value in values.items():

            placeholder = "{{" + key + "}}"

            template = template.replace(
                placeholder,
                str(value)
            )

        # Ensure output folder exists
        output_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        # Write report
        output_file.write_text(
            template,
            encoding="utf-8"
        )

        print(f"✓ Generated: {output_file}")