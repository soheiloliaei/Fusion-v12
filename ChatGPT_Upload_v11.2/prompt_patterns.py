class PromptPattern:
    def __init__(self, name, description, template):
        self.name = name
        self.description = description
        self.template = template

    def apply(self, task: str, context: dict) -> str:
        raise NotImplementedError("Subclasses must implement apply()")

class StepwiseInsightSynthesis(PromptPattern):
    def __init__(self):
        super().__init__(
            name="StepwiseInsightSynthesis",
            description="Decomposes a design/support task into clear, sequential insights, each building on the previous, for explainable agentic reasoning.",
            template=(
                "Task: {task}\n"
                "Context: {context}\n"
                "Instructions:\n"
                "1. Break down the task into logical steps.\n"
                "2. For each step, synthesize a key insight relevant to the support/design goal.\n"
                "3. Present the insights as a numbered list, each with a brief rationale.\n"
                "\n"
                "Stepwise Insights:\n"
                "1. ..."
            )
        )

    def apply(self, task: str, context: dict) -> str:
        context_str = "\n".join(f"{k}: {v}" for k, v in context.items())
        return self.template.format(task=task, context=context_str)

class RoleDirective(PromptPattern):
    def __init__(self):
        super().__init__(
            name="RoleDirective",
            description="Directs the agent to respond strictly from the perspective of a specified role, ensuring outputs match the intended narrative or design authority.",
            template=(
                "Task: {task}\n"
                "Context: {context}\n"
                "Role: {role}\n"
                "Instructions:\n"
                "- Respond ONLY as the specified role.\n"
                "- Use language, priorities, and focus areas appropriate for this role in Block's support/design context.\n"
                "- Summarize or explain as this role would to a peer.\n"
                "\n"
                "Role-based Output:\n"
            )
        )

    def apply(self, task: str, context: dict) -> str:
        role = context.get("role", "Support Design Lead")
        context_str = "\n".join(f"{k}: {v}" for k, v in context.items() if k != "role")
        return self.template.format(task=task, context=context_str, role=role)

class PatternCritiqueThenRewrite(PromptPattern):
    def __init__(self):
        super().__init__(
            name="PatternCritiqueThenRewrite",
            description="First critiques the provided output for clarity, alignment, and completeness, then rewrites it to improve quality and adherence to agentic design standards.",
            template=(
                "Task: {task}\n"
                "Context: {context}\n"
                "Draft Output:\n{draft}\n"
                "Instructions:\n"
                "1. Critique the draft for clarity, alignment with support/design goals, and completeness.\n"
                "2. List specific issues or areas for improvement.\n"
                "3. Rewrite the draft, addressing the critique points, in a clear and concise manner.\n"
                "\n"
                "Critique:\n- ...\n\nRewritten Output:\n"
            )
        )

    def apply(self, task: str, context: dict) -> str:
        draft = context.get("draft", "")
        context_str = "\n".join(f"{k}: {v}" for k, v in context.items() if k != "draft")
        return self.template.format(task=task, context=context_str, draft=draft) 