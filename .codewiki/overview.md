# CodeWiki Repository Overview

## Purpose

CodeWiki is an automated documentation generation system that creates comprehensive documentation for code repositories using AI-powered analysis. The system analyzes codebases across multiple programming languages, builds dependency graphs, and generates structured documentation using large language models. It provides both command-line and web-based interfaces for users to generate and view documentation for their software projects.

## Architecture

```mermaid
graph TB
    subgraph "User Interfaces"
        CLI[CLI Interface]
        WEB[Web Interface]
    end
    
    subgraph "Frontend Layer"
        ROUTES[Web Routes]
        WORKER[Background Worker]
        CACHE[Cache Manager]
        GITHUB[GitHub Processor]
    end
    
    subgraph "Backend Core"
        DOCGEN[Documentation Generator]
        AGENT[Agent Orchestrator]
        ANALYZER[Dependency Analyzer]
        TOOLS[Agent Tools]
    end
    
    subgraph "Supporting Modules"
        CONFIG[Configuration]
        UTILS[Utilities]
        MODELS[Data Models]
    end
    
    subgraph "Language Support"
        PY[Python Analyzer]
        JS[JavaScript Analyzer]
        TS[TypeScript Analyzer]
        JAVA[Java Analyzer]
        CS[C# Analyzer]
        CPP[C/C++ Analyzer]
        PHP[PHP Analyzer]
        OTHER[Other Languages]
    end
    
    CLI --> CONFIG
    WEB --> ROUTES
    ROUTES --> WORKER
    WORKER --> DOCGEN
    DOCGEN --> AGENT
    DOCGEN --> ANALYZER
    AGENT --> TOOLS
    ANALYZER --> PY
    ANALYZER --> JS
    ANALYZER --> TS
    ANALYZER --> JAVA
    ANALYZER --> CS
    ANALYZER --> CPP
    ANALYZER --> PHP
    ANALYZER --> OTHER
    CONFIG --> ALL[All Modules]
    UTILS --> ALL
    TOOLS --> AGENT
    CACHE --> WORKER
    GITHUB --> WORKER
```

## End-to-End Flow

```mermaid
flowchart TD
    A[User submits repository] --> B{CLI or Web?}
    B -->|CLI| C[CLI Configuration]
    B -->|Web| D[Web Interface]
    C --> E[Load Configuration]
    D --> E
    E --> F[Repository Analysis]
    F --> G[Dependency Graph Building]
    G --> H[Module Clustering]
    H --> I[AI Documentation Generation]
    I --> J[Documentation Output]
    J --> K[HTML Generation]
    K --> L[Documentation Complete]
    
    subgraph "AI Processing"
        M[Agent Orchestrator] --> N[LLM Services]
        N --> O[Documentation Content]
        O --> P[File Generation]
    end
    
    I --> M
    P --> J
```

## Core Modules Documentation

### [CLI Module](cli.md)
Provides command-line interface for documentation generation with configuration management, git integration, and progress tracking.

### [Dependency Analyzer Module](dependency_analyzer.md)
Performs static code analysis across multiple languages to build dependency graphs and identify code relationships.

### [Documentation Generator Module](documentation_generator.md)
Orchestrates the entire documentation generation process using dynamic programming to process modules in dependency order.

### [Agent Orchestrator Module](agent_orchestrator.md)
Manages AI agents that generate documentation for individual modules using LLMs and specialized tools.

### [Agent Tools Module](agent_tools.md)
Provides file system and code analysis tools for AI agents to interact with the codebase during documentation generation.

### [Frontend Module](frontend.md)
Web-based interface for submitting repositories and viewing generated documentation with job management and caching.

### [Configuration Module](config.md)
Manages both persistent user settings and runtime job configurations for the documentation generation system.

### [Utilities Module](utils.md)
Provides essential file operations and utility functions used throughout the CodeWiki system.