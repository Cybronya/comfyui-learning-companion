---
key: 平台全量/video_capybara_v0_1_video_edit_2027025679124013057.json
name: video_capybara_v0_1_video_edit_2027025679124013057
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/video_capybara_v0_1_video_edit_2027025679124013057.json
hash: 0d0b496a268b8d04
coverage: 0.807692
learned_at: 2026-11-14 01:18:34
nodes: [BasicScheduler, CFGGuider, SamplerCustomAdvanced, ModelSamplingSD3, UNETLoader, DualCLIPLoader, VAELoader, CLIPTextEncode, KSamplerSelect, RandomNoise, VAEDecode, CLIPVisionLoader, HunyuanVideo15ImageToVideo, CLIPVisionEncode, ResizeImageMaskNode, MarkdownNote, ImageFromBatch, MarkdownNote, MarkdownNote, GetVideoComponents, PrimitiveInt, PrimitiveInt, LoadVideo, CLIPTextEncode, CreateVideo, SaveVideo]
patterns: []
missing: []
---

# 平台全量/video_capybara_v0_1_video_edit_2027025679124013057.json

> 来源文件 `comfyui_library/workflows/平台全量/video_capybara_v0_1_video_edit_2027025679124013057.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `BasicScheduler`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
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
- `MarkdownNote`
- `MarkdownNote`
- `GetVideoComponents`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadVideo`
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `SaveVideo`

## 知识

覆盖率 **81%**（21/26）

**有卡**：`BasicScheduler`、`CFGGuider`、`SamplerCustomAdvanced`、`ModelSamplingSD3`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`CLIPTextEncode`、`KSamplerSelect`、`RandomNoise`、`VAEDecode`、`CLIPVisionLoader`、`HunyuanVideo15ImageToVideo`、`CLIPVisionEncode`、`ResizeImageMaskNode`、`ImageFromBatch`、`GetVideoComponents`、`LoadVideo`、`CreateVideo`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、CLIPVisionEncode
