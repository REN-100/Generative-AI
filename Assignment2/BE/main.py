import json
from python_repo_mapper import PythonRepoMapper
from python_code_analyzer import PythonCodeAnalyzer
from python_doc_genie import PythonDocGenie

class CodebaseGenius:
    def __init__(self):
        self.mapper = PythonRepoMapper()
        self.analyzer = PythonCodeAnalyzer()
        self.doc_genie = PythonDocGenie()
    
    def analyze_repository(self, github_url):
        """Main workflow: clone -> analyze -> generate docs"""
        print(">>> Starting Codebase Genius Analysis...")
        
        # Step 1: Repository Mapping
        print(">>> Step 1: Repository Mapping")
        repo_data = self.mapper.run(github_url)
        if repo_data['status'] == 'error':
            return repo_data
        
        # Step 2: Code Analysis
        print(">>> Step 2: Code Analysis")
        code_analysis = self.analyzer.analyze_directory(repo_data['local_path'])
        
        # Step 3: Documentation Generation
        print(">>> Step 3: Documentation Generation")
        docs = self.doc_genie.generate_markdown(repo_data, code_analysis)
        output_path = self.doc_genie.save_documentation(repo_data['repo_name'])
        
        return {
            "status": "completed",
            "repository": repo_data['repo_name'],
            "documentation_path": output_path,
            "summary": {
                "files_analyzed": repo_data['file_tree_count'],
                "functions_found": code_analysis['functions_found'],
                "classes_found": code_analysis['classes_found'],
                "readme_summary": repo_data['readme_summary']
            }
        }

def main():
    genius = CodebaseGenius()
    
    # Test with a sample repository
    test_url = "https://github.com/jaseci-labs/jac-demo"
    result = genius.analyze_repository(test_url)
    
    print("\n>>> FINAL RESULT:")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()