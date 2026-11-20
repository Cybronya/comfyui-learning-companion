---
name: unknown_workflow_sampler_clip_unet_330
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.84775
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, DualCLIPLoader, KSamplerSelect, ModelSamplingSD3, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Image_capybara_v0_1_image_edit_2027040053440024577.json, 图片生成/图生图/Image_capybara_v0_1_image_edit_fast_2027042674460594177.json, 图片生成/文生图/Image_capybara_v0_1_text_to_image_2026943093957730306.json, 图片生成/文生图/Image_capybara_v0_1_text_to_image_fast_2027038386724278274.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_330

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Image_capybara_v0_1_image_edit_2027040053440024577.json、图片生成/图生图/Image_capybara_v0_1_image_edit_fast_2027042674460594177.json、图片生成/文生图/Image_capybara_v0_1_text_to_image_2026943093957730306.json、图片生成/文生图/Image_capybara_v0_1_text_to_image_fast_2027038386724278274.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSamplerSelect`
- `ModelSamplingSD3`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 2/4 个有
- `CLIPVisionLoader` —— 2/4 个有
- `EmptyHunyuanVideo15Latent` —— 2/4 个有
- `GetImageSize` —— 2/4 个有
- `HunyuanVideo15ImageToVideo` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `ResizeImageMaskNode` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
