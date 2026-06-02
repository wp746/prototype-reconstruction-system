# A11 QA Agent

## Responsibility

Run final production QA across DNA coverage, branch fit, prompt lint, continuity, and handoff completeness.

## Inputs

All ledgers, selected branch, final prompts, handoff package.

## Outputs

QA report, score, pass/fail, required fixes, accepted residual risks.

## Pass Criteria

- `DNA_SIGNOFF` passes.
- Shot count, state changes, transformation, hands/body, VFX mechanism, sound cues, dialogue timing, and payoff are represented.
- No source/reference-process language appears in final prompts.
- A-line asset consistency, B-line clean-control rules, C-line compactness rules, or D-line prompt-variable rules pass according to branch.
- Final score is at least 95/100. Anything below 95 is not user-deliverable.

## 95-Point Scoring Gate

Score every production prompt before handoff:

- DNA coverage: 20 points. Story, action, state changes, prop/VFX mechanism, sound, dialogue, edit rhythm, and final payoff are all represented.
- Structure and continuity: 20 points. Shot count or beat count is correct; continuity mode is correct; timecoded beats are not mistaken for hard cuts; motion and blocking are physically coherent.
- Variable/invariant discipline: 15 points. Preserved method and replaced expression are separated; user-selected replacement layers are honored.
- Branch fit: 15 points. A/B/C/D branch rules are followed; no asset/storyboard/text-only/prompt-remake logic is mixed accidentally.
- Prompt execution clarity: 15 points. The model-facing prompt is concise, causal, and source-free, with one main action per beat or shot.
- Failure prevention: 10 points. Negatives target actual risks without irrelevant baggage.
- User intent fit: 5 points. The final output matches the user's requested direction, assets, aspect, platform, and test goal.

If any single category loses more than 5 points, revise even if the total remains above 95.
