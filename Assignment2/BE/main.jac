import { repo_mapper } with './agents/repo_mapper.jac';
import { code_analyzer } with './agents/code_analyzer.jac'; 
import { doc_genie } with './agents/doc_genie.jac';

node repository {
    has name;
    has url;
    has local_path;
    has file_tree;
    has readme_summary;
}

walker init {
    root {
        spawn here --> node::repository;
    }
}

walker code_genius_supervisor {
    has input github_url;
    has output documentation = '';
    has output status = 'initialized';
    
    can orchestrate_workflow with code_genius_supervisor entry {
        std.log('🎯 Codebase Genius starting analysis for: ' + input.github_url);
        
        report {
            'status': 'starting_analysis',
            'repository': input.github_url,
            'timestamp': std.time_now()
        };
        
        // Step 1: Repository Mapping
        std.log('📁 Step 1: Repository Mapping');
        spawn here walker::repo_mapper(github_url=input.github_url);
        
        // Step 2: Code Analysis  
        std.log('🔍 Step 2: Code Analysis');
        spawn here walker::code_analyzer(target_files=file_list);
        
        // Step 3: Documentation Generation
        std.log('📝 Step 3: Documentation Generation');
        spawn here walker::doc_genie(
            code_graph=analysis_results,
            file_tree=file_tree,
            readme_summary=readme_summary
        );
        
        report {
            'status': 'completed',
            'documentation': generated_docs,
            'repository': input.github_url,
            'output_path': './outputs/' + repo_name + '/docs.md'
        };
    }
}

// API endpoint walker
walker analyze_repo {
    has input github_url;
    
    with entry {
        spawn here walker::code_genius_supervisor(github_url=input.github_url);
    }
}
