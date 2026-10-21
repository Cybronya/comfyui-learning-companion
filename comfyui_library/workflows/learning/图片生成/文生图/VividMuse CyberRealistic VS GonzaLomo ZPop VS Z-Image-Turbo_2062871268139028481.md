---
key: 图片生成/文生图/VividMuse CyberRealistic VS GonzaLomo ZPop VS Z-Image-Turbo_2062871268139028481.json
name: VividMuse CyberRealistic VS GonzaLomo ZPop VS Z-Image-Turbo_2062871268139028481
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/VividMuse CyberRealistic VS GonzaLomo ZPop VS Z-Image-Turbo_2062871268139028481.json
hash: 544726012d863e71
coverage: 0.939394
learned_at: 2026-10-19 23:02:48
nodes: [CLIPLoader, ConditioningZeroOut, VAELoader, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, UNETLoader, CLIPTextEncode, UNETLoader, VAELoader, KSamplerAdvanced, KSamplerAdvanced, easy promptList, CLIPLoader, ConditioningZeroOut, CLIPTextEncode, VAELoader, UNETLoader, KSamplerAdvanced, PrimitiveStringMultiline, EmptyLatentImage, Fast Groups Bypasser (rgthree), easy promptList, VAEDecode, LayerUtility: ImageReel, VAEDecode, VAEDecode, LayerUtility: ImageReelComposit, Seed (rgthree), SaveImage, SaveImage, SaveImage, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": "beta", "height": 2048, "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed", "width": 1536}
---

# 图片生成/文生图/VividMuse CyberRealistic VS GonzaLomo ZPop VS Z-Image-Turbo_2062871268139028481.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/VividMuse CyberRealistic VS GonzaLomo ZPop VS Z-Image-Turbo_2062871268139028481.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `CLIPLoader`
- `ConditioningZeroOut`
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `easy promptList`
- `CLIPLoader`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `PrimitiveStringMultiline`
- `EmptyLatentImage` ★核心
- `Fast Groups Bypasser (rgthree)`
- `easy promptList`
- `VAEDecode` ★核心
- `LayerUtility: ImageReel`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageReelComposit`
- `Seed (rgthree)`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `beta`
- `width` = `1536`
- `height` = `2048`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（31/33）

**有卡**：`CLIPLoader`、`ConditioningZeroOut`、`VAELoader`、`CLIPTextEncode`、`UNETLoader`、`KSamplerAdvanced`、`easy promptList`、`EmptyLatentImage`、`VAEDecode`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`Seed (rgthree)`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader、KSamplerAdvanced
