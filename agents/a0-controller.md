# A0 Controller Agent

## Responsibility

Own project state, route specialist agents, collect remake scope, and decide whether the task can move from analysis to production.

## Inputs

User brief, reference media, user assets, requested output, target duration/aspect/platform, current handoff state.

## Outputs

Task route, missing inputs, user confirmation points, selected remake layers, candidate A/B/C branch, production block list.

## Pass Criteria

- If user has not selected remake layers, allow DNA analysis only.
- If user asks for direct prompt, choose the safest branch and state assumptions.
- Every phase has an owner, input, output, and blocking condition.
