---
key: 图片生成/图生图/WAN 2.2  Upscaler_1965097044522188801.json
name: WAN 2.2  Upscaler_1965097044522188801
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/WAN 2.2  Upscaler_1965097044522188801.json
hash: 61999cecbf8f55e8
coverage: 0.863636
learned_at: 2026-10-23 11:27:25
nodes: [ModelSamplingSD3, UNETLoader, VAELoader, CLIPLoader, LoraLoaderModelOnly, CLIPTextEncode, ImageUpscaleWithModel, easy imageBatchToImageList, TTP_Image_Tile_Batch, VAEDecode, PreviewImage, TTP_Image_Assy, ImageListToImageBatch, TTP_Tile_image_size, PreviewImage, CLIPTextEncode, LoadImage, UpscaleModelLoader, Image Comparer (rgthree), SaveImage, KSampler, VAEEncode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.08000000000000002, "sampler_name": "heun", "scheduler": "beta", "seed": 964026935619207, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/WAN 2.2  Upscaler_1965097044522188801.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/WAN 2.2  Upscaler_1965097044522188801.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ImageUpscaleWithModel`
- `easy imageBatchToImageList`
- `TTP_Image_Tile_Batch`
- `VAEDecode` ★核心
- `PreviewImage`
- `TTP_Image_Assy`
- `ImageListToImageBatch`
- `TTP_Tile_image_size`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `UpscaleModelLoader`
- `Image Comparer (rgthree)`
- `SaveImage`
- `KSampler` ★核心
- `VAEEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `964026935619207`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.08000000000000002`

## 知识

覆盖率 **86%**（19/22）

**有卡**：`ModelSamplingSD3`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`ImageUpscaleWithModel`、`easy imageBatchToImageList`、`TTP_Image_Tile_Batch`、`VAEDecode`、`TTP_Image_Assy`、`ImageListToImageBatch`、`TTP_Tile_image_size`、`LoadImage`、`UpscaleModelLoader`、`SaveImage`、`KSampler`、`VAEEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
