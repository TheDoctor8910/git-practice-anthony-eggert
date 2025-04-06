# Static and Dynamic Code Analysis Report

## Static Analysis


**flake8**:
- line 1: 'math' imported but unused
- line 2: 'random' imported but unused
- line 28: local variable 'output' is assigned to but never used

**pylint**:
- line 1: missing module docstring
- line 5: missing function or method docstring
- line 12: missing function or method docstring
- line 19: missing function or method docstring
- line 26: missing function or method docstring
- line 28: unused variable 'output'
- line 1: unused import math
- line 2: unused import random

## Line Profiler

Bottleneck found in:

- 'expensive_op': took ~1.12 seconds for 1000 calls

### Fix:
- Replaced loop with arithmetic function - Significant speedup
- Also tested with lru_cache - slight further speedup

## Code Coverage

- Coverage before: 85%
- Coverage after: 100%
- 'unused_function' was not covered, removed

## Fix Summary
- Replaced expensive loop in expensive_op with arithmetic function and added lru caching
- Removed unused_function
- Removed unused variable receiving slow_func output
- Removed unused imports