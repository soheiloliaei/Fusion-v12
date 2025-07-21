"""
Enhanced agent chain system for Fusion v11.2.
Provides sequential agent execution with pattern application, creative tension, and metrics tracking.
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum

from fusion_v11_agents_complete import Dispatcher, TensionType, apply_creative_tension
from prompt_pattern_registry import get_pattern_by_name
from evaluator_metrics import evaluate_output

@dataclass
class ChainStep:
    """Configuration for a single step in the agent chain."""
    agent: str
    pattern: Optional[str] = None
    tension_type: Optional[str] = None
    metrics_threshold: Optional[float] = 0.7

class ChainMode(Enum):
    """Execution modes for the agent chain."""
    SEQUENTIAL = "sequential"  # Standard sequential execution
    PARALLEL = "parallel"      # Parallel agent execution where possible
    ADAPTIVE = "adaptive"      # Adapts chain based on metrics

def run_agent_chain(
    flow: List[Dict[str, Any]], 
    input_text: str, 
    context: Optional[Dict[str, Any]] = None,
    mode: ChainMode = ChainMode.SEQUENTIAL,
    metrics_threshold: float = 0.7
) -> Dict[str, Any]:
    """
    Run a chain of agents with pattern application, creative tension, and metrics tracking.
    
    Args:
        flow: List of chain steps with agent, pattern, and tension configs
        input_text: Initial input text
        context: Optional context dictionary
        mode: Chain execution mode
        metrics_threshold: Quality threshold for outputs
    
    Returns:
        Dictionary containing chain results, metrics, and insights
    """
    dispatcher = Dispatcher()
    context = context or {}
    results = []
    metrics_history = []
    chain_insights = []

    current_input = input_text
    previous_metrics = None

    for step_config in flow:
        step = ChainStep(**step_config)
        step_result = execute_chain_step(
            dispatcher=dispatcher,
            step=step,
            input_text=current_input,
            context=context,
            previous_metrics=previous_metrics,
            mode=mode
        )

        # Evaluate output quality
        metrics = evaluate_output(
            text=step_result["output"],
            pattern_name=step.pattern if step.pattern else "default",
            context=context
        )

        # Check if output meets quality threshold
        if metrics["overall"] < (step.metrics_threshold or metrics_threshold):
            retry_result = retry_chain_step(
                dispatcher=dispatcher,
                step=step,
                input_text=current_input,
                context=context,
                previous_metrics=metrics
            )
            if retry_result["metrics"]["overall"] > metrics["overall"]:
                step_result = retry_result

        # Record step results
        results.append({
            "step": step_config,
            "input": current_input,
            "output": step_result["output"],
            "metrics": metrics,
            "insights": step_result.get("insights", [])
        })

        # Update for next iteration
        current_input = step_result["output"]
        previous_metrics = metrics
        metrics_history.append(metrics)
        chain_insights.extend(step_result.get("insights", []))

    return {
        "chain_results": results,
        "metrics_history": metrics_history,
        "chain_insights": chain_insights,
        "overall_metrics": calculate_chain_metrics(metrics_history),
        "chain_quality": assess_chain_quality(results, metrics_history)
    }

def execute_chain_step(
    dispatcher: Dispatcher,
    step: ChainStep,
    input_text: str,
    context: Dict[str, Any],
    previous_metrics: Optional[Dict[str, Any]] = None,
    mode: ChainMode = ChainMode.SEQUENTIAL
) -> Dict[str, Any]:
    """Execute a single step in the agent chain."""
    
    # Apply pattern if specified
    if step.pattern:
        pattern = get_pattern_by_name(step.pattern)
        input_text = pattern.apply(input_text, context)

    # Apply creative tension if specified
    if step.tension_type:
        tension_result = apply_creative_tension(
            {"input": input_text},
            step.tension_type,
            context
        )
        input_text = tension_result["balanced_perspective"]

    # Route to agent
    output = dispatcher.execute({
        "agent_name": step.agent,
        "user_input": input_text,
        "context": context
    })["output"]

    # Generate step insights
    insights = generate_step_insights(
        step=step,
        output=output,
        previous_metrics=previous_metrics,
        mode=mode
    )

    return {
        "output": output,
        "insights": insights
    }

def retry_chain_step(
    dispatcher: Dispatcher,
    step: ChainStep,
    input_text: str,
    context: Dict[str, Any],
    previous_metrics: Dict[str, Any]
) -> Dict[str, Any]:
    """Retry a chain step with enhanced context based on previous metrics."""
    
    # Enhance context with metrics insights
    enhanced_context = context.copy()
    enhanced_context.update({
        "previous_metrics": previous_metrics,
        "improvement_areas": [
            k for k, v in previous_metrics.items() 
            if isinstance(v, (int, float)) and v < 0.7
        ],
        "retry_attempt": True
    })

    # Execute with enhanced context
    return execute_chain_step(
        dispatcher=dispatcher,
        step=step,
        input_text=input_text,
        context=enhanced_context,
        previous_metrics=previous_metrics
    )

def generate_step_insights(
    step: ChainStep,
    output: str,
    previous_metrics: Optional[Dict[str, Any]] = None,
    mode: ChainMode = ChainMode.SEQUENTIAL
) -> List[str]:
    """Generate insights for a chain step."""
    insights = []

    # Pattern-specific insights
    if step.pattern:
        insights.append(f"Pattern '{step.pattern}' applied to structure output")

    # Tension-specific insights
    if step.tension_type:
        insights.append(f"Creative tension '{step.tension_type}' used for breakthrough thinking")

    # Metrics-based insights
    if previous_metrics:
        if previous_metrics.get("overall", 0) < 0.7:
            insights.append("Output quality improved from previous step")
        if previous_metrics.get("block_relevance", 0) < 0.7:
            insights.append("Block relevance enhanced in this step")

    # Mode-specific insights
    if mode == ChainMode.ADAPTIVE:
        insights.append("Chain adapted based on metrics feedback")

    return insights

def calculate_chain_metrics(metrics_history: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Calculate overall metrics for the entire chain."""
    if not metrics_history:
        return {}

    # Calculate averages for each metric
    metric_keys = [k for k in metrics_history[0].keys() if isinstance(metrics_history[0][k], (int, float))]
    averages = {}

    for key in metric_keys:
        values = [m[key] for m in metrics_history if key in m]
        averages[key] = sum(values) / len(values) if values else 0

    # Calculate chain-specific metrics
    return {
        "average_metrics": averages,
        "improvement_trend": calculate_improvement_trend(metrics_history),
        "consistency_score": calculate_consistency_score(metrics_history),
        "chain_effectiveness": calculate_chain_effectiveness(metrics_history)
    }

def calculate_improvement_trend(metrics_history: List[Dict[str, Any]]) -> float:
    """Calculate the improvement trend across the chain."""
    if len(metrics_history) < 2:
        return 1.0

    overall_scores = [m.get("overall", 0) for m in metrics_history]
    improvements = [b - a for a, b in zip(overall_scores, overall_scores[1:])]
    
    return sum(improvements) / len(improvements) + 1.0

def calculate_consistency_score(metrics_history: List[Dict[str, Any]]) -> float:
    """Calculate how consistent the quality is across the chain."""
    if not metrics_history:
        return 1.0

    overall_scores = [m.get("overall", 0) for m in metrics_history]
    variance = sum((x - sum(overall_scores) / len(overall_scores)) ** 2 for x in overall_scores) / len(overall_scores)
    
    return 1.0 - min(variance, 1.0)

def calculate_chain_effectiveness(metrics_history: List[Dict[str, Any]]) -> float:
    """Calculate overall chain effectiveness."""
    if not metrics_history:
        return 0.0

    improvement_trend = calculate_improvement_trend(metrics_history)
    consistency_score = calculate_consistency_score(metrics_history)
    final_quality = metrics_history[-1].get("overall", 0)

    return (improvement_trend * 0.3 + consistency_score * 0.3 + final_quality * 0.4)

def assess_chain_quality(
    results: List[Dict[str, Any]], 
    metrics_history: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """Assess the overall quality of the chain execution."""
    
    chain_effectiveness = calculate_chain_effectiveness(metrics_history)
    
    quality_assessment = {
        "score": chain_effectiveness,
        "rating": "excellent" if chain_effectiveness > 0.9 else
                 "good" if chain_effectiveness > 0.8 else
                 "acceptable" if chain_effectiveness > 0.7 else
                 "needs_improvement",
        "strengths": [],
        "improvement_areas": []
    }

    # Analyze strengths
    if calculate_improvement_trend(metrics_history) > 0:
        quality_assessment["strengths"].append("Consistent improvement across chain")
    if calculate_consistency_score(metrics_history) > 0.8:
        quality_assessment["strengths"].append("High output consistency")
    if metrics_history[-1].get("block_relevance", 0) > 0.8:
        quality_assessment["strengths"].append("Strong Block-specific relevance")

    # Analyze improvement areas
    if calculate_consistency_score(metrics_history) < 0.7:
        quality_assessment["improvement_areas"].append("Output consistency could be improved")
    if metrics_history[-1].get("innovation_score", 0) < 0.7:
        quality_assessment["improvement_areas"].append("Innovation level could be enhanced")
    if metrics_history[-1].get("pattern_effectiveness", 0) < 0.7:
        quality_assessment["improvement_areas"].append("Pattern application could be more effective")

    return quality_assessment 