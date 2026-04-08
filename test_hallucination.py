import pytest
import os
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import HallucinationMetric
from deepeval.models.llms import AnthropicModel # Added this
from dotenv import load_dotenv

load_dotenv()

def test_tissot_hallucination():
    # 1. This is the output Claude gave you in the previous step
    actual_output = "Insert previous Claude response here"

    # 2. These are the facts the grader will use to check for lies
    context = [
        "The Cal 784-2 uses a suspended movement ring with plastic/rubber buffers.",
        "There is no centrifugal adjustment screw on the rotor of the Cal 784-2.",
        "The Tissot 784-2 is an automatic movement.", # This is the truth Claude missed!
        "The Omega Cal 601 is manual; the Tissot 784-2 is automatic."
    ]

    # 3. Tell DeepEval to use Claude-3.5-Sonnet as the JUDGE
    custom_model = AnthropicModel(model="claude-4-6-sonnet-20250219")
    metric = HallucinationMetric(threshold=0.7, model=custom_model)
    
    test_case = LLMTestCase(
        input="Explain the adjustment procedure for the centrifugal escapement buffer on a Tissot PR516 GL Caliber 784-2 to prevent rotor-stall.",
        actual_output=actual_output,
        context=context
    )

    metric.measure(test_case)
    
    # This will print the reason Claude failed or passed in the terminal
    print(f"\nScore: {metric.score}")
    print(f"Reason: {metric.reason}")
    
    assert_test(test_case, [metric])
