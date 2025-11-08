import streamlit as st
import requests
import json

st.set_page_config(page_title="Codebase Genius", page_icon="📚")

st.title("📚 Codebase Genius")
st.markdown("Automatically generate documentation for any GitHub repository")

github_url = st.text_input(
    "GitHub Repository URL",
    placeholder="https://github.com/username/repository"
)

if st.button("Generate Documentation"):
    if github_url:
        with st.spinner("Analyzing repository and generating documentation..."):
            try:
                # Call our Python backend
                response = requests.post(
                    'http://localhost:5000/analyze',
                    json={'github_url': github_url},
                    timeout=300  # 5 minute timeout for large repos
                )
                
                if response.status_code == 200:
                    result = response.json()
                    st.success("Documentation generated successfully!")
                    
                    # Show summary
                    st.subheader("Analysis Summary")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Files", result['summary']['files_analyzed'])
                    with col2:
                        st.metric("Functions", result['summary']['functions_found'])
                    with col3:
                        st.metric("Classes", result['summary']['classes_found'])
                    
                    # Show documentation
                    with st.expander("Generated Documentation"):
                        # Read the generated markdown file
                        try:
                            with open(result['documentation_path'], 'r') as f:
                                docs_content = f.read()
                            st.markdown(docs_content)
                        except:
                            st.info("Documentation preview not available")
                    
                    # Download button
                    with open(result['documentation_path'], 'r') as f:
                        st.download_button(
                            "Download Documentation",
                            f.read(),
                            file_name=f"{result['repository']}_documentation.md"
                        )
                else:
                    st.error(f"Error: {response.json().get('error', 'Unknown error')}")
                    
            except Exception as e:
                st.error(f"Connection error: {e}")
    else:
        st.warning("Please enter a GitHub repository URL")
