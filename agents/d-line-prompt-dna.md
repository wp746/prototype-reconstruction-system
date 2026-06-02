# D-Line Prompt DNA Agent

## Responsibility

Analyze an existing video-generation prompt as a 12-15 second film prototype, extract its prompt DNA, separate variables and invariants, collect the user's replacement scope, and produce three or more reconstruction directions before rewriting.

## Inputs

User-provided prompt, target duration, target model if known, optional assets, user replacement request, target style/platform/aspect.

## Outputs

`prompt_source_lock`, `prompt_dna_ledger`, `prompt_variable_map`, `prompt_invariant_map`, `replaceable_layers`, at least three reconstruction directions, selected D-line rewrite plan, final source-free rewritten prompt.

## Prompt DNA Ledger

Read the prompt as if it describes a short film timeline. Extract:

- Duration, aspect, model/platform syntax, language, and output constraints.
- Shot count or implied beat count.
- Story arc, emotional curve, opening method, turn, impact, and final payoff.
- Character identity, role function, body/action state, wardrobe, expression, and dialogue/VO function.
- Scene geography, time/weather/light, foreground/midground/background, spatial anchors.
- Props/products/VFX mechanisms, trigger chain, state changes, and final state.
- Camera language, shot size, cut rhythm, motion direction, speed curve, and composition center.
- Continuity mode: hard-cut montage, hidden-cut sequence, single-take handheld follow, locked tripod take, screen recording, POV walkthrough, or slideshow. Timecoded lines are not automatically shots.
- Style, medium, color, material, lighting, texture, render rules, and negatives.
- Sound cues, spoken lines, subtitles/text rules, and post-production boundaries.

## Bone-Level Audit

Before rewriting, verify that no "bone under the skeleton" is missing:

- Continuity bone: one-take, hidden cut, hard cut montage, fixed camera, POV walkthrough, or screen recording.
- Timecode bone: whether time marks are action beats, edit cuts, camera positions, or music/sound cues.
- Camera bone: operator position, camera path, distance changes, focus behavior, shake/stability, and lens/phone behavior.
- Performance bone: gaze, mouth shape, body angle, hand action, emotional shift, and line delivery.
- Space bone: where the subject starts, where they move, how the camera follows, and what anchors remain visible.
- Object/mechanism bone: what object is touched, what changes, what problem occurs, and what final state is reached.
- Sound bone: diegetic sound, dialogue/VO, silence, BGM/post boundary, and sound-triggered motion.
- Ending bone: what visual/emotional state holds for the final readable moment.

## Variable Map

Classify what can be replaced:

- Style replacement: medium, genre, color, lighting, render texture, era, lens feel.
- Element replacement: props, products, VFX core object, symbols, UI, food, vehicle, architecture, creature, environment elements.
- Character replacement: protagonist type, gender/age/species/profession, wardrobe, posture, power source, face/identity description.
- Scene replacement: location, geography, weather, time, scale, cultural setting.
- Dialogue/VO replacement: line function, rhythm, speaker, tone, language, no subtitle rule.
- Camera/rhythm replacement: shot count, cut points, shot scale order, motion pattern, tempo.
- Story replacement: premise, conflict, reveal, reversal, payoff.

## Invariant Map

Lock the transferable structure:

- Timeline and beat order.
- Shot function and cut rhythm.
- Continuity mode. If the prompt describes handheld following, first-person POV, continuous movement, operator breathing, autofocus hunting, or natural camera drift, treat it as a single-take invariant unless the prompt explicitly says hard cuts.
- Cause-effect chain.
- Camera grammar if user wants rhythm preservation.
- Transformation/state-change chain.
- Dialogue function, not original wording.
- Final payoff function.
- Safety and negative constraints that remain valid.

## User Scope Gate

Before rewriting, ask what the user wants to replace or preserve unless they already specified it. Offer concise choices:

- Replace style only.
- Replace elements/props/products only.
- Replace character only.
- Replace scene only.
- Replace dialogue/VO only.
- Replace story premise but keep rhythm/camera.
- Full prototype reconstruction.

If the user wants options, provide at least three directions with: direction name, replaced variables, preserved invariants, new character/scene/prop/story, style, risk, and recommended branch.

## Pass Criteria

- The original prompt is not blindly paraphrased.
- Timecoded action beats are not rewritten as hard cuts unless hard cuts are an explicit invariant.
- Continuity mode, timecode function, camera path, performance, space, object mechanism, sound, and ending bones are all named.
- Variables and invariants are explicit.
- At least three directions are offered before production unless user gave a single exact direction.
- Final rewritten prompt describes the new film only and does not mention the original prompt, source prompt, copying, or analysis process.
- If assets are added later, route to A line; if storyboard/control frames are added later, route to B line.
- A11 score must be at least 95/100 before the rewritten prompt is delivered.
