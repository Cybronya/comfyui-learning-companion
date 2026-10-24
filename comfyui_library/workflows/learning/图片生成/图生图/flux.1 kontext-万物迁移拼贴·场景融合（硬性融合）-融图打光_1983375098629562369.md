---
key: 图片生成/图生图/flux.1 kontext-万物迁移拼贴·场景融合（硬性融合）-融图打光_1983375098629562369.json
name: flux.1 kontext-万物迁移拼贴·场景融合（硬性融合）-融图打光_1983375098629562369
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/flux.1 kontext-万物迁移拼贴·场景融合（硬性融合）-融图打光_1983375098629562369.json
hash: 8e2cf23f0ea14c3a
coverage: 0.787879
learned_at: 2026-10-23 11:35:50
nodes: [Reroute, Reroute, SetNode, FastCanvasTool, LayerMask: PersonMaskUltra V2, SetNode, easy imageRemBg, GrowMask, BatchCropFromMaskAdvanced, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, DualCLIPLoader, VAELoader, ReferenceLatent, RebatchLatents, KSampler, ConditioningZeroOut, FluxGuidance, VAEEncodeTiled, FluxKontextImageScale, VAEDecode, RepeatLatentBatch, PreviewImage, Anything Everywhere3, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, SaveImage, Note, LoadImage, LoadImage, FastCanvas, 孤海-图像与遮罩描边]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 881431773295040, "steps": 20}
---

# 图片生成/图生图/flux.1 kontext-万物迁移拼贴·场景融合（硬性融合）-融图打光_1983375098629562369.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/flux.1 kontext-万物迁移拼贴·场景融合（硬性融合）-融图打光_1983375098629562369.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `Reroute`
- `Reroute`
- `SetNode`
- `FastCanvasTool`
- `LayerMask: PersonMaskUltra V2`
- `SetNode`
- `easy imageRemBg`
- `GrowMask`
- `BatchCropFromMaskAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `ReferenceLatent`
- `RebatchLatents`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `FluxGuidance`
- `VAEEncodeTiled` ★核心
- `FluxKontextImageScale`
- `VAEDecode` ★核心
- `RepeatLatentBatch`
- `PreviewImage`
- `Anything Everywhere3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `Note`
- `LoadImage`
- `LoadImage`
- `FastCanvas`
- `孤海-图像与遮罩描边`

## 关键参数

- `seed` = `881431773295040`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（26/33）

**有卡**：`FastCanvasTool`、`LayerMask: PersonMaskUltra V2`、`easy imageRemBg`、`GrowMask`、`BatchCropFromMaskAdvanced`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`ReferenceLatent`、`RebatchLatents`、`KSampler`、`ConditioningZeroOut`、`FluxGuidance`、`VAEEncodeTiled`、`FluxKontextImageScale`、`VAEDecode`、`RepeatLatentBatch`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`SaveImage`、`LoadImage`、`FastCanvas`、`孤海-图像与遮罩描边`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
