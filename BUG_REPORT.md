# Bug Report and Fix Notes

## Observed problem
The original `average()` function returned an incorrect average because its loop skipped the last element. For an empty list, it also attempted to divide by zero.

## Root cause
- `range(0, len(numbers) - 1)` does not visit the last index.
- There was no guard against an empty list.

## Resolution
The corrected implementation uses `sum(numbers) / len(numbers)` after checking that the list is not empty. It raises a clear `ValueError` for invalid empty input.

## Verification
- Input `[10, 20, 30, 40]` should return `25.0`.
- Input `[5]` should return `5.0`.
- Input `[]` should raise `ValueError`.

## Academic honesty note
If this project is submitted as work completed with Cursor AI, document the actual Cursor prompts and changes you personally made. Do not claim that an AI tool was used for steps you did not perform.
