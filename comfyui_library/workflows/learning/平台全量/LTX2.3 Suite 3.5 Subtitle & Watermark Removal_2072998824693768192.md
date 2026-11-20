---
key: 平台全量/LTX2.3 Suite 3.5 Subtitle & Watermark Removal_2072998824693768192.json
name: LTX2.3 Suite 3.5 Subtitle & Watermark Removal_2072998824693768192
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.3 Suite 3.5 Subtitle & Watermark Removal_2072998824693768192.json
hash: b9dd6eb8163d8564
coverage: 0.717949
learned_at: 2026-11-14 00:37:33
nodes: [Note, UNETLoader, UNETLoader, MarkdownNote, Note, PreviewAny, VAELoader, CLIPTextEncode, CreateVideo, SaveVideo, CLIPLoader, KSamplerAdvanced, CLIPTextEncode, VAEDecode, StringReplace, StringReplace, BerniniConditioning, PreviewAny, RHLLMChatNode, ImageFromBatch, PrimitiveInt, easy showAnything, easy showAnything, KSamplerAdvanced, easy showAnything, GetVideoComponents, image_scale_pixel_v2, LoraLoaderModelOnly, LoraLoaderModelOnly, PrimitiveInt, PrimitiveInt, PathchSageAttentionKJ, PathchSageAttentionKJ, BerniniPromptEnhancer, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadVideo]
patterns: []
missing: []
parameters: {"cfg": 14, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 平台全量/LTX2.3 Suite 3.5 Subtitle & Watermark Removal_2072998824693768192.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.3 Suite 3.5 Subtitle & Watermark Removal_2072998824693768192.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `Note`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `MarkdownNote`
- `Note`
- `PreviewAny`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `SaveVideo`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `StringReplace`
- `StringReplace`
- `BerniniConditioning`
- `PreviewAny`
- `RHLLMChatNode`
- `ImageFromBatch`
- `PrimitiveInt`
- `easy showAnything`
- `easy showAnything`
- `KSamplerAdvanced` ★核心
- `easy showAnything`
- `GetVideoComponents`
- `image_scale_pixel_v2`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `BerniniPromptEnhancer`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadVideo`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `14`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **72%**（28/39）

**有卡**：`UNETLoader`、`VAELoader`、`CLIPTextEncode`、`CreateVideo`、`SaveVideo`、`CLIPLoader`、`KSamplerAdvanced`、`VAEDecode`、`StringReplace`、`BerniniConditioning`、`RHLLMChatNode`、`ImageFromBatch`、`GetVideoComponents`、`image_scale_pixel_v2`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`BerniniPromptEnhancer`、`LoadVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、KSamplerAdvanced、BerniniConditioning
