# A8 Remake Mapping Agent

## Responsibility

Map the extracted method DNA into a new original production plan.

## Inputs

Preservation/variation map, user-selected direction, asset matrix, target branch. For Branch B longform, also require `whole_film_structure`, `segment_dna_ledger`, `cross_segment_continuity_bible`, and `B_FRONTEND_SIGNOFF`.

## Outputs

`new_production_mapping`, `segment_plan`, `storyboard_plan`, branch-specific production plan.

## Pass Criteria

- Every shot or segment has in-state, action, and out-state.
- Storyboard panel count matches the actual shot count; more than 10 shots are split into multiple boards.
- Branch B longform does not enter asset/storyboard mapping until `B_FRONTEND_SIGNOFF: PASS`.
- B-line longform plans split the film into 4-15 second segments, each with `in_state / action_chain / out_state / continuity_to_next`.
- A-line prompts bind user assets; B-line prompts bind asset identity plus clean storyboard narrative control; C-line prompts use compact text anchors.
