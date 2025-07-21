from prompt_patterns import PatternCritiqueThenRewrite

def test_pattern_critique_then_rewrite():
    pattern = PatternCritiqueThenRewrite()
    task = "Evaluate and improve the following PRP section."
    context = {
        "draft": "The support agent should try to help the customer as much as possible. If the customer is unhappy, maybe offer a refund.",
        "section": "Refund Policy"
    }
    prompt = pattern.apply(task, context)
    print("Generated Prompt:\n", prompt)

if __name__ == "__main__":
    test_pattern_critique_then_rewrite() 