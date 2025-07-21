from prompt_patterns import StepwiseInsightSynthesis

def test_stepwise_insight_synthesis():
    pattern = StepwiseInsightSynthesis()
    task = "Analyze the support workflow transcript and extract key process insights."
    context = {
        "transcript": "Customer requests refund. Agent verifies purchase. Agent initiates refund. Customer receives confirmation.",
        "system": "Cash App Support"
    }
    prompt = pattern.apply(task, context)
    print("Generated Prompt:\n", prompt)

if __name__ == "__main__":
    test_stepwise_insight_synthesis() 