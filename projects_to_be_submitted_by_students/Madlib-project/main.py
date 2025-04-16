import re
from typing import List, Dict, Optional
import json
import os

class MadLib:
    def __init__(self, template: str, placeholders: Dict[str, str]):
        """Initialize MadLib with a template and placeholder types."""
        self.template = template
        self.placeholders = placeholders
        self.validate_template()

    def validate_template(self) -> None:
        """Validate that all placeholders in template have corresponding types."""
        found_placeholders = set(re.findall(r'\{(\w+)\}', self.template))
        if found_placeholders != set(self.placeholders.keys()):
            raise ValueError("Template placeholders don't match provided types")

    def get_user_input(self, placeholder: str) -> str:
        """Get validated user input for a placeholder."""
        word_type = self.placeholders[placeholder]
        while True:
            try:
                user_input = input(f"Enter a {word_type} for '{placeholder}': ").strip()
                if not user_input:
                    raise ValueError("Input cannot be empty")
                if word_type.lower() == "number":
                    float(user_input)  # Validate number
                elif word_type.lower() == "noun" and not re.match(r'^[a-zA-Z]+$', user_input):
                    raise ValueError("Please enter a valid noun (letters only)")
                return user_input
            except ValueError as e:
                print(f"Error: {e}. Please try again.")

    def generate_story(self) -> str:
        """Generate the completed MadLib story."""
        story = self.template
        for placeholder in self.placeholders:
            user_input = self.get_user_input(placeholder)
            story = story.replace(f"{{{placeholder}}}", user_input)
        return story

class MadLibManager:
    def __init__(self):
        """Initialize MadLibManager with storage for templates."""
        self.templates: List[Dict] = []
        self.load_templates()

    def load_templates(self) -> None:
        """Load templates from a JSON file if it exists."""
        try:
            if os.path.exists("madlib_templates.json"):
                with open("madlib_templates.json", "r") as file:
                    self.templates = json.load(file)
        except json.JSONDecodeError:
            print("Error loading templates. Starting with empty template list.")
            self.templates = []

    def save_templates(self) -> None:
        """Save templates to a JSON file."""
        try:
            with open("madlib_templates.json", "w") as file:
                json.dump(self.templates, file, indent=2)
        except IOError as e:
            print(f"Error saving templates: {e}")

    def add_template(self, template: str, placeholders: Dict[str, str]) -> None:
        """Add a new template to the collection."""
        try:
            madlib = MadLib(template, placeholders)
            self.templates.append({
                "template": template,
                "placeholders": placeholders
            })
            self.save_templates()
            print("Template added successfully!")
        except ValueError as e:
            print(f"Error adding template: {e}")

    def play_madlib(self, template_index: Optional[int] = None) -> None:
        """Play a MadLib game with the specified template index."""
        if not self.templates:
            print("No templates available. Please add a template first.")
            return

        if template_index is None or not (0 <= template_index < len(self.templates)):
            print("\nAvailable templates:")
            for i, template in enumerate(self.templates):
                print(f"{i + 1}. {template['template'][:50]}...")
            while True:
                try:
                    template_index = int(input("Choose a template number: ")) - 1
                    if 0 <= template_index < len(self.templates):
                        break
                    print("Invalid template number.")
                except ValueError:
                    print("Please enter a valid number.")

        template_data = self.templates[template_index]
        madlib = MadLib(template_data["template"], template_data["placeholders"])
        print("\nYour MadLib Story:")
        print(madlib.generate_story())

def main() -> None:
    """Main function to run the MadLib program."""
    manager = MadLibManager()
    
    # Add a sample template
    sample_template = "Once upon a time, a {adjective} {noun} went to {place} to find a {object}."
    sample_placeholders = {
        "adjective": "adjective",
        "noun": "noun",
        "place": "place",
        "object": "noun"
    }
    manager.add_template(sample_template, sample_placeholders)

    while True:
        print("\n=== MadLib Game ===")
        print("1. Play MadLib")
        print("2. Add new template")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        try:
            if choice == "1":
                manager.play_madlib()
            elif choice == "2":
                template = input("Enter the template with {placeholders}: ")
                placeholders = {}
                placeholder_names = re.findall(r'\{(\w+)\}', template)
                for name in placeholder_names:
                    word_type = input(f"Enter word type for '{name}' (e.g., noun, adjective): ")
                    placeholders[name] = word_type
                manager.add_template(template, placeholders)
            elif choice == "3":
                print("Thanks for playing!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()