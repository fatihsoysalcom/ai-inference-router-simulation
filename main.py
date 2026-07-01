import time

# Simulate different AI models deployed as serverless functions.
# In a real scenario, these would be API calls to actual AI models
# hosted on a platform like DigitalOcean Serverless Inference.

def code_generator_model(prompt: str) -> str:
    """Simulates an AI model generating code."""
    print(f"[Model: Code Generator] Processing request: '{prompt}'...")
    time.sleep(0.5) # Simulate network latency/processing
    return f"Generated Python code for: '{prompt}'. (e.g., `def {prompt.replace(' ', '_')}(): pass`)"

def bug_fixer_model(prompt: str) -> str:
    """Simulates an AI model fixing bugs."""
    print(f"[Model: Bug Fixer] Processing request: '{prompt}'...")
    time.sleep(0.7)
    return f"Fixed potential bug in code related to: '{prompt}'. (e.g., 'Added try-except block.')"

def code_optimizer_model(prompt: str) -> str:
    """Simulates an AI model optimizing code."""
    print(f"[Model: Code Optimizer] Processing request: '{prompt}'...")
    time.sleep(0.6)
    return f"Optimized code for: '{prompt}'. (e.g., 'Refactored loop for better performance.')"

class InferenceRouter:
    """
    Simulates an Inference Router that dispatches requests to different
    AI models (simulated serverless inference endpoints).
    This is the core concept of routing agent-based coding tasks to
    specific AI capabilities.
    """
    def __init__(self):
        # Map task types to their respective simulated AI model functions.
        # This represents how the router knows which 'serverless' model to call.
        self.models = {
            "code_generation": code_generator_model,
            "bug_fixing": bug_fixer_model,
            "code_optimization": code_optimizer_model,
        }
        print("Inference Router initialized with available models.")

    def route_inference(self, task_type: str, prompt: str) -> str:
        """
        Routes an inference request to the appropriate AI model based on task_type.
        This simulates an AI agent requesting a specific capability from the router.
        """
        if task_type in self.models:
            print(f"\n[Router] Routing '{task_type}' request for prompt: '{prompt}'...")
            model_function = self.models[task_type]
            result = model_function(prompt) # Call the simulated serverless model
            print(f"[Router] Request for '{task_type}' completed.")
            return result
        else:
            return f"Error: Unknown task type '{task_type}'. Available types: {list(self.models.keys())}"

if __name__ == "__main__":
    router = InferenceRouter()

    print("\n--- Simulating AI Agent Requests ---")

    # Simulate an AI agent requesting code generation
    task1_prompt = "create a simple Python function to add two numbers"
    response1 = router.route_inference("code_generation", task1_prompt)
    print(f"Agent received: {response1}")

    # Simulate an AI agent requesting bug fixing
    task2_prompt = "a loop that might cause an off-by-one error"
    response2 = router.route_inference("bug_fixing", task2_prompt)
    print(f"Agent received: {response2}")

    # Simulate an AI agent requesting code optimization
    task3_prompt = "a function with nested loops for matrix multiplication"
    response3 = router.route_inference("code_optimization", task3_prompt)
    print(f"Agent received: {response3}")

    # Simulate an AI agent requesting an unknown task
    task4_prompt = "design a UI layout"
    response4 = router.route_inference("ui_design", task4_prompt)
    print(f"Agent received: {response4}")

    print("\n--- Simulation Complete ---")
