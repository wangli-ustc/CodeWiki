# Dependency Analyzer Module Overview

## Purpose

The `dependency_analyzer` module is a core component of the CodeWiki system responsible for static code analysis and dependency graph construction. It provides multi-language support for analyzing code repositories, extracting code components (functions, classes, methods), and identifying relationships between them to build comprehensive dependency graphs. This module enables understanding of code structure, call relationships, and dependencies across various programming languages including Python, JavaScript, TypeScript, Java, C#, C/C++, PHP, and DML.

## Architecture

```mermaid
graph TB
    subgraph "Dependency Analyzer Module"
        subgraph "Analysis Service Layer"
            AS[AnalysisService]
            CGA[CallGraphAnalyzer]
            RA[RepoAnalyzer]
        end
        
        subgraph "Language Analyzers"
            PY[PythonASTAnalyzer]
            JS[TreeSitterJSAnalyzer]
            TS[TreeSitterTSAnalyzer]
            JAVA[TreeSitterJavaAnalyzer]
            CS[TreeSitterCSharpAnalyzer]
            CPP[TreeSitterCppAnalyzer]
            C[TreeSitterCAnalyzer]
            PHP[TreeSitterPHPAnalyzer]
            DML[TreeSitterDMLAnalyzer]
            NS[NamespaceResolver]
        end
        
        subgraph "Core Components"
            DP[DependencyParser]
            DGB[DependencyGraphBuilder]
            AST[DependencyParser]
        end
        
        subgraph "Data Models"
            subgraph "Core Models"
                REPO[Repository]
                NODE[Node]
                CALL[CallRelationship]
            end
            subgraph "Analysis Models"
                ANALYSIS[AnalysisResult]
                SELECTION[NodeSelection]
            end
        end
    end
    
    AS --> CGA
    AS --> RA
    CGA --> PY
    CGA --> JS
    CGA --> TS
    CGA --> JAVA
    CGA --> CS
    CGA --> CPP
    CGA --> C
    CGA --> PHP
    CGA --> DML
    PHP --> NS
    
    RA --> AS
    DP --> AS
    AST --> DP
    DGB --> AST
    DGB --> ANALYSIS
    
    AS -.-> NODE
    AS -.-> CALL
    AS -.-> REPO
    ANALYSIS --> REPO
    ANALYSIS --> NODE
    ANALYSIS --> CALL
```

## Core Components Documentation

- **[Analysis Service](dependency_analyzer/analysis_service.md)** - Main orchestrator for repository analysis with support for multiple programming languages
- **[Language Analyzers](dependency_analyzer/language_analyzers.md)** - Collection of language-specific analyzers using tree-sitter and AST parsing
- **[AST Parser](dependency_analyzer/ast_parser.md)** - Core parsing functionality that builds dependency graphs from repository analysis
- **[Dependency Graph Builder](dependency_analyzer/dependency_graph_builder.md)** - Constructs comprehensive dependency graphs and identifies leaf nodes for documentation
- **[Core Models](dependency_analyzer/core_models.md)** - Fundamental data structures (Node, CallRelationship, Repository) for representing code components
- **[Analysis Models](dependency_analyzer/analysis_models.md)** - Data models for analysis results and node selection for partial exports