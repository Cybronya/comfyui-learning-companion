---
key: 图片生成/图生图/Image_capybara_v0_1_image_edit_fast_2027042674460594177.json
name: Image_capybara_v0_1_image_edit_fast_2027042674460594177
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Image_capybara_v0_1_image_edit_fast_2027042674460594177.json
hash: e5a3005f3e01a4ad
coverage: 0.869565
learned_at: 2026-10-23 11:03:36
nodes: [MarkdownNote, MarkdownNote, SamplerCustomAdvanced, HunyuanVideo15ImageToVideo, ModelSamplingSD3, VAEDecode, DualCLIPLoader, VAELoader, CLIPVisionLoader, CLIPVisionEncode, ResizeImageMaskNode, CLIPTextEncode, KSamplerSelect, RandomNoise, MarkdownNote, GetImageSize, SaveImage, LoadImage, CLIPTextEncode, UNETLoader, LoraLoaderModelOnly, CFGGuider, BasicScheduler]
patterns: []
missing: []
---

# 图片生成/图生图/Image_capybara_v0_1_image_edit_fast_2027042674460594177.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Image_capybara_v0_1_image_edit_fast_2027042674460594177.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `MarkdownNote`
- `MarkdownNote`
- `SamplerCustomAdvanced` ★核心
- `HunyuanVideo15ImageToVideo`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `ResizeImageMaskNode`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `MarkdownNote`
- `GetImageSize`
- `SaveImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CFGGuider`
- `BasicScheduler`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`SamplerCustomAdvanced`、`HunyuanVideo15ImageToVideo`、`ModelSamplingSD3`、`VAEDecode`、`DualCLIPLoader`、`VAELoader`、`CLIPVisionLoader`、`CLIPVisionEncode`、`ResizeImageMaskNode`、`CLIPTextEncode`、`KSamplerSelect`、`RandomNoise`、`GetImageSize`、`SaveImage`、`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`CFGGuider`、`BasicScheduler`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
