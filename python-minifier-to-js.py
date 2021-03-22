import regex as re
def openAndProcessCodeToString(filename):
    with open(filename) as f:
        code = f.read().replace("\\n", "\\\\n").replace("`", "")
    code = re.sub("(import|from) .*", "", code) # Remove all import statements
    return code


code = ""
files = [
    "tokenisation.py",
    "lexer.py",
    "ast.py",
    "astparser.py",
    "semantic_analyser.py",
    "convert_to_python.py",
    "stack.py",
    "interpreter.py",
    "main.py"
    ]
for file in files:
    code += openAndProcessCodeToString("python_src/"+file) + "\n"

code += "\n'Loaded and Ready to go!'"

with open("code-minified.py", "w") as f:
    f.write(code)

with open("newcode.js", "w") as f:
    f.write(f"var InterpreterCode = `{code}`;")
