---
key: 图片生成/图生图/（高清放大）Wan2.2 - 14B - 加速版 -  图片高清放大_1977811440935600129.json
name: （高清放大）Wan2.2 - 14B - 加速版 -  图片高清放大_1977811440935600129
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（高清放大）Wan2.2 - 14B - 加速版 -  图片高清放大_1977811440935600129.json
hash: 8e2a54c21ff01aa4
coverage: 0.956522
learned_at: 2026-10-23 13:38:37
nodes: [UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAEEncode, easy imageBatchToImageList, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, ImageUpscaleWithModel, ConstrainImage|pysssss, ImageScaleToTotalPixels, easy cleanGpuUsed, UpscaleModelLoader, TTP_Tile_image_size, TTP_Image_Tile_Batch, Note, KSampler, VAEDecode, ImageListToImageBatch, TTP_Image_Assy, SaveImage, VAELoader, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "sampler_name": "heun", "scheduler": "beta", "seed": 828910784053819, "steps": 5}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/（高清放大）Wan2.2 - 14B - 加速版 -  图片高清放大_1977811440935600129.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（高清放大）Wan2.2 - 14B - 加速版 -  图片高清放大_1977811440935600129.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAEEncode` ★核心
- `easy imageBatchToImageList`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageUpscaleWithModel`
- `ConstrainImage|pysssss`
- `ImageScaleToTotalPixels`
- `easy cleanGpuUsed`
- `UpscaleModelLoader`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `Note`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImageListToImageBatch`
- `TTP_Image_Assy`
- `SaveImage`
- `VAELoader`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `828910784053819`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **96%**（22/23）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAEEncode`、`easy imageBatchToImageList`、`ModelSamplingSD3`、`CLIPTextEncode`、`ImageUpscaleWithModel`、`ConstrainImage|pysssss`、`ImageScaleToTotalPixels`、`easy cleanGpuUsed`、`UpscaleModelLoader`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`KSampler`、`VAEDecode`、`ImageListToImageBatch`、`TTP_Image_Assy`、`SaveImage`、`VAELoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
