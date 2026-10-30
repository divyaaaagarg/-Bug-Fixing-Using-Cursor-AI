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

## How I used Cursor AI

1. I opened buggy_code.py in Cursor.
2. I asked Cursor: 
3. Cursor pointed out that the average divides by zero for an empty list and that the loop boundary was wrong.
4. I reviewed the suggested change, applied it, and ran the program with normal and empty inputs to confirm the fix.
