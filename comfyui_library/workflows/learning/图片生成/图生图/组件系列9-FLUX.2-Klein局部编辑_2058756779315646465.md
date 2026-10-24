---
key: 图片生成/图生图/组件系列9-FLUX.2-Klein局部编辑_2058756779315646465.json
name: 组件系列9-FLUX.2-Klein局部编辑_2058756779315646465
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/组件系列9-FLUX.2-Klein局部编辑_2058756779315646465.json
hash: dd1bd3adcf57e899
coverage: 0.708333
learned_at: 2026-10-23 13:21:35
nodes: [INPAINT_ExpandMask, CLIPLoader, VAELoader, CLIPTextEncode, ConditioningZeroOut, ReferenceLatent, ReferenceLatent, UNETLoader, KSampler, VAEDecode, SetNode, LoadImage, GetNode, SaveImage, Image Comparer (rgthree), InpaintModelConditioning, ImageAndMaskPreview, Seed (rgthree), GetNode, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, PrimitiveStringMultiline, PreviewImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 651305037196267, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/组件系列9-FLUX.2-Klein局部编辑_2058756779315646465.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/组件系列9-FLUX.2-Klein局部编辑_2058756779315646465.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `INPAINT_ExpandMask`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ReferenceLatent`
- `ReferenceLatent`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `LoadImage`
- `GetNode`
- `SaveImage`
- `Image Comparer (rgthree)`
- `InpaintModelConditioning`
- `ImageAndMaskPreview`
- `Seed (rgthree)`
- `GetNode`
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `PrimitiveStringMultiline`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `651305037196267`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **71%**（17/24）

**有卡**：`INPAINT_ExpandMask`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`ReferenceLatent`、`UNETLoader`、`KSampler`、`VAEDecode`、`LoadImage`、`SaveImage`、`InpaintModelConditioning`、`ImageAndMaskPreview`、`Seed (rgthree)`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
