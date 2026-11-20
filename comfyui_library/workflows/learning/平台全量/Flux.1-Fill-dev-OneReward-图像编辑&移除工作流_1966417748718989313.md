---
key: 平台全量/Flux.1-Fill-dev-OneReward-图像编辑&移除工作流_1966417748718989313.json
name: Flux.1-Fill-dev-OneReward-图像编辑&移除工作流_1966417748718989313
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux.1-Fill-dev-OneReward-图像编辑&移除工作流_1966417748718989313.json
hash: a5548fa77dfab304
coverage: 0.8125
learned_at: 2026-11-14 00:28:50
nodes: [DifferentialDiffusion, ConditioningZeroOut, Mask Fill Holes, VAELoader, PathchSageAttentionKJ, DualCLIPLoader, LoraLoaderModelOnly, KSampler, InpaintModelConditioning, GrowMaskWithBlur, ImageMaskSwitch, VAEDecode, UNETLoader, InpaintCropImproved, LoadImage, InpaintStitchImproved, easy boolean, easy int, easy int, easy ifElse, Note, easy boolean, Image Comparer (rgthree), CLIPTextEncode, Note, ArgosTranslateTextNode, easy ifElse, ShowText|pysssss, FluxGuidance, easy imageSwitch, easy positive, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 864341494068948, "steps": 20}
---

# 平台全量/Flux.1-Fill-dev-OneReward-图像编辑&移除工作流_1966417748718989313.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux.1-Fill-dev-OneReward-图像编辑&移除工作流_1966417748718989313.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（32 个）：
- `DifferentialDiffusion`
- `ConditioningZeroOut`
- `Mask Fill Holes`
- `VAELoader`
- `PathchSageAttentionKJ`
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `InpaintModelConditioning`
- `GrowMaskWithBlur`
- `ImageMaskSwitch`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `InpaintCropImproved`
- `LoadImage`
- `InpaintStitchImproved`
- `easy boolean`
- `easy int`
- `easy int`
- `easy ifElse`
- `Note`
- `easy boolean`
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `Note`
- `ArgosTranslateTextNode`
- `easy ifElse`
- `ShowText|pysssss`
- `FluxGuidance`
- `easy imageSwitch`
- `easy positive`
- `SaveImage`

## 关键参数

- `seed` = `864341494068948`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（26/32）

**有卡**：`DifferentialDiffusion`、`ConditioningZeroOut`、`Mask Fill Holes`、`VAELoader`、`PathchSageAttentionKJ`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`KSampler`、`InpaintModelConditioning`、`GrowMaskWithBlur`、`ImageMaskSwitch`、`VAEDecode`、`UNETLoader`、`InpaintCropImproved`、`LoadImage`、`InpaintStitchImproved`、`easy boolean`、`easy int`、`CLIPTextEncode`、`ArgosTranslateTextNode`、`FluxGuidance`、`easy imageSwitch`、`easy positive`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
