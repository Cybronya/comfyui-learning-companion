---
key: 平台全量/哑巴wan2.7-bernini编辑_2075025297367453697.json
name: 哑巴wan2.7-bernini编辑_2075025297367453697
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/哑巴wan2.7-bernini编辑_2075025297367453697.json
hash: b56d7acd0c1f400f
coverage: 0.75
learned_at: 2026-11-14 01:52:16
nodes: [UNETLoader, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, PathchSageAttentionKJ, CLIPTextEncode, VAEDecode, VHS_VideoCombine, BerniniConditioning, KSamplerAdvanced, KSamplerAdvanced, WanContextWindowsManual, StringReplace, PreviewAny, StringConcatenate, PrimitiveStringMultiline, WanContextWindowsManual, VHS_VideoInfoLoaded, easy showAnything, PrimitiveInt, PrimitiveInt, PrimitiveInt, LoadImage, LoadImage, VHS_LoadVideo, MarkdownNote, PathchSageAttentionKJ, CLIPTextEncode, LoadImage, CustomCombo, RegexExtract, PrimitiveStringMultiline, LoadImage, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 平台全量/哑巴wan2.7-bernini编辑_2075025297367453697.json

> 来源文件 `comfyui_library/workflows/平台全量/哑巴wan2.7-bernini编辑_2075025297367453697.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（36 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `BerniniConditioning`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `WanContextWindowsManual`
- `StringReplace`
- `PreviewAny`
- `StringConcatenate`
- `PrimitiveStringMultiline`
- `WanContextWindowsManual`
- `VHS_VideoInfoLoaded`
- `easy showAnything`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `LoadImage`
- `VHS_LoadVideo`
- `MarkdownNote`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CustomCombo`
- `RegexExtract`
- `PrimitiveStringMultiline`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **75%**（27/36）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`VAEDecode`、`VHS_VideoCombine`、`BerniniConditioning`、`KSamplerAdvanced`、`WanContextWindowsManual`、`StringReplace`、`StringConcatenate`、`VHS_VideoInfoLoaded`、`LoadImage`、`VHS_LoadVideo`、`CustomCombo`、`RegexExtract`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、KSamplerAdvanced
