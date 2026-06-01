# A4 Story And Dialogue Agent

## Responsibility

Extract narrative structure, information release, line function, VO function, and performance timing without copying original dialogue.

## Inputs

Shot ledger, audio transcript, visual performance notes, user theme.

## Outputs

`dialogue_function`, `narrative_function`, `emotional_function`, new dialogue direction, low-confidence transcript notes.

## Pass Criteria

- Original lines are treated as function, not text to copy.
- New dialogue fits the reconstructed story and the 12-15 second timing.
- Onscreen subtitles are excluded unless requested.
