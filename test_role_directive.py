from prompt_patterns import RoleDirective

def test_role_directive():
    pattern = RoleDirective()
    task = "Summarize the case view for the advocate dashboard."
    context = {
        "case_id": "A12345",
        "user": "Advocate",
        "role": "Support Advocate",
        "case_summary": "Customer reported a failed transaction. Investigation showed a network error. Refund processed."
    }
    prompt = pattern.apply(task, context)
    print("Generated Prompt:\n", prompt)

if __name__ == "__main__":
    test_role_directive() 