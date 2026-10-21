---
key: 图片生成/文生图/VividMuse Z-Image-Turbo-全能图片G2-Style_2057436016042139650.json
name: VividMuse Z-Image-Turbo-全能图片G2-Style_2057436016042139650
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/VividMuse Z-Image-Turbo-全能图片G2-Style_2057436016042139650.json
hash: 637e97920d1d11ab
coverage: 0.958333
learned_at: 2026-10-19 22:45:43
nodes: [UNETLoader, VAELoader, CLIPLoader, VAELoader, CLIPLoader, UNETLoader, VAELoader, CLIPLoader, UNETLoader, VAELoader, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, LoraLoaderModelOnly, UNETLoader, EmptyLatentImage, LayerUtility: ImageReelComposit, LayerUtility: ImageReel, easy promptList, easy promptList, Fast Groups Bypasser (rgthree), Seed (rgthree), LoraLoaderModelOnly, CLIPTextEncode, ConditioningZeroOut, VAEDecode, KSamplerAdvanced, SaveImage, CLIPTextEncode, ConditioningZeroOut, KSamplerAdvanced, VAEDecode, SaveImage, CLIPTextEncode, ConditioningZeroOut, KSamplerAdvanced, VAEDecode, SaveImage, LoraLoaderModelOnly, KSamplerAdvanced, LoraLoaderModelOnly, KSamplerAdvanced, VAEDecode, SaveImage, KSamplerAdvanced, LoraLoaderModelOnly, PrimitiveStringMultiline, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": "beta57", "height": 2048, "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed", "width": 1536}
---

# 图片生成/文生图/VividMuse Z-Image-Turbo-全能图片G2-Style_2057436016042139650.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/VividMuse Z-Image-Turbo-全能图片G2-Style_2057436016042139650.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageReel`
- `easy promptList`
- `easy promptList`
- `Fast Groups Bypasser (rgthree)`
- `Seed (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `SaveImage`

## 关键参数

- `width` = `1536`
- `height` = `2048`
- `batch_size` = `1`
- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `beta57`

## 知识

覆盖率 **96%**（46/48）

**有卡**：`UNETLoader`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`easy promptList`、`Seed (rgthree)`、`VAEDecode`、`KSamplerAdvanced`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader
