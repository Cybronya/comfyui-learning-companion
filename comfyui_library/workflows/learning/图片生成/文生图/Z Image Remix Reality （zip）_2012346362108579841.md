---
key: 图片生成/文生图/Z Image Remix Reality （zip）_2012346362108579841.json
name: Z Image Remix Reality （zip）_2012346362108579841
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z Image Remix Reality （zip）_2012346362108579841.json
hash: 9f243ee58345f008
coverage: 0.882353
learned_at: 2026-10-19 22:15:21
nodes: [ConditioningZeroOut, CLIPLoader, VAELoader, UNETLoader, Seed (rgthree), CLIPTextEncode, PreviewAny, KSampler, CompressImages, SaveImage, SeedVarianceEnhancer, Fast Groups Bypasser (rgthree), Text, RH_LLMAPI_NODE, VAEDecode, EmptySD3LatentImage, Int]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 3, "steps": 10}
---

# 图片生成/文生图/Z Image Remix Reality （zip）_2012346362108579841.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z Image Remix Reality （zip）_2012346362108579841.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `ConditioningZeroOut`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `Seed (rgthree)`
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `KSampler` ★核心
- `CompressImages`
- `SaveImage`
- `SeedVarianceEnhancer`
- `Fast Groups Bypasser (rgthree)`
- `Text`
- `RH_LLMAPI_NODE`
- `VAEDecode` ★核心
- `EmptySD3LatentImage`
- `Int`

## 关键参数

- `seed` = `3`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`ConditioningZeroOut`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`Seed (rgthree)`、`CLIPTextEncode`、`KSampler`、`CompressImages`、`SaveImage`、`SeedVarianceEnhancer`、`Text`、`RH_LLMAPI_NODE`、`VAEDecode`、`EmptySD3LatentImage`、`Int`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、UNETLoader、Seed (rgthree)
