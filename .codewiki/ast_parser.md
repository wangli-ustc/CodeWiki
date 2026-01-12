# AST Parser Module Documentation

## Overview

The AST Parser module is a core component of the dependency analyzer system that provides functionality for parsing multi-language repositories and extracting code components. The module leverages the [analysis_service](analysis_service.md) to perform structural and call graph analysis, then builds a comprehensive dependency graph of code components.

The primary class `DependencyParser` serves as the main entry point for repository parsing, creating a mapping of components with their dependencies and metadata. This module is essential for understanding code structure and relationships across different programming languages.

## Architecture

```mermaid
graph TD
    A[DependencyParser] --> B[AnalysisService]
    B --> C[Language Analyzers]
    A --> D[Node Objects]
    D --> E[Repository Model]
    A --> F[Dependency Graph]
    
    C --> G[C Analyzer]
    C --> H[Cpp Analyzer]
    C --> I[Java Analyzer]
    C --> J[Python Analyzer]
    C --> K[JS/TS Analyzers]
    C --> L[Other Language Analyzers]
    
    style A fill:#e1f5fe
    style B fill:#f3e5f5
    style D fill:#e8f5e8
```

## Core Components

### DependencyParser

The `DependencyParser` class is the main component of this module, responsible for:

- Parsing repositories and extracting code components
- Building dependency relationships between components
- Managing component metadata and documentation
- Saving dependency graphs to JSON format

#### Key Methods

- `parse_repository()`: Main entry point that analyzes repository structure and call graphs
- `_build_components_from_analysis()`: Processes analysis results into Node objects
- `save_dependency_graph()`: Exports the dependency graph to JSON format
- `_determine_component_type()`: Identifies the type of code component
- `_file_to_module_path()`: Converts file paths to module paths

## Data Flow

```mermaid
sequenceDiagram
    participant Client
    participant DP as DependencyParser
    participant AS as AnalysisService
    participant LA as Language Analyzers
    participant NM as Node Models
    
    Client->>DP: parse_repository()
    DP->>AS: _analyze_structure()
    AS->>LA: Analyze files by language
    LA-->>AS: File tree structure
    AS->>AS: _analyze_call_graph()
    AS-->>DP: Call graph result
    DP->>NM: Create Node objects
    NM-->>DP: Component nodes with dependencies
    DP-->>Client: Dictionary of components
```

## Component Relationships

```mermaid
graph LR
    subgraph "AST Parser Module"
        DP[DependencyParser]
    end
    
    subgraph "Analysis Service"
        AS[AnalysisService]
    end
    
    subgraph "Language Analyzers"
        LA[Multiple Language Analyzers]
    end
    
    subgraph "Core Models"
        NM[Node Models]
        RM[Repository Model]
    end
    
    subgraph "Output"
        DG[Dependency Graph]
        JSON[JSON Output]
    end
    
    DP --> AS
    AS --> LA
    DP --> NM
    NM --> RM
    DP --> DG
    DG --> JSON
```

## Dependencies

The AST Parser module depends on several other modules:

- **[analysis_service](analysis_service.md)**: Provides structural and call graph analysis capabilities
- **[core_models](core_models.md)**: Defines the Node data structure used to represent code components
- **[language_analyzers](language_analyzers.md)**: Language-specific parsing capabilities through the AnalysisService

## Process Flow

```mermaid
flowchart TD
    A[Initialize DependencyParser] --> B[Call parse_repository]
    B --> C[AnalysisService._analyze_structure]
    C --> D[Get file tree structure]
    D --> E[AnalysisService._analyze_call_graph]
    E --> F[Extract functions and relationships]
    F --> G[Build components from analysis]
    G --> H[Create Node objects]
    H --> I[Map dependencies]
    I --> J[Return component dictionary]
    
    style A fill:#e1f5fe
    style J fill:#e8f5e8
```

## Usage Example

The DependencyParser is typically used as follows:

```python
parser = DependencyParser(repo_path="/path/to/repository")
components = parser.parse_repository()
parser.save_dependency_graph("dependency_graph.json")
```

## Integration Points

The AST Parser module integrates with the broader system through:

1. **[analysis_service](analysis_service.md)**: For performing the actual parsing and analysis
2. **[dependency_graph_builder](dependency_graph_builder.md)**: For constructing the final dependency graph
3. **[cli](cli.md)**: Through the documentation generation workflow
4. **[documentation_generator](documentation_generator.md)**: Providing component information for documentation

## File Extensions Supported

The module supports parsing of multiple programming languages through the underlying language analyzers, including:
- Python (.py)
- JavaScript/TypeScript (.js, .ts, .tsx, .jsx)
- Java (.java)
- C# (.cs)
- C/C++ (.c, .cpp, .h, .hpp)
- PHP (.php)
- And other languages supported by the language analyzers

## Error Handling

The module includes logging capabilities for debugging and error tracking. All operations are logged at the DEBUG level, providing visibility into the parsing process and any issues that may occur during analysis.

## Performance Considerations

The parser processes repositories by:
1. Analyzing repository structure first
2. Performing call graph analysis
3. Building component relationships
4. Creating Node objects with metadata

For large repositories, this process can be time-intensive, but provides comprehensive dependency information.