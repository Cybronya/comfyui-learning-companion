---
key: 图片生成/图生图/Image_capybara_v0_1_image_edit_2027040053440024577.json
name: Image_capybara_v0_1_image_edit_2027040053440024577
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Image_capybara_v0_1_image_edit_2027040053440024577.json
hash: f4de6ed2317405ee
coverage: 0.863636
learned_at: 2026-10-23 11:03:35
nodes: [MarkdownNote, MarkdownNote, CFGGuider, SamplerCustomAdvanced, ModelSamplingSD3, VAEDecode, UNETLoader, DualCLIPLoader, VAELoader, ResizeImageMaskNode, CLIPTextEncode, KSamplerSelect, RandomNoise, BasicScheduler, MarkdownNote, GetImageSize, SaveImage, LoadImage, CLIPTextEncode, CLIPVisionLoader, CLIPVisionEncode, HunyuanVideo15ImageToVideo]
patterns: []
missing: []
---

# 图片生成/图生图/Image_capybara_v0_1_image_edit_2027040053440024577.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Image_capybara_v0_1_image_edit_2027040053440024577.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `MarkdownNote`
- `MarkdownNote`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `ResizeImageMaskNode`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `BasicScheduler`
- `MarkdownNote`
- `GetImageSize`
- `SaveImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `HunyuanVideo15ImageToVideo`

## 知识

覆盖率 **86%**（19/22）

**有卡**：`CFGGuider`、`SamplerCustomAdvanced`、`ModelSamplingSD3`、`VAEDecode`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`ResizeImageMaskNode`、`CLIPTextEncode`、`KSamplerSelect`、`RandomNoise`、`BasicScheduler`、`GetImageSize`、`SaveImage`、`LoadImage`、`CLIPVisionLoader`、`CLIPVisionEncode`、`HunyuanVideo15ImageToVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
