"""
Test for GitHub Copilot LLM services.

This test demonstrates calling the GitHub Copilot API through LiteLLM.
"""
import os
import sys
from pathlib import Path

# Add the codewiki directory to the path
sys.path.insert(0, str(Path(__file__).parent.parent))

from codewiki.src.be import copilot_llm_services
from codewiki.src.config import Config


def test_call_llm_with_claude():
    """
    Test calling LLM with GPT-4o through GitHub Copilot.
    
    This test sends a simple greeting and requests information about
    what the model can do.
    """
    # Create a test configuration
    # Note: You need to set your GitHub token with Copilot access
    config = Config(
        repo_path=".",
        output_dir="test_output",
        dependency_graph_dir="test_output/dependency_graphs",
        docs_dir="test_output/docs",
        max_depth=2,
        llm_base_url=os.getenv("LLM_BASE_URL", ""),  # Optional custom endpoint
        llm_api_key=os.getenv("GITHUB_TOKEN", ""),  # GitHub token
        main_model="gpt-4o",
        cluster_model="gpt-4o",
        fallback_model="gpt-4o-mini"
    )
    
    # Check if API key is configured
    if not config.llm_api_key:
        print("Error: GITHUB_TOKEN environment variable not set")
        print("Please set your GitHub token with Copilot access:")
        print("  export GITHUB_TOKEN='your-github-token'")
        sys.exit(1)
    
    print("Testing GitHub Copilot LLM service...")
    print(f"Model: github_copilot/gpt-4o")
    print(f"Prompt: 'hello, what can you do for me'")
    print("-" * 70)
    
    try:
        # Call the LLM
        response = copilot_llm_services.call_llm(
            prompt="hello, what can you do for me",
            config=config,
            model="github_copilot/claude-sonnet-4.5",
            temperature=0.0
        )
        
        print("\nResponse:")
        print("-" * 70)
        print(response)
        print("-" * 70)
        print("\n✓ Test completed successfully!")
        
    except Exception as e:
        print(f"\n✗ Error calling LLM: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


def test_call_llm_with_default_model():
    """
    Test calling LLM using the default model from config.
    """
    config = Config(
        repo_path=".",
        output_dir="test_output",
        dependency_graph_dir="test_output/dependency_graphs",
        docs_dir="test_output/docs",
        max_depth=2,
        llm_base_url=os.getenv("LLM_BASE_URL", ""),
        llm_api_key=os.getenv("GITHUB_TOKEN", ""),
        main_model="gpt-4o",
        cluster_model="gpt-4o",
        fallback_model="gpt-4o-mini"
    )
    
    if not config.llm_api_key:
        print("Skipping test - GITHUB_TOKEN not set")
        return
    
    print("\n\nTesting with default model from config...")
    print(f"Default model: {config.main_model}")
    print("-" * 70)
    
    try:
        # Call without specifying model (uses config.main_model)
        response = copilot_llm_services.call_llm(
            prompt="What is the capital of France?",
            config=config,
            temperature=0.0
        )
        
        print("\nResponse:")
        print("-" * 70)
        print(response)
        print("-" * 70)
        print("\n✓ Default model test completed successfully!")
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()


def test_get_model_formatting():
    """Test the get_model() helper function."""
    print("\n\nTesting get_model() formatting...")
    print("-" * 70)
    
    test_cases = [
        ("gpt-4o", "github_copilot/gpt-4o"),
        ("gpt-4o-mini", "github_copilot/gpt-4o-mini"),
        ("github_copilot/o1-preview", "github_copilot/o1-preview"),
    ]
    
    for input_model, expected in test_cases:
        result = copilot_llm_services.get_model(input_model)
        status = "✓" if result == expected else "✗"
        print(f"{status} get_model('{input_model}') = '{result}'")
        assert result == expected, f"Expected {expected}, got {result}"
    
    print("-" * 70)
    print("\n✓ Model formatting test completed successfully!")


if __name__ == "__main__":
    print("=" * 70)
    print("GitHub Copilot LLM Services Test Suite")
    print("=" * 70)
    
    # Run tests
    test_get_model_formatting()
    test_call_llm_with_claude()
    test_call_llm_with_default_model()
    
    print("\n" + "=" * 70)
    print("All tests completed!")
    print("=" * 70)
