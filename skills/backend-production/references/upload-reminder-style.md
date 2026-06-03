# Upload Reminder Style

Use green upload reminders when a prompt needs reference images.

## Standard Chinese Reminder

```html
<span style="color:#15803d;font-weight:600;">上传提醒：@图片1 = A01 / 角色资产；@图片2 = A03 / 场景资产；@图片3 = A05 / 道具资产；@图片4 = S01_CLEAN_STORYBOARD_CONTROL / 4x2 干净故事板。此提醒不属于提示词。</span>
```

## Standard English Reminder

```html
<span style="color:#15803d;font-weight:600;">Upload reminder: @image1 = A01 / character asset; @image2 = A03 / scene asset; @image3 = A05 / prop asset; @image4 = S01_CLEAN_STORYBOARD_CONTROL / 4x2 clean storyboard. This reminder is not part of the prompt.</span>
```

## Rules

- Put reminders outside prompt code blocks.
- Never copy reminders into Image2 or Seedance prompts.
- Always specify `@image number = asset code / purpose`.
- If upload order changes, update the reminder and the Seedance reference map together.

