---
key: 图片生成/文生图/VividMuse Anima workflow V1_2067579804886589442.json
name: VividMuse Anima workflow V1_2067579804886589442
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/VividMuse Anima workflow V1_2067579804886589442.json
hash: a3a250628634fafe
coverage: 0.866667
learned_at: 2026-10-19 23:21:46
nodes: [CLIPLoader, VAELoader, LayerUtility: ImageReel, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, easy promptList, CLIPTextEncode, CLIPTextEncode, KSampler, VAEDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, KSampler, VAEDecode, SaveImage, SaveImage, UpscaleModelLoader, Image Comparer (rgthree), Image Comparer (rgthree), LayerUtility: ImageReelComposit, SaveImage, Fast Groups Bypasser (rgthree), EmptyLatentImage, Seed (rgthree), PrimitiveStringMultiline, PrimitiveStringMultiline, easy promptConcat, easy promptConcat, PrimitiveStringMultiline, SaveImage, easy promptList, RTXVideoSuperResolution, SaveImage, ImageUpscaleWithModel]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 5, "denoise": 1, "height": 1216, "sampler_name": "er_sde", "scheduler": "beta57", "seed": 0, "steps": 30, "width": 832}
---

# 图片生成/文生图/VividMuse Anima workflow V1_2067579804886589442.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/VividMuse Anima workflow V1_2067579804886589442.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: ImageReel`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy promptList`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `UpscaleModelLoader`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `EmptyLatentImage` ★核心
- `Seed (rgthree)`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `easy promptConcat`
- `easy promptConcat`
- `PrimitiveStringMultiline`
- `SaveImage`
- `easy promptList`
- `RTXVideoSuperResolution`
- `SaveImage`
- `ImageUpscaleWithModel`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `0`
- `steps` = `30`
- `cfg` = `5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta57`
- `denoise` = `1`
- `width` = `832`
- `height` = `1216`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（39/45）

**有卡**：`CLIPLoader`、`VAELoader`、`LayerUtility: ImageReel`、`LoraLoaderModelOnly`、`UNETLoader`、`easy promptList`、`CLIPTextEncode`、`KSampler`、`VAEDecode`、`SaveImage`、`UpscaleModelLoader`、`LayerUtility: ImageReelComposit`、`EmptyLatentImage`、`Seed (rgthree)`、`easy promptConcat`、`RTXVideoSuperResolution`、`ImageUpscaleWithModel`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader
