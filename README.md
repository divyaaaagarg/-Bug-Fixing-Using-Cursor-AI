# Bug Fixing Using Cursor AI

A small debugging case study showing a deliberately faulty Python program and a corrected version. The example is suitable for documenting an AI-assisted debugging workflow in Cursor.

## Files
- `buggy_code.py` — contains a common off-by-one and empty-list bug.
- `fixed_code.py` — corrected implementation with validation.
- `BUG_REPORT.md` — explains the symptoms, root cause, and fix.

## Technologies
- Python 3
- Cursor AI (workflow/documentation tool; code can also run in any Python environment)

## Run locally
```bash
python buggy_code.py
python fixed_code.py
```
The buggy version is included only to demonstrate the defect. Use `fixed_code.py` for the corrected behaviour.

## What was fixed?
The original code attempted to calculate an average by dividing by the number of items without checking whether the list was empty. It also used an incorrect loop boundary in a separate total calculation. The corrected version validates input and uses Python's built-in `sum()`.

## AI-assisted workflow to describe honestly
1. Open the project in Cursor.
2. Ask the assistant to explain the failing behaviour and identify the edge cases.
3. Review the proposed change rather than accepting it blindly.
4. Run the program and verify normal and edge-case inputs.
5. Record the actual prompts and results you personally used before submitting.
