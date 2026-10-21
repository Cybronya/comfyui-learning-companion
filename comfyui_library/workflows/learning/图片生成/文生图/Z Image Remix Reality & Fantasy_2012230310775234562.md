---
key: 图片生成/文生图/Z Image Remix Reality & Fantasy_2012230310775234562.json
name: Z Image Remix Reality & Fantasy_2012230310775234562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z Image Remix Reality & Fantasy_2012230310775234562.json
hash: 1444e7aba8381902
coverage: 0.928571
learned_at: 2026-10-19 22:15:21
nodes: [ConditioningZeroOut, CLIPLoader, UNETLoader, LayerUtility: ImageReelComposit, KSampler, VAELoader, SeedVarianceEnhancer, SaveImage, EmptySD3LatentImage, ConditioningZeroOut, CLIPLoader, KSampler, VAELoader, SeedVarianceEnhancer, SaveImage, VAEDecode, VAEDecode, LayerUtility: ImageReel, SaveImage, UNETLoader, Seed (rgthree), Seed (rgthree), PreviewAny, EmptySD3LatentImage, CLIPTextEncode, CLIPTextEncode, RH_LLMAPI_NODE, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 3, "steps": 10}
---

# 图片生成/文生图/Z Image Remix Reality & Fantasy_2012230310775234562.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z Image Remix Reality & Fantasy_2012230310775234562.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `ConditioningZeroOut`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LayerUtility: ImageReelComposit`
- `KSampler` ★核心
- `VAELoader`
- `SeedVarianceEnhancer`
- `SaveImage`
- `EmptySD3LatentImage`
- `ConditioningZeroOut`
- `CLIPLoader`
- `KSampler` ★核心
- `VAELoader`
- `SeedVarianceEnhancer`
- `SaveImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageReel`
- `SaveImage`
- `UNETLoader` ★核心
- `Seed (rgthree)`
- `Seed (rgthree)`
- `PreviewAny`
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `RH_LLMAPI_NODE`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `3`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（26/28）

**有卡**：`ConditioningZeroOut`、`CLIPLoader`、`UNETLoader`、`LayerUtility: ImageReelComposit`、`KSampler`、`VAELoader`、`SeedVarianceEnhancer`、`SaveImage`、`EmptySD3LatentImage`、`VAEDecode`、`LayerUtility: ImageReel`、`Seed (rgthree)`、`CLIPTextEncode`、`RH_LLMAPI_NODE`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、UNETLoader、Seed (rgthree)
