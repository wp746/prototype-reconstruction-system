# A3 Shot DNA Agent

## Responsibility

Perform shot-by-shot and state-by-state decomposition across visual, camera, performance, VFX, and edit logic.

## Inputs

Initial `shot_ledger`, frame observations, sync timeline, user remake scope.

## Outputs

Completed `shot_ledger`, `state_ledger`, shot function map, omission-risk list.

For Branch B longform work, also output:

- `segment_dna_ledger`: one DNA ledger per selected segment.
- `segment_in_out_state_chain`: how each segment starts, changes, and hands off to the next segment.
- `cross_segment_omission_audit`: missing continuity risks across character, scene, prop, style, sound, and edit rhythm.

## Pass Criteria

- Each shot explains narrative function, emotional function, composition center, camera path, action direction, and cut reason.
- Transformation, hand changes, prop mechanisms, wardrobe/state shifts, reactions, and final payoff are not skipped.
- For Branch B longform, every selected segment passes multidimensional DNA audit before assets, storyboards, or Seedance prompts are produced.
