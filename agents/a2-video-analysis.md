# A2 Video Analysis Agent

## Responsibility

Turn reference media into verifiable evidence: duration, aspect, frames, cuts, motion, audio rhythm, and initial shot ledger.

## Inputs

Reference video/link/screenshots, optional audio notes, target clip range.

## Outputs

`media_probe`, `frame_sampling_plan`, `frame_observations`, `multimodal_sync`, `shot_count_estimate`, initial `shot_ledger`.

For Branch B longform work, also output:

- `whole_film_structure`: opening, setup, development, turning point, climax, ending image.
- `segment_table`: 4-15 second production segments based on story function, not mechanical time slicing.
- `cross_segment_continuity_targets`: character, scene, prop, style, sound, and edit continuity that must persist across segments.

## Pass Criteria

- Every shot candidate has timecode, duration, and evidence.
- For clips under 15 seconds, contact sheets do not replace state-change verification.
- Cut points, camera movement, and major visual changes are explicit.
- For Branch B longform, whole-film structure and segment table are complete before asset/storyboard planning begins.
