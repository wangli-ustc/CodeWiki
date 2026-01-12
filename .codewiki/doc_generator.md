# Documentation Generator CLI Module

## Overview

The `doc_generator` module serves as a CLI adapter for the backend documentation generation system. It wraps the core backend `DocumentationGenerator` and provides CLI-specific functionality including progress tracking, error handling, and logging configuration. This module bridges the gap between the command-line interface and the sophisticated backend documentation generation capabilities.

## Architecture

```mermaid
graph TB
    subgraph "CLI Layer"
        A[CLIDocumentationGenerator]
        B[ProgressTracker]
        C[DocumentationJob]
    end
    
    subgraph "Backend Layer"
        D[DocumentationGenerator]
        E[DependencyAnalyzer]
        F[ClusterModules]
        G[HTMLGenerator]
    end
    
    A --> B
    A --> C
    A --> D
    D --> E
    D --> F
    A --> G
    
    style A fill:#e1f5fe
    style D fill:#f3e5f5
```

## Core Components

### CLIDocumentationGenerator

The main class that orchestrates the documentation generation process. It manages the entire workflow from dependency analysis to final documentation output.

**Key Responsibilities:**
- Initialize and configure the backend documentation generator
- Track progress through multiple generation stages
- Handle CLI-specific configuration and logging
- Manage job lifecycle and statistics

**Initialization Parameters:**
- `repo_path`: Path to the repository to document
- `output_dir`: Directory for generated documentation
- `config`: LLM configuration dictionary
- `verbose`: Enable verbose output mode
- `generate_html`: Flag to generate HTML viewer

## Dependencies

The `doc_generator` module depends on several other modules in the system:

- **[config_manager](config_manager.md)**: For configuration management
- **[progress](progress.md)**: For progress tracking and reporting
- **[job_models](job_models.md)**: For job status and statistics tracking
- **[html_generator](html_generator.md)**: For HTML output generation
- **[dependency_analyzer](dependency_analyzer.md)**: For code analysis and dependency graph building
- **[documentation_generator](documentation_generator.md)**: For core documentation generation capabilities

## Data Flow

```mermaid
sequenceDiagram
    participant CLI as CLIDocumentationGenerator
    participant DA as DependencyAnalyzer
    participant CM as ClusterModules
    participant DG as DocumentationGenerator
    participant HG as HTMLGenerator
    
    CLI->>DG: Initialize with config
    DG->>DA: Build dependency graph
    DA-->>DG: Components and leaf nodes
    DG->>CM: Cluster modules
    CM-->>DG: Module tree
    DG->>DG: Generate documentation
    DG->>HG: Generate HTML (if requested)
    HG-->>CLI: Complete documentation
```

## Process Flow

```mermaid
flowchart TD
    A[Initialize CLIDocumentationGenerator] --> B[Configure Backend Logging]
    B --> C[Start Job Tracking]
    C --> D[Stage 1: Dependency Analysis]
    D --> E[Build Dependency Graph]
    E --> F[Stage 2: Module Clustering]
    F --> G[Cluster Modules with LLM]
    G --> H[Stage 3: Documentation Generation]
    H --> I[Generate Module Documentation]
    I --> J[Stage 4: HTML Generation]
    J --> K[Generate HTML Viewer]
    K --> L[Stage 5: Finalization]
    L --> M[Complete Job]
    
    D --> E2[Parse Source Files]
    E2 --> E3[Analyze Dependencies]
    E3 --> E
    
    F --> G2[Create Module Tree]
    G2 --> G3[Save to JSON]
    G3 --> G
    
    H --> I2[Generate Documentation for Each Module]
    I2 --> I3[Create Repository Overview]
    I3 --> I
    
    J --> K2[Load Module Tree and Metadata]
    K2 --> K3[Generate HTML Output]
    K3 --> K
```

## Key Features

### Progress Tracking
The module provides detailed progress tracking through 5 distinct stages:
1. Dependency Analysis
2. Module Clustering
3. Documentation Generation
4. HTML Generation (optional)
5. Finalization

### Logging Configuration
The module configures backend logging for CLI use with colored output formatting, supporting both verbose and non-verbose modes.

### Error Handling
Comprehensive error handling with job failure tracking and API error propagation.

### HTML Generation
Optional HTML viewer generation for easy documentation browsing.

## Integration Points

The `doc_generator` module integrates with the broader system through:

- **[CLI](cli.md)**: As the main entry point for documentation generation
- **[Backend Services](documentation_generator.md)**: For core documentation capabilities
- **[Configuration System](config.md)**: For managing LLM and generation settings
- **[Progress Tracking](progress.md)**: For user feedback during generation

## Usage Context

This module is typically used when generating documentation from the command line, providing a user-friendly interface to the sophisticated backend documentation generation system while maintaining detailed progress reporting and error handling appropriate for CLI usage.