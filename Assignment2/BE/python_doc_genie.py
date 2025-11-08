import json
from datetime import datetime

class PythonDocGenie:
    def __init__(self):
        self.documentation = ""
    
    def generate_markdown(self, repo_data, code_analysis):
        """Generate markdown documentation"""
        print(">>> Generating documentation...")
        
        doc = f"""# {repo_data['repo_name']} - Documentation

Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Repository Overview
- **Repository**: {repo_data['repo_name']}
- **Total Files**: {repo_data['file_tree_count']}
- **README Summary**: {repo_data['readme_summary']}

## Code Analysis Summary
- **Functions Found**: {code_analysis['functions_found']}
- **Classes Found**: {code_analysis['classes_found']}
- **Unique Imports**: {code_analysis['imports_found']}

## File Structure