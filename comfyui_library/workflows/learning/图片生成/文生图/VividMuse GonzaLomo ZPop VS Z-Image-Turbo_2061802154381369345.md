---
key: 图片生成/文生图/VividMuse GonzaLomo ZPop VS Z-Image-Turbo_2061802154381369345.json
name: VividMuse GonzaLomo ZPop VS Z-Image-Turbo_2061802154381369345
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/VividMuse GonzaLomo ZPop VS Z-Image-Turbo_2061802154381369345.json
hash: ff69baa18c03a59a
coverage: 0.92
learned_at: 2026-10-19 23:02:48
nodes: [CLIPLoader, ConditioningZeroOut, VAELoader, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, LayerUtility: ImageReelComposit, VAEDecode, VAEDecode, LayerUtility: ImageReel, UNETLoader, UNETLoader, VAELoader, KSamplerAdvanced, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSamplerAdvanced, CLIPTextEncode, easy promptList, easy promptList, Seed (rgthree), SaveImage, SaveImage, SaveImage, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": "FlowMatchEulerDiscreteScheduler", "height": 1536, "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed", "width": 1152}
---

# 图片生成/文生图/VividMuse GonzaLomo ZPop VS Z-Image-Turbo_2061802154381369345.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/VividMuse GonzaLomo ZPop VS Z-Image-Turbo_2061802154381369345.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `CLIPLoader`
- `ConditioningZeroOut`
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `LayerUtility: ImageReelComposit`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageReel`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `EmptyLatentImage` ★核心
- `Fast Groups Bypasser (rgthree)`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `easy promptList`
- `easy promptList`
- `Seed (rgthree)`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `FlowMatchEulerDiscreteScheduler`
- `width` = `1152`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（23/25）

**有卡**：`CLIPLoader`、`ConditioningZeroOut`、`VAELoader`、`CLIPTextEncode`、`LayerUtility: ImageReelComposit`、`VAEDecode`、`LayerUtility: ImageReel`、`UNETLoader`、`KSamplerAdvanced`、`EmptyLatentImage`、`easy promptList`、`Seed (rgthree)`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader、KSamplerAdvanced
