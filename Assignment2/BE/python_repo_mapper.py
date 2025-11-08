import os
import git
from pathlib import Path
import json

class PythonRepoMapper:
    def __init__(self):
        self.file_tree = []
        self.repo_name = ""
        self.local_path = ""
        self.error = ""
        self.readme_summary = ""
    
    def clone_repository(self, github_url):
        """Clone a GitHub repository"""
        try:
            print(f">>> Cloning repository: {github_url}")
            
            # Extract repo name from URL
            repo_parts = github_url.split("/")
            self.repo_name = repo_parts[-1].replace(".git", "")
            self.local_path = f"./temp_repos/{self.repo_name}"
            
            # Create temp_repos directory if it doesn't exist
            os.makedirs("./temp_repos", exist_ok=True)
            
            # Clone the repository
            repo = git.Repo.clone_from(github_url, self.local_path)
            
            print(f">>> Successfully cloned repository to: {self.local_path}")
            return True
        except Exception as e:
            self.error = f"Clone failed: {e}"
            print(f">>> ERROR: {self.error}")
            return False
    
    def generate_file_tree(self):
        """Generate file tree structure"""
        if not self.local_path:
            self.error = "No local path available - clone first"
            return False
        
        try:
            print(">>> Generating file tree structure...")
            
            for root, dirs, files in os.walk(self.local_path):
                # Skip hidden directories
                dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
                
                # Add directories
                for dir_name in dirs:
                    dir_path = os.path.join(root, dir_name)
                    relative_path = os.path.relpath(dir_path, self.local_path)
                    
                    self.file_tree.append({
                        "name": dir_name,
                        "path": relative_path,
                        "file_type": "directory",
                        "size": 0,
                        "extension": ""
                    })
                
                # Add files
                for file_name in files:
                    file_path = os.path.join(root, file_name)
                    relative_path = os.path.relpath(file_path, self.local_path)
                    
                    file_size = os.path.getsize(file_path)
                    file_ext = os.path.splitext(file_name)[1]
                    
                    self.file_tree.append({
                        "name": file_name,
                        "path": relative_path,
                        "file_type": "file",
                        "size": file_size,
                        "extension": file_ext
                    })
            
            print(f">>> Generated file tree with {len(self.file_tree)} items")
            return True
        except Exception as e:
            self.error = f"File tree generation failed: {e}"
            print(f">>> ERROR: {self.error}")
            return False

    def analyze_readme(self):
        """Find and analyze README files"""
        print(">>> Analyzing README files...")
        
        readme_files = []
        for file_item in self.file_tree:
            if file_item["file_type"] == "file":
                file_lower = file_item["name"].lower()
                if file_lower.startswith("readme"):
                    readme_files.append(file_item)
        
        if readme_files:
            print(f">>> Found {len(readme_files)} README files")
            
            # Read the first README file content
            readme_path = os.path.join(self.local_path, readme_files[0]["path"])
            try:
                with open(readme_path, 'r', encoding='utf-8') as f:
                    readme_content = f.read()
                
                # Simple summary for now - we'll add byLLM later
                self.readme_summary = f"README found with {len(readme_content)} characters. Content preview: {readme_content[:200]}..."
                print(">>> README analysis completed")
                return True
            except Exception as e:
                self.readme_summary = f"Error reading README: {e}"
                return False
        else:
            self.readme_summary = "No README files found"
            print(">>> No README files found")
            return True
    
    def run(self, github_url):
        """Main execution flow"""
        print(f">>> Starting Repo Mapper for: {github_url}")
        
        # Step 1: Clone repository
        if not self.clone_repository(github_url):
            return {"status": "error", "error": self.error}
        
        # Step 2: Generate file tree
        if not self.generate_file_tree():
            return {"status": "error", "error": self.error}
        
        # Step 3: Analyze README
        self.analyze_readme()
        
        # Success
        return {
            "status": "completed",
            "repo_name": self.repo_name,
            "local_path": self.local_path,
            "file_tree_count": len(self.file_tree),
            "readme_summary": self.readme_summary,
            "file_tree_sample": self.file_tree[:10]  # Show first 10 items
        }

# Test the Python version
if __name__ == "__main__":
    mapper = PythonRepoMapper()
    result = mapper.run("https://github.com/jaseci-labs/jac-demo")
    print(">>> RESULT:", json.dumps(result, indent=2))