# str_replace_editor Module Documentation

The `str_replace_editor` module provides a comprehensive file editing tool that enables agents to view, create, and modify files within the CodeWiki system. This module is a critical component of the agent toolset, allowing for persistent file operations across command calls.

## Overview

The `str_replace_editor` module implements a filesystem editor tool that allows agents to perform various file operations including viewing file contents, creating new files, replacing text within files, inserting text at specific lines, and undoing edits. The module includes intelligent features like window expansion to show complete functions/classes and file mapping for large Python files.

## Architecture

```mermaid
graph TB
    subgraph "Agent Tools Layer"
        A[AgentOrchestrator]
        DT[DocumentationGenerator]
    end

    subgraph "str_replace_editor Module"
        SRE[EditTool]
        FM[Filemap]
        WE[WindowExpander]
        SR[Tool Function]
    end

    subgraph "Dependencies"
        CW[CodeWikiDeps]
        TS[TreeSitter]
        VMD[validate_mermaid_diagrams]
    end

    A --> SRE
    DT --> SRE
    SRE --> FM
    SRE --> WE
    SRE --> CW
    FM --> TS
    SR --> SRE
    SR --> VMD
```

## Core Components

### EditTool
The main class that implements the file editing functionality. It supports multiple commands:
- `view`: Display file contents or directory structure
- `create`: Create new files
- `str_replace`: Replace text within files
- `insert`: Insert text at specific line numbers
- `undo_edit`: Revert the last edit

### Filemap
A utility class that creates file maps for Python files, showing function and class definitions while eliding their contents for better overview of large files.

### WindowExpander
Intelligently expands viewports to include complete functions, classes, or other code blocks rather than using fixed line windows.

## Dependencies

The `str_replace_editor` module depends on several other modules:

- [CodeWikiDeps](deps.md) - Provides dependency injection for the tool
- [validate_mermaid_diagrams](utils.md) - Validates Mermaid diagrams in documentation files
- TreeSitter libraries - Used for parsing Python code in the Filemap functionality

## Data Flow

```mermaid
sequenceDiagram
    participant A as Agent
    participant S as str_replace_editor
    participant F as File System
    participant R as Registry

    A->>S: Execute command (view/create/str_replace/insert/undo_edit)
    S->>R: Check file history
    S->>F: Read/Write file operations
    F-->>S: File content
    S->>S: Process content (expand windows, validate, etc.)
    S-->>A: Return results with line numbers and context
```

## Component Interactions

```mermaid
graph LR
    subgraph "Input Processing"
        CMD[Command Parser]
        VAL[Path Validator]
    end

    subgraph "File Operations"
        READ[File Reader]
        WRITE[File Writer]
        HIST[History Manager]
    end

    subgraph "Content Processing"
        EXP[Window Expander]
        MAP[File Mapper]
        LINT[Linter]
    end

    subgraph "Output Generation"
        OUT[Output Formatter]
        TRUNC[Truncator]
    end

    CMD --> VAL
    VAL --> READ
    READ --> EXP
    READ --> MAP
    EXP --> LINT
    MAP --> LINT
    LINT --> OUT
    OUT --> TRUNC
    READ --> HIST
    WRITE --> HIST
```

## Key Features

### File Operations
- **View**: Display file contents with line numbers or directory structure
- **Create**: Create new files with specified content
- **String Replace**: Replace specific text patterns with new content
- **Insert**: Insert text at specific line numbers
- **Undo Edit**: Revert the last edit operation

### Intelligent Display
- **Window Expansion**: Automatically expands viewports to show complete functions/classes
- **File Mapping**: Provides an overview of Python files with elided function bodies
- **Content Truncation**: Handles large files by truncating content with clear indicators

### Validation and Safety
- **Path Validation**: Ensures paths are valid and exist before operations
- **Linter Integration**: Validates Python code after edits
- **History Tracking**: Maintains edit history for undo functionality
- **Duplicate Prevention**: Prevents duplicate operations and invalid replacements

## Process Flow

```mermaid
flowchart TD
    START([Start]) --> VALIDATE{Validate Command}
    VALIDATE --> |Invalid| ERROR[Log Error]
    VALIDATE --> |Valid| PATH_CHECK{Check Path}
    PATH_CHECK --> |Invalid| ERROR
    PATH_CHECK --> |Valid| COMMAND{Process Command}
    
    COMMAND --> |view| VIEW_PROC[View Processing]
    COMMAND --> |create| CREATE_PROC[Create Processing]
    COMMAND --> |str_replace| REPLACE_PROC[Replace Processing]
    COMMAND --> |insert| INSERT_PROC[Insert Processing]
    COMMAND --> |undo_edit| UNDO_PROC[Undo Processing]
    
    VIEW_PROC --> WINDOW[Window Expansion]
    CREATE_PROC --> WRITE_FILE[Write File]
    REPLACE_PROC --> LINT_CHECK[Run Linter]
    INSERT_PROC --> SNIPPET[Create Snippet]
    UNDO_PROC --> RESTORE[Restore from History]
    
    WINDOW --> OUTPUT[Generate Output]
    WRITE_FILE --> HISTORY[Update History]
    LINT_CHECK --> OUTPUT
    SNIPPET --> OUTPUT
    RESTORE --> OUTPUT
    
    HISTORY --> OUTPUT
    OUTPUT --> RETURN[Return Result]
    ERROR --> RETURN
    RETURN --> END([End])
```

## Configuration Options

The module includes several configuration constants:
- `MAX_RESPONSE_LEN`: Maximum length of response before truncation (default: 16000)
- `MAX_WINDOW_EXPANSION_VIEW`: Maximum lines to expand when viewing (default: 0)
- `MAX_WINDOW_EXPANSION_EDIT_CONFIRM`: Maximum lines to expand for edit confirmation (default: 0)
- `USE_FILEMAP`: Whether to use file mapping for large Python files (default: False)
- `USE_LINTER`: Whether to run linter on Python files (default: False)

## Error Handling

The module implements comprehensive error handling:
- Unicode decode errors are handled with multiple encoding attempts
- Path validation prevents invalid file operations
- Duplicate text replacements are prevented
- Linter warnings are provided for syntax errors
- History tracking allows for safe undo operations

## Integration Points

The `str_replace_editor` module integrates with:
- The [AgentOrchestrator](agent_orchestrator.md) for tool execution
- The [DocumentationGenerator](documentation_generator.md) for documentation file operations
- The [Registry](config_manager.md) for persistent state management
- The [Mermaid validation system](utils.md) for diagram validation in documentation files

## Usage Examples

The tool is typically used through the `str_replace_editor_tool` which provides a standardized interface for agents to perform file operations. The tool maintains state across command calls and provides detailed feedback about operations performed.