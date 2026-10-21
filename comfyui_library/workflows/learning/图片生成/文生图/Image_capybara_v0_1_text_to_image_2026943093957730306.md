---
key: 图片生成/文生图/Image_capybara_v0_1_text_to_image_2026943093957730306.json
name: Image_capybara_v0_1_text_to_image_2026943093957730306
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Image_capybara_v0_1_text_to_image_2026943093957730306.json
hash: 1f1ce77c4da5a010
coverage: 0.823529
learned_at: 2026-10-19 22:29:43
nodes: [CFGGuider, RandomNoise, MarkdownNote, VAEDecode, SaveImage, UNETLoader, DualCLIPLoader, VAELoader, EmptyHunyuanVideo15Latent, MarkdownNote, MarkdownNote, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, SamplerCustomAdvanced, KSamplerSelect, BasicScheduler]
patterns: []
missing: []
---

# 图片生成/文生图/Image_capybara_v0_1_text_to_image_2026943093957730306.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Image_capybara_v0_1_text_to_image_2026943093957730306.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（17 个）：
- `CFGGuider`
- `RandomNoise`
- `MarkdownNote`
- `VAEDecode` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `EmptyHunyuanVideo15Latent`
- `MarkdownNote`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`CFGGuider`、`RandomNoise`、`VAEDecode`、`SaveImage`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`EmptyHunyuanVideo15Latent`、`CLIPTextEncode`、`ModelSamplingSD3`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicScheduler`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、EmptyHunyuanVideo15Latent
