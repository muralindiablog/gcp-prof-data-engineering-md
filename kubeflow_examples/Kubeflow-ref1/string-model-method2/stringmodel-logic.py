from typing import NamedTuple

class ProcessingResults(NamedTuple):
    """
    Standardized output schema for the string processing logic.
    """
    combined: str
    reversed: str
    uppercased: str

def run(a: str = "Hello", b: str = "World") -> ProcessingResults:
    """
    Executes core string transformations (Concat -> Reverse -> Upper).
    
    Args:
        a: The first input string prefix.
        b: The second input string suffix.
        
    Returns:
        ProcessingResults: A NamedTuple containing the three transformation stages.
    """
    # Core Logic
    combined_val = a + b
    reversed_val = combined_val[::-1]
    uppercased_val = combined_val.upper()
    
    return ProcessingResults(
        combined=combined_val,
        reversed=reversed_val,
        uppercased=uppercased_val
    )

def main():
    # Local execution for verification
    results = run("Data", "Science")
    
    print(f"Combined Stage:  {results.combined}")
    print(f"Reversed Stage:  {results.reversed}")
    print(f"Uppercased Stage: {results.uppercased}")
    print(f"Full Data Bundle: {results}")

if __name__ == "__main__":
    main()
