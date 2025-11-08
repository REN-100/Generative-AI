import json
from datetime import datetime
import os

class PythonDocGenie:
    def __init__(self):
        self.documentation = ""
    
    def generate_markdown(self, repo_data, code_analysis):
        """Generate markdown documentation"""
        print(">>> Generating documentation...")
        
        # Build the documentation step by step to avoid f-string issues
        doc_lines = []
        
        doc_lines.append(f"# {repo_data['repo_name']} - Documentation")
        doc_lines.append("")
        doc_lines.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        doc_lines.append("")
        doc_lines.append("## Repository Overview")
        doc_lines.append(f"- **Repository**: {repo_data['repo_name']}")
        doc_lines.append(f"- **Total Files**: {repo_data['file_tree_count']}")
        doc_lines.append(f"- **README Summary**: {repo_data['readme_summary']}")
        doc_lines.append("")
        doc_lines.append("## Code Analysis Summary")
        doc_lines.append(f"- **Functions Found**: {code_analysis['functions_found']}")
        doc_lines.append(f"- **Classes Found**: {code_analysis['classes_found']}")
        doc_lines.append(f"- **Unique Imports**: {code_analysis['imports_found']}")
        doc_lines.append("")
        doc_lines.append("## File Structure")
        doc_lines.append("```")
        
        # Add file tree (simplified)
        for item in repo_data['file_tree_sample']:
            indent = "  " * item['path'].count('/')
            doc_lines.append(f"{indent}{item['name']}")
        
        doc_lines.append("```")
        doc_lines.append("")
        doc_lines.append("## Functions")
        
        # Add functions
        for func in code_analysis['functions']:
            doc_lines.append(f"- `{func['name']}` (in {func['file']}, line {func['line']})")
        
        doc_lines.append("")
        doc_lines.append("## Classes")
        
        # Add classes
        for cls in code_analysis['classes']:
            doc_lines.append(f"- `{cls['name']}` (in {cls['file']}, line {cls['line']})")
        
        self.documentation = "\n".join(doc_lines)
        return self.documentation
    
    def save_documentation(self, repo_name):
        """Save documentation to file"""
        output_dir = "../outputs"
        os.makedirs(output_dir, exist_ok=True)
        
        filename = f"{output_dir}/{repo_name}_docs.md"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(self.documentation)
        
        print(f">>> Documentation saved to: {filename}")
        return filename

if __name__ == "__main__":
    # Test with existing data
    # First run the repo mapper to get data
    from python_repo_mapper import PythonRepoMapper
    from python_code_analyzer import PythonCodeAnalyzer
    
    mapper = PythonRepoMapper()
    repo_data = mapper.run("https://github.com/jaseci-labs/jac-demo")
    
    analyzer = PythonCodeAnalyzer()
    code_analysis = analyzer.analyze_directory("./temp_repos/jac-demo")
    
    genie = PythonDocGenie()
    docs = genie.generate_markdown(repo_data, code_analysis)
    genie.save_documentation(repo_data['repo_name'])
    
    print(">>> Documentation generation completed!")