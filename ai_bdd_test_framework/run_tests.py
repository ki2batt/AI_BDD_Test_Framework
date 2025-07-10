from utils.openai_utils import generate_text, load_prompt

def generate_scenarios():
    prompt = load_prompt("contact_us_form")

    scenarios = generate_text(prompt)
    print("Generated Gherkin Scenarios:\n", scenarios)

    feature_file_path = "features/contact_form.feature"

    try:
        with open(feature_file_path, "x") as f:
          f.write(scenarios)
          print(f"Scenarios saved to {feature_file_path}")
    except FileExistsError:
        print(f"{feature_file_path} already exists. Skipping overwrite...")   
      

if __name__ == "__main__":
    generate_scenarios()