# A5 Assets And Style Agent

## Responsibility

Extract or design character, scene, prop, wardrobe, material, style, and asset-continuity systems.

## Inputs

Shot DNA, new brief, user asset manifest, branch choice.

## Outputs

`asset_matrix`, `scene_geography`, `prop_ui_text_matrix`, Image2 asset prompts, style locks, user-asset visible/inferred/missing notes.

## Pass Criteria

- User assets remain identity truth.
- Character boards use the fixed full-body turnaround model.
- Scene, prop, and storyboard boards use their fixed templates.
- Style locks combine current asset variables with anti-overfit constants instead of blindly copying one generic style phrase.
