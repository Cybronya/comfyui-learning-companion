---
key: 图片生成/文生图/Image_capybara_v0_1_text_to_image_fast_2027038386724278274.json
name: Image_capybara_v0_1_text_to_image_fast_2027038386724278274
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Image_capybara_v0_1_text_to_image_fast_2027038386724278274.json
hash: 71bd65a359339d0e
coverage: 0.833333
learned_at: 2026-10-19 22:29:43
nodes: [SamplerCustomAdvanced, ModelSamplingSD3, DualCLIPLoader, VAELoader, CLIPTextEncode, KSamplerSelect, RandomNoise, MarkdownNote, VAEDecode, MarkdownNote, MarkdownNote, EmptyHunyuanVideo15Latent, SaveImage, UNETLoader, BasicScheduler, CFGGuider, CLIPTextEncode, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 图片生成/文生图/Image_capybara_v0_1_text_to_image_fast_2027038386724278274.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Image_capybara_v0_1_text_to_image_fast_2027038386724278274.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（18 个）：
- `SamplerCustomAdvanced` ★核心
- `ModelSamplingSD3`
- `DualCLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `MarkdownNote`
- `VAEDecode` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `EmptyHunyuanVideo15Latent`
- `SaveImage`
- `UNETLoader` ★核心
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **83%**（15/18）

**有卡**：`SamplerCustomAdvanced`、`ModelSamplingSD3`、`DualCLIPLoader`、`VAELoader`、`CLIPTextEncode`、`KSamplerSelect`、`RandomNoise`、`VAEDecode`、`EmptyHunyuanVideo15Latent`、`SaveImage`、`UNETLoader`、`BasicScheduler`、`CFGGuider`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
