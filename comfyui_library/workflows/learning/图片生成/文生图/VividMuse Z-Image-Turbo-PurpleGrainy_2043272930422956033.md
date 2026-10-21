---
key: 图片生成/文生图/VividMuse Z-Image-Turbo-PurpleGrainy_2043272930422956033.json
name: VividMuse Z-Image-Turbo-PurpleGrainy_2043272930422956033
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/VividMuse Z-Image-Turbo-PurpleGrainy_2043272930422956033.json
hash: 27ff66c741fa7c17
coverage: 0.875
learned_at: 2026-10-21 02:55:19
nodes: [UNETLoader, VAELoader, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, UNETLoader, VAELoader, CLIPLoader, ConditioningZeroOut, CLIPTextEncode, PreviewImage, VAEDecode, VAEDecode, SaveImage, LayerUtility: ImageReelComposit, SaveImage, BasicScheduler, KSamplerAdvanced, LoraLoaderModelOnly, LayerUtility: ImageReel, BasicScheduler, Fast Groups Bypasser (rgthree), EmptyLatentImage, SigmasPreview, SigmasPreview, easy promptList, easy promptList, Seed (rgthree), SaveImage, PreviewImage, KSamplerAdvanced, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": "simple", "height": 2048, "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed", "width": 1536}
---

# 图片生成/文生图/VividMuse Z-Image-Turbo-PurpleGrainy_2043272930422956033.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/VividMuse Z-Image-Turbo-PurpleGrainy_2043272930422956033.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `BasicScheduler`
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageReel`
- `BasicScheduler`
- `Fast Groups Bypasser (rgthree)`
- `EmptyLatentImage` ★核心
- `SigmasPreview`
- `SigmasPreview`
- `easy promptList`
- `easy promptList`
- `Seed (rgthree)`
- `SaveImage`
- `PreviewImage`
- `KSamplerAdvanced` ★核心
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`
- `width` = `1536`
- `height` = `2048`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（28/32）

**有卡**：`UNETLoader`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`VAEDecode`、`SaveImage`、`LayerUtility: ImageReelComposit`、`BasicScheduler`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`LayerUtility: ImageReel`、`EmptyLatentImage`、`SigmasPreview`、`easy promptList`、`Seed (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader
