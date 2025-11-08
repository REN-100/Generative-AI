import os
import ast
import json

class PythonCodeAnalyzer:
    def __init__(self):
        self.functions = []
        self.classes = []
        self.imports = []
    
    def analyze_python_file(self, file_path):
        """Analyze a Python file and extract functions, classes, and imports"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            tree = ast.parse(content)
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    self.functions.append({
                        "name": node.name,
                        "file": os.path.basename(file_path),
                        "line": node.lineno
                    })
                elif isinstance(node, ast.ClassDef):
                    self.classes.append({
                        "name": node.name,
                        "file": os.path.basename(file_path),
                        "line": node.lineno
                    })
                elif isinstance(node, ast.Import):
                    for alias in node.names:
                        self.imports.append(alias.name)
            
            return True
        except Exception as e:
            print(f">>> Error analyzing {file_path}: {e}")
            return False
    
    def analyze_directory(self, directory_path):
        """Analyze all Python files in a directory"""
        print(f">>> Analyzing Python files in: {directory_path}")
        
        python_files = []
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith('.py'):
                    python_files.append(os.path.join(root, file))
        
        print(f">>> Found {len(python_files)} Python files")
        
        for py_file in python_files[:5]:  # Analyze first 5 files for now
            self.analyze_python_file(py_file)
        
        return {
            "functions_found": len(self.functions),
            "classes_found": len(self.classes),
            "imports_found": len(self.imports),
            "functions": self.functions[:10],  # Sample
            "classes": self.classes[:10],      # Sample
            "imports": list(set(self.imports))[:10]  # Unique imports sample
        }

if __name__ == "__main__":
    analyzer = PythonCodeAnalyzer()
    result = analyzer.analyze_directory("./temp_repos/jac-demo")
    print(">>> CODE ANALYSIS RESULT:", json.dumps(result, indent=2))