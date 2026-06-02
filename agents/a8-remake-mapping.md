# A8 Remake Mapping Agent

## Responsibility

Map the extracted method DNA into a new original production plan.

## Inputs

Preservation/variation map, user-selected direction, asset matrix, target branch.

## Outputs

`new_production_mapping`, `segment_plan`, `storyboard_plan`, branch-specific production plan.

## Pass Criteria

- Every shot or segment has in-state, action, and out-state.
- Storyboard panel count matches the actual shot count; more than 10 shots are split into multiple boards.
- B-line longform plans split the film into 4-15 second segments, each with `in_state / action_chain / out_state / continuity_to_next`.
- A-line prompts bind user assets; B-line prompts bind asset identity plus clean storyboard narrative control; C-line prompts use compact text anchors.
