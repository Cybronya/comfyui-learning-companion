---
key: 图片生成/图生图/Wan2.2卓越升级：图生图大师，创意重塑无限！_1950442294635880450.json
name: Wan2.2卓越升级：图生图大师，创意重塑无限！_1950442294635880450
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2卓越升级：图生图大师，创意重塑无限！_1950442294635880450.json
hash: f3cdd8179786e9a1
coverage: 0.923077
learned_at: 2026-10-23 11:28:15
nodes: [UpscaleModelLoader, ImageScaleBy, ImageListToImageBatch, TTP_Image_Assy, DualCLIPLoader, VAELoader, TTP_Tile_image_size, CLIPTextEncode, TTP_Image_Tile_Batch, ImpactImageBatchToImageList, VAEEncode, VAEDecodeTiled, VAELoader, CLIPLoader, LoraLoaderModelOnly, UNETLoader, CLIPTextEncode, CLIPTextEncode, VAEDecode, LoadImage, SaveImage, FastFilmGrain, CLIPTextEncode, ImageUpscaleWithModel, Note, Image Comparer (rgthree), KSampler, ImageUpscaleWithModel, LayerUtility: ImageScaleRestore V2, VAEEncode, UNETLoader, UpscaleModelLoader, SaveImage, KSampler, Florence2ModelLoader, Text, Florence2Run, TextConcatenate, easy showAnything]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.05000000000000001, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 150512508280654, "steps": 10}
---

# 图片生成/图生图/Wan2.2卓越升级：图生图大师，创意重塑无限！_1950442294635880450.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2卓越升级：图生图大师，创意重塑无限！_1950442294635880450.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `UpscaleModelLoader`
- `ImageScaleBy`
- `ImageListToImageBatch`
- `TTP_Image_Assy`
- `DualCLIPLoader`
- `VAELoader`
- `TTP_Tile_image_size`
- `CLIPTextEncode` ★核心
- `TTP_Image_Tile_Batch`
- `ImpactImageBatchToImageList`
- `VAEEncode` ★核心
- `VAEDecodeTiled` ★核心
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `SaveImage`
- `FastFilmGrain`
- `CLIPTextEncode` ★核心
- `ImageUpscaleWithModel`
- `Note`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `ImageUpscaleWithModel`
- `LayerUtility: ImageScaleRestore V2`
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `UpscaleModelLoader`
- `SaveImage`
- `KSampler` ★核心
- `Florence2ModelLoader`
- `Text`
- `Florence2Run`
- `TextConcatenate`
- `easy showAnything`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `150512508280654`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.05000000000000001`

## 知识

覆盖率 **92%**（36/39）

**有卡**：`UpscaleModelLoader`、`ImageScaleBy`、`ImageListToImageBatch`、`TTP_Image_Assy`、`DualCLIPLoader`、`VAELoader`、`TTP_Tile_image_size`、`CLIPTextEncode`、`TTP_Image_Tile_Batch`、`ImpactImageBatchToImageList`、`VAEEncode`、`VAEDecodeTiled`、`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`VAEDecode`、`LoadImage`、`SaveImage`、`FastFilmGrain`、`ImageUpscaleWithModel`、`KSampler`、`LayerUtility: ImageScaleRestore V2`、`Florence2ModelLoader`、`Text`、`Florence2Run`、`TextConcatenate`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
