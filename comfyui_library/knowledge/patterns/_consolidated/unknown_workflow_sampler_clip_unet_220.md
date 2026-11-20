---
name: unknown_workflow_sampler_clip_unet_220
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.833167
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, DualCLIPLoader, KSamplerSelect, ModelSamplingSD3, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Image_capybara_v0_1_image_edit_2027040053440024577.json, 图片生成/图生图/Image_capybara_v0_1_image_edit_fast_2027042674460594177.json, 图片生成/文生图/Image_capybara_v0_1_text_to_image_2026943093957730306.json, 图片生成/文生图/Image_capybara_v0_1_text_to_image_fast_2027038386724278274.json, 视频生成/图生视频/video_capybara_v0_1_image_to_video_2026952696527327234.json, 视频生成/图生视频/video_capybara_v0_1_image_to_video_fast_2027031167693754370.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_220

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Image_capybara_v0_1_image_edit_2027040053440024577.json、图片生成/图生图/Image_capybara_v0_1_image_edit_fast_2027042674460594177.json、图片生成/文生图/Image_capybara_v0_1_text_to_image_2026943093957730306.json、图片生成/文生图/Image_capybara_v0_1_text_to_image_fast_2027038386724278274.json、视频生成/图生视频/video_capybara_v0_1_image_to_video_2026952696527327234.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSamplerSelect`
- `ModelSamplingSD3`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 4/6 个有
- `CLIPVisionLoader` —— 4/6 个有
- `HunyuanVideo15ImageToVideo` —— 4/6 个有
- `LoadImage` —— 4/6 个有
- `SaveImage` —— 4/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `CreateVideo` —— 2/6 个有
- `EmptyHunyuanVideo15Latent` —— 2/6 个有
- `GetImageSize` —— 2/6 个有
- `ImageResizeKJv2` —— 2/6 个有
- `PrimitiveInt` —— 2/6 个有
- `ResizeAndPadImage` —— 2/6 个有
- `ResizeImageMaskNode` —— 2/6 个有
- `SaveVideo` —— 2/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
