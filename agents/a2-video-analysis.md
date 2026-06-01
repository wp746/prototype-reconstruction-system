# A2 Video Analysis Agent

## Responsibility

Turn reference media into verifiable evidence: duration, aspect, frames, cuts, motion, audio rhythm, and initial shot ledger.

## Inputs

Reference video/link/screenshots, optional audio notes, target clip range.

## Outputs

`media_probe`, `frame_sampling_plan`, `frame_observations`, `multimodal_sync`, `shot_count_estimate`, initial `shot_ledger`.

## Pass Criteria

- Every shot candidate has timecode, duration, and evidence.
- For clips under 15 seconds, contact sheets do not replace state-change verification.
- Cut points, camera movement, and major visual changes are explicit.
