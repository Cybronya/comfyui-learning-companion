---
key: 平台全量/video_capybara_v0_1_video_edit_fast_2027033973167235074.json
name: video_capybara_v0_1_video_edit_fast_2027033973167235074
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/video_capybara_v0_1_video_edit_fast_2027033973167235074.json
hash: a323079206df63f8
coverage: 0.814815
learned_at: 2026-11-14 01:18:35
nodes: [SamplerCustomAdvanced, ModelSamplingSD3, DualCLIPLoader, VAELoader, CLIPTextEncode, KSamplerSelect, RandomNoise, VAEDecode, CLIPVisionLoader, HunyuanVideo15ImageToVideo, CLIPVisionEncode, ResizeImageMaskNode, MarkdownNote, ImageFromBatch, GetVideoComponents, PrimitiveInt, PrimitiveInt, LoadVideo, CreateVideo, SaveVideo, UNETLoader, LoraLoaderModelOnly, CFGGuider, BasicScheduler, CLIPTextEncode, MarkdownNote, MarkdownNote]
patterns: []
missing: []
---

# 平台全量/video_capybara_v0_1_video_edit_fast_2027033973167235074.json

> 来源文件 `comfyui_library/workflows/平台全量/video_capybara_v0_1_video_edit_fast_2027033973167235074.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `SamplerCustomAdvanced` ★核心
- `ModelSamplingSD3`
- `DualCLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `VAEDecode` ★核心
- `CLIPVisionLoader`
- `HunyuanVideo15ImageToVideo`
- `CLIPVisionEncode`
- `ResizeImageMaskNode`
- `MarkdownNote`
- `ImageFromBatch`
- `GetVideoComponents`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadVideo`
- `CreateVideo`
- `SaveVideo`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CFGGuider`
- `BasicScheduler`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `MarkdownNote`

## 知识

覆盖率 **81%**（22/27）

**有卡**：`SamplerCustomAdvanced`、`ModelSamplingSD3`、`DualCLIPLoader`、`VAELoader`、`CLIPTextEncode`、`KSamplerSelect`、`RandomNoise`、`VAEDecode`、`CLIPVisionLoader`、`HunyuanVideo15ImageToVideo`、`CLIPVisionEncode`、`ResizeImageMaskNode`、`ImageFromBatch`、`GetVideoComponents`、`LoadVideo`、`CreateVideo`、`SaveVideo`、`UNETLoader`、`LoraLoaderModelOnly`、`CFGGuider`、`BasicScheduler`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
