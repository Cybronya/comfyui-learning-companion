---
key: 视频生成/文生视频/Bernini-R Image-to-Video_2072998885414707200.json
name: Bernini-R Image-to-Video_2072998885414707200
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Bernini-R Image-to-Video_2072998885414707200.json
hash: 135386c8ccb7023e
coverage: 0.692308
learned_at: 2026-10-15 22:44:04
nodes: [Note, UNETLoader, UNETLoader, MarkdownNote, Note, PreviewAny, VAELoader, CLIPTextEncode, CLIPLoader, KSamplerAdvanced, CLIPTextEncode, VAEDecode, StringReplace, StringReplace, PreviewAny, RHLLMChatNode, PrimitiveInt, easy showAnything, easy showAnything, KSamplerAdvanced, easy showAnything, image_scale_pixel_v2, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PrimitiveInt, PrimitiveInt, PathchSageAttentionKJ, PathchSageAttentionKJ, SaveVideo, LoadImage, BerniniConditioning, BerniniPromptEnhancer, Text, CreateVideo, PrimitiveFloat]
patterns: []
missing: []
parameters: {"cfg": 14, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/文生视频/Bernini-R Image-to-Video_2072998885414707200.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Bernini-R Image-to-Video_2072998885414707200.json`

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
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `StringReplace`
- `StringReplace`
- `PreviewAny`
- `RHLLMChatNode`
- `PrimitiveInt`
- `easy showAnything`
- `easy showAnything`
- `KSamplerAdvanced` ★核心
- `easy showAnything`
- `image_scale_pixel_v2`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `SaveVideo`
- `LoadImage`
- `BerniniConditioning`
- `BerniniPromptEnhancer`
- `Text`
- `CreateVideo`
- `PrimitiveFloat`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `14`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **69%**（27/39）

**有卡**：`UNETLoader`、`VAELoader`、`CLIPTextEncode`、`CLIPLoader`、`KSamplerAdvanced`、`VAEDecode`、`StringReplace`、`RHLLMChatNode`、`image_scale_pixel_v2`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`SaveVideo`、`LoadImage`、`BerniniConditioning`、`BerniniPromptEnhancer`、`Text`、`CreateVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
