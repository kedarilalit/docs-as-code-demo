import ast

with open("src/calculator.py", "r") as file:
    code = file.read()

tree = ast.parse(code)

for item in tree.body:
    if isinstance(item, ast.FunctionDef):
        function_name = item.name
        documentation = ast.get_docstring(item)

        lines = documentation.splitlines()

        description = lines[0]

        parameters = []
        returns = []

        section = None

        for line in lines[1:]:
            line = line.strip()

            if line == "Parameters:":
                section = "parameters"
                continue

            if line == "Returns:":
                section = "returns"
                continue

            if section == "parameters" and line:
                parameters.append(line)

            elif section == "returns" and line:
                returns.append(line)

        with open("docs/calculator.md", "w") as doc_file:
            doc_file.write(f"# {function_name}\n\n")
            doc_file.write(f"{description}\n\n")

            doc_file.write("## Parameters\n\n")

            for parameter in parameters:
                name, description = parameter.split(":", 1)
                doc_file.write(f"- `{name}` - {description.strip()}\n")

            doc_file.write("\n## Returns\n\n")

            for return_line in returns:
                doc_file.write(f"{return_line}\n")

        print("Documentation generated successfully.")