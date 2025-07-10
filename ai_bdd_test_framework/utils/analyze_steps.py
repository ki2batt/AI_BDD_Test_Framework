from utils.openai_utils import generate_text

def analyze_steps(file_path):
    """
    Check Behave steps and suggest code for missing ones.
    """
    try:
        with open(file_path, "r") as f: # Try to open the file at the given path in read mode
            steps = f.read() # Read the entire content of the file into the 'steps' variable
    except FileExistsError:
        print(f"Error: File {file_path} not found.")
        return # Exit the function since the file does not exist
    
    environment_context = """
    The automation framework is already set up to initialize Playwright in environment.py.
    This includes setting up the browser, creating a new page, and managing teardown processes.
    Avoid reinitializing Playwright in step definitions as it is redundant.
    You can access the current page using 'context.page'.
    """

    # Create a prompt combining the environment context and the Behave steps
    prompt = f"""
    {environment_context}

    Analyze the following Behave step definitions. 
    For each unimplemented step, 
    provide example Python code to implement it, using Playwright for browser automation.
    Ensure you add assertions to steps which perform validations i.e. steps which contain the following: 'Then I should see'
    
    Behave steps:
    {steps}
    """

    # Generate AI suggestions
    suggestions = generate_text(prompt)
    print("AI suggestions:\n")
    print(suggestions)

#It checks if the script is run directly, then runs the code inside.
if __name__ == "__main__":
    analyze_steps("features/steps/contact_us_form_steps.py")