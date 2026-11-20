---
key: 平台全量/bernini-1.3B_去除字幕水印_2082731108394954753.json
name: bernini-1.3B_去除字幕水印_2082731108394954753
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/bernini-1.3B_去除字幕水印_2082731108394954753.json
hash: 01a18b89428842db
coverage: 0.608696
learned_at: 2026-11-14 01:09:32
nodes: [SetNode, SetNode, ImageFromBatch, BatchCount+, RepeatImageBatch, BatchImagesNode, SetNode, SetNode, ImageFromBatch, BatchCount+, GetNode, GetNode, SetNode, GetNode, KSamplerAdvanced, easy showAnything, easy showAnything, GetNode, BatchCount+, SimpleMath+, SetNode, VAEDecode, SetNode, easy showAnything, easy showAnything, SimpleMath+, Seed (rgthree), VAELoader, CLIPLoader, MarkdownNote, CLIPTextEncode, MarkdownNote, VHS_VideoInfoLoaded, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, VHS_LoadVideo, ImageResizeKJv2, BerniniConditioning, ModelPreviewOverrideKJ, VHS_VideoCombine, CLIPTextEncode, INTConstant, INTConstant, WanContextWindowsManual, GetNode]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 平台全量/bernini-1.3B_去除字幕水印_2082731108394954753.json

> 来源文件 `comfyui_library/workflows/平台全量/bernini-1.3B_去除字幕水印_2082731108394954753.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（46 个）：
- `SetNode`
- `SetNode`
- `ImageFromBatch`
- `BatchCount+`
- `RepeatImageBatch`
- `BatchImagesNode`
- `SetNode`
- `SetNode`
- `ImageFromBatch`
- `BatchCount+`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `easy showAnything`
- `easy showAnything`
- `GetNode`
- `BatchCount+`
- `SimpleMath+`
- `SetNode`
- `VAEDecode` ★核心
- `SetNode`
- `easy showAnything`
- `easy showAnything`
- `SimpleMath+`
- `Seed (rgthree)`
- `VAELoader`
- `CLIPLoader`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `VHS_VideoInfoLoaded`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `BerniniConditioning`
- `ModelPreviewOverrideKJ`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `INTConstant`
- `INTConstant`
- `WanContextWindowsManual`
- `GetNode`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **61%**（28/46）

**有卡**：`ImageFromBatch`、`BatchCount+`、`RepeatImageBatch`、`BatchImagesNode`、`KSamplerAdvanced`、`SimpleMath+`、`VAEDecode`、`Seed (rgthree)`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`VHS_VideoInfoLoaded`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`VHS_LoadVideo`、`ImageResizeKJv2`、`BerniniConditioning`、`ModelPreviewOverrideKJ`、`VHS_VideoCombine`、`INTConstant`、`WanContextWindowsManual`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、UNETLoader、KSamplerAdvanced、Seed (rgthree)
