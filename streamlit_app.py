import streamlit as st
import sys
import os
import shutil

# Add the Assignment2/BE directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'Assignment2', 'BE'))

from python_repo_mapper import PythonRepoMapper
from python_code_analyzer import PythonCodeAnalyzer
from python_doc_genie import PythonDocGenie

st.set_page_config(
    page_title="Codebase Genius",
    page_icon="📚", 
    layout="wide"
)

def main():
    st.title("📚 Codebase Genius")
    st.markdown("""
    **Automatically generate documentation for any GitHub repository**
    
    This AI-powered system analyzes codebases and creates comprehensive documentation.
    """)
    
    # Repository input
    col1, col2 = st.columns([2, 1])
    
    with col1:
        github_url = st.text_input(
            "GitHub Repository URL",
            placeholder="https://github.com/username/repository",
            help="Enter the full URL of a public GitHub repository"
        )
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        analyze_btn = st.button("🚀 Generate Documentation", type="primary")
    
    # Example repositories
    st.markdown("### Try these examples:")
    example_cols = st.columns(3)
    
    examples = [
        ("Jac Language", "https://github.com/jaseci-labs/jac"),
        ("Flask Tutorial", "https://github.com/microsoft/python-sample-vscode-flask-tutorial"),
        ("Simple Python", "https://github.com/jakevdp/simple-python-example")
    ]
    
    for i, (name, url) in enumerate(examples):
        with example_cols[i]:
            if st.button(f"📁 {name}", key=f"example_{i}"):
                st.session_state.github_url = url
                st.rerun()
    
    # Set URL from example buttons
    if 'github_url' in st.session_state:
        github_url = st.session_state.github_url
        st.text_input("GitHub Repository URL", value=github_url, key="url_display")
    
    # Analysis section
    if analyze_btn and github_url:
        if not github_url.startswith('https://github.com/'):
            st.error("❌ Please enter a valid GitHub URL starting with 'https://github.com/'")
        else:
            with st.spinner("🔍 Analyzing repository and generating documentation... This may take a few minutes."):
                try:
                    # Initialize components
                    mapper = PythonRepoMapper()
                    analyzer = PythonCodeAnalyzer()
                    doc_genie = PythonDocGenie()
                    
                    # Step 1: Repository mapping
                    st.info("📥 Cloning repository...")
                    repo_data = mapper.run(github_url)
                    
                    if repo_data['status'] == 'error':
                        st.error(f"❌ Repository error: {repo_data.get('error', 'Unknown error')}")
                        return
                    
                    # Step 2: Code analysis
                    st.info("🔍 Analyzing code structure...")
                    code_analysis = analyzer.analyze_directory(repo_data['local_path'])
                    
                    # Step 3: Documentation generation
                    st.info("📝 Generating documentation...")
                    docs_content = doc_genie.generate_markdown(repo_data, code_analysis)
                    
                    # Display results
                    st.success("✅ Documentation generated successfully!")
                    
                    # Summary metrics
                    st.subheader("📊 Analysis Summary")
                    
                    col1, col2, col3, col4 = st.columns(4)
                    
                    with col1:
                        st.metric("Files Analyzed", repo_data['file_tree_count'])
                    
                    with col2:
                        st.metric("Functions Found", code_analysis['functions_found'])
                    
                    with col3:
                        st.metric("Classes Found", code_analysis['classes_found'])
                    
                    with col4:
                        st.metric("Imports Found", code_analysis['imports_found'])
                    
                    # Documentation preview
                    st.subheader("📄 Generated Documentation")
                    
                    with st.expander("View Full Documentation", expanded=True):
                        st.markdown(docs_content)
                    
                    # Download button
                    st.download_button(
                        "💾 Download Documentation",
                        docs_content,
                        file_name=f"{repo_data['repo_name']}_documentation.md",
                        mime="text/markdown"
                    )
                    
                    # Clean up: remove the cloned repository
                    if os.path.exists(repo_data['local_path']):
                        shutil.rmtree(repo_data['local_path'])
                        
                except Exception as e:
                    st.error(f"❌ Analysis failed: {str(e)}")
                    st.info("💡 This might be due to repository size, network issues, or unsupported code structure.")

    # Features section
    if not analyze_btn:
        st.markdown("---")
        st.subheader("✨ Features")
        
        feature_cols = st.columns(3)
        
        with feature_cols[0]:
            st.markdown("""
            **🔍 Code Analysis**
            - Automatic repository cloning
            - File structure mapping
            - Function and class detection
            - Import relationship analysis
            """)
        
        with feature_cols[1]:
            st.markdown("""
            **📚 Documentation**
            - Markdown format
            - Code structure overview
            - Function documentation
            - Class hierarchy
            """)
        
        with feature_cols[2]:
            st.markdown("""
            **🚀 Multi-Language**
            - Python support
            - Jac language support
            - Extensible architecture
            - Customizable templates
            """)

if __name__ == "__main__":
    main()
