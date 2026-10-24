---
key: 图片生成/图生图/一键三视图Kontext-character-creator_1943503167298695169.json
name: 一键三视图Kontext-character-creator_1943503167298695169
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/一键三视图Kontext-character-creator_1943503167298695169.json
hash: 338959e398197848
coverage: 0.525
learned_at: 2026-10-23 11:54:31
nodes: [PreviewImage, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, VAEDecode, SetNode, LoadImage, UNETLoader, PathchSageAttentionKJ, PatchModelPatcherOrder, CFGZeroStar, DualCLIPLoader, VAELoader, RMBG, ImageResizeKJv2, ImageStitch, SetNode, SetNode, FluxKontextImageScale, EmptySD3LatentImage, VAEEncode, GetNode, GetNode, SetNode, GetNode, PrimitiveInt, PrimitiveInt, GetNode, GetNode, KSampler, FluxGuidance, SaveImage, ReferenceLatent, ConditioningZeroOut, LoadImage, CLIPTextEncode]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 80087, "steps": 25}
---

# 图片生成/图生图/一键三视图Kontext-character-creator_1943503167298695169.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/一键三视图Kontext-character-creator_1943503167298695169.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `PreviewImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
- `SetNode`
- `LoadImage`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `PatchModelPatcherOrder`
- `CFGZeroStar`
- `DualCLIPLoader`
- `VAELoader`
- `RMBG`
- `ImageResizeKJv2`
- `ImageStitch`
- `SetNode`
- `SetNode`
- `FluxKontextImageScale`
- `EmptySD3LatentImage`
- `VAEEncode` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `FluxGuidance`
- `SaveImage`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `LoadImage`
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `80087`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **52%**（21/40）

**有卡**：`VAEDecode`、`LoadImage`、`UNETLoader`、`PathchSageAttentionKJ`、`PatchModelPatcherOrder`、`CFGZeroStar`、`DualCLIPLoader`、`VAELoader`、`RMBG`、`ImageResizeKJv2`、`ImageStitch`、`FluxKontextImageScale`、`EmptySD3LatentImage`、`VAEEncode`、`KSampler`、`FluxGuidance`、`SaveImage`、`ReferenceLatent`、`ConditioningZeroOut`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
