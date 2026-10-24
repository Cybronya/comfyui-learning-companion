---
key: 图片生成/图生图/FLUX.1 Kontext商业级印花_纹理提取工作_2055163655582429186.json
name: FLUX.1 Kontext商业级印花_纹理提取工作_2055163655582429186
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.1 Kontext商业级印花_纹理提取工作_2055163655582429186.json
hash: 83e15c01198c5eab
coverage: 1
learned_at: 2026-10-23 10:54:00
nodes: [DualCLIPLoader, VAELoader, CLIPTextEncode, ReferenceLatent, ConditioningZeroOut, FluxGuidance, VAEDecode, LayerUtility: PurgeVRAM, ImageUpscaleWithModel, UpscaleModelLoader, UNETLoader, LoraLoaderModelOnly, VAEEncode, LoadImage, FluxKontextImageScale, SaveImage, KSampler, CR Latent Input Switch, Int, EmptyLatentImage, ImpactInt, Int, CR Latent Batch Size, 1hew_AnySwitchSelect, LoraLoaderModelOnly, LayerUtility: CropByMask V2, LayerMask: SegformerB2ClothesUltra, Text]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 2, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 362695620583359, "steps": 25, "width": 1024}
---

# 图片生成/图生图/FLUX.1 Kontext商业级印花_纹理提取工作_2055163655582429186.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.1 Kontext商业级印花_纹理提取工作_2055163655582429186.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `DualCLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `ConditioningZeroOut`
- `FluxGuidance`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEEncode` ★核心
- `LoadImage`
- `FluxKontextImageScale`
- `SaveImage`
- `KSampler` ★核心
- `CR Latent Input Switch`
- `Int`
- `EmptyLatentImage` ★核心
- `ImpactInt`
- `Int`
- `CR Latent Batch Size`
- `1hew_AnySwitchSelect`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: CropByMask V2`
- `LayerMask: SegformerB2ClothesUltra`
- `Text`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `362695620583359`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `2`

## 知识

覆盖率 **100%**（28/28）

**有卡**：`DualCLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ReferenceLatent`、`ConditioningZeroOut`、`FluxGuidance`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`VAEEncode`、`LoadImage`、`FluxKontextImageScale`、`SaveImage`、`KSampler`、`CR Latent Input Switch`、`Int`、`EmptyLatentImage`、`ImpactInt`、`CR Latent Batch Size`、`1hew_AnySwitchSelect`、`LayerUtility: CropByMask V2`、`LayerMask: SegformerB2ClothesUltra`、`Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage
