---
name: prototype-reconstruction-system
description: Use when the user provides a video clip, short film, link, screenshots, or production assets and wants AIGC reference remake, prototype reconstruction, video DNA deconstruction, Image2 asset/storyboard prompts, or Seedance 2.0 A/B/C branch prompts. The skill performs DNA-level analysis, chooses asset-based, storyboard-controlled, or text-only delivery, and outputs source-free production prompts with QA.
---

# Prototype Reconstruction System

This skill turns a reference video, link, screenshot set, script, or user asset pack into a production-ready AIGC remake package. It is for method reconstruction, not copying: preserve transferable film grammar and rebuild the expression as a new independent piece.

## Architecture

This repository is installed as one Skill, but it runs as one Master Agent coordinating A0-A11 specialist agents. Start with `agents/master-agent.md` for routing, then load only the specialist agent files needed for the user's task.

## Non-Negotiables

- Do backend DNA analysis before production. Do not jump straight to assets, storyboards, or Seedance prompts unless the user explicitly requests a quick C-line direct prompt.
- Final model-facing prompts must be source-free: do not mention reference film, original clip, learning, copying, remake, mother film, or analysis process.
- BGM and subtitles are post-production unless the user explicitly asks to generate them. Dialogue can be designed as spoken performance timing, but no onscreen subtitles by default.
- For 12-15 second clips, preserve the real shot count and state-change chain. A contact sheet is only navigation; verify transformations, hands, props, VFX, reactions, and final payoff.
- If user assets exist, treat them as identity truth. Reference material supplies shot function, camera grammar, action rhythm, and spatial logic, not identity replacement.
- Before handoff, run an omission audit and only proceed when `DNA_SIGNOFF` is true or explicitly mark the remaining uncertainty.

## Core Workflow

1. Intake the user's goal and available inputs.
   - Identify whether the user wants to preserve style, story, scene, role archetype, dialogue function, camera rhythm, VFX mechanism, sound design, or only one of these layers.
   - If the user asks for options, give at least three reconstruction directions before production.
   - If the user says "直接输出提示词" with no assets/storyboard, use C line.

2. Analyze the reference media.
   - Probe duration, aspect ratio, shot count, cut points, camera movement, composition center, action direction, performance, wardrobe/state shifts, VFX stages, sound effects, dialogue/VO function, captions, and final payoff.
   - Build a shot ledger and state ledger. For short clips, use frame-by-frame or state-change-by-state-change verification.
   - Classify whether the clip is isolated or part of a repeated mother structure.

3. Separate invariants and variables.
   - Invariants: shot rhythm, camera method, emotional curve, reveal logic, action causality, VFX mechanism, sound rhythm, final image function.
   - Variables: identity, face, costume, exact dialogue wording, brand/IP signs, specific scene, music, captions, props that are protected or not provided by the user.
   - Convert variables into new original design choices.

4. Choose the delivery branch.
   - A line: asset-based direct Seedance. Use when user assets, character consistency, products, props, or brand identity matter most.
   - B line: clean black-and-white storyboard/control-frame guided Seedance. Use when shot order, cut rhythm, composition, and motion direction matter most.
   - C line: text-only direct Seedance. Use when no assets/storyboard are available and the user needs fast prompt validation.

5. Produce deliverables.
   - Full package: asset prompts, storyboard/control-frame prompts when needed, Seedance prompts, sound/VFX notes, and QA checklist.
   - A line: bind assets explicitly by ID and module label, such as `A01 / M03 FACE CLOSE-UP`, `S01 / V04 CAMERA A`, `P01 / P06 HAND LOGIC`.
   - B line: state which clean storyboard grid is provided and keep this control sentence: "将提供的 [storyboard image / grid] 制作成一段流畅的电影级动画视频。严格保持 SH01-SH08 的镜头顺序、切点节奏、构图重心、动作方向和镜头连贯性。不要渲染故事板边框、编号、箭头、文字标注或面板布局。故事板只作为运动、构图、镜头切点和动作方向参考，最终必须是一条连续成片。"
   - C line: keep prompt compact, causal, and source-free. Do not include asset-reference syntax or storyboard negatives.

6. Validate before handoff.
   - Check no source/reference process language leaks into model prompts.
   - Check shot count, transformation/state change, dialogue timing, hand/body action, VFX mechanism, and final payoff are present.
   - Check A-line prompts do not let storyboard identity override user assets.
   - Check B-line prompts exclude arrows, labels, frame numbers, text, watermarks, UI, subtitles, logos, and storyboard panel layout.
   - Check C-line prompt stays within any requested character limit and does not carry irrelevant A/B-line baggage.

## Reference Files To Load As Needed

- For full remake intake and scope gates, read `docs/remake-reconstruction-protocol.md`.
- For forensic DNA and omission audit, read `docs/dna-forensic-audit-system.md`.
- For A/B/C branch selection and prompt rules, read `docs/global-three-branch-remake-system.md`.
- For Seedance branch handoff wording, read `docs/seedance-two-branch-delivery-protocol.md`.
- For portrait overfit and style-lock control, read `docs/image2-live-action-portrait-overfit-control.md`.
- For ready-to-copy master prompts, read `templates/remake-master-agent-prompt-v1.md` and `templates/seedance-reference-prompt-template-v1.md`.
- For asset/storyboard board layouts, read only the relevant file in `templates/`.
- For internal multi-agent routing, read `agents/master-agent.md`; then load the relevant A0-A11 specialist file.
- If editing this repository, run `python3 scripts/check_project.py` before finishing.

## Output Defaults

- If the task is a general remake request: first deliver DNA analysis, variable/invariant map, at least three reconstruction directions, and a recommended A/B/C route.
- If the task is a production request: deliver the selected branch package and include prompt-lint notes.
- If the user has supplied assets: use A line unless they explicitly ask for storyboard control.
- If the user supplies clean storyboard/control frames: use B line only after asset identity and storyboard cleanliness are checked.
- If the user has no assets and asks for one Seedance prompt: use C line and target a single continuous 12-15 second result when feasible.
