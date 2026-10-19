---
key: 数字人/数字人/Wan2.2高清修复去AI感添加细节，人物特效数字人视频处理方案_2103973346378600450.json
name: Wan2.2高清修复去AI感添加细节，人物特效数字人视频处理方案_2103973346378600450
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.2高清修复去AI感添加细节，人物特效数字人视频处理方案_2103973346378600450.json
hash: 98e8e2808bccf2ab
coverage: 0.885246
learned_at: 2026-10-19 00:41:06
nodes: [VAELoader, CLIPLoader, TTP_Image_Tile_Batch, CLIPTextEncode, ImageFromBatch, PathchSageAttentionKJ, UpscaleModelLoader, ImageUpscaleWithModel, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, TTP_Image_Assy, ShowText|pysssss, LoraLoaderModelOnly, ModelSamplingSD3, ImageListToImageBatch, VAEDecode, LoraLoaderModelOnly, FluxGuidance, UNETLoader, TTP_Tile_image_size, ImageScaleToTotalPixels, Florence2Run, Florence2ModelLoader, easy imageBatchToImageList, PreviewImage, InjectLatentNoise+, easy cleanGpuUsed, CLIPTextEncode, LoadImage, KSampler, Image Comparer (rgthree), SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/Wan2.2高清修复去AI感添加细节，人物特效数字人视频处理方案_2103973346378600450.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.2高清修复去AI感添加细节，人物特效数字人视频处理方案_2103973346378600450.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（61 个）：
- `VAELoader`
- `CLIPLoader`
- `TTP_Image_Tile_Batch`
- `CLIPTextEncode` ★核心
- `ImageFromBatch`
- `PathchSageAttentionKJ`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEEncode` ★核心
- `TTP_Image_Assy`
- `ShowText|pysssss`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `ImageListToImageBatch`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `FluxGuidance`
- `UNETLoader` ★核心
- `TTP_Tile_image_size`
- `ImageScaleToTotalPixels`
- `Florence2Run`
- `Florence2ModelLoader`
- `easy imageBatchToImageList`
- `PreviewImage`
- `InjectLatentNoise+`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（54/61）

**有卡**：`VAELoader`、`CLIPLoader`、`TTP_Image_Tile_Batch`、`CLIPTextEncode`、`ImageFromBatch`、`PathchSageAttentionKJ`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEEncode`、`TTP_Image_Assy`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`ImageListToImageBatch`、`VAEDecode`、`FluxGuidance`、`UNETLoader`、`TTP_Tile_image_size`、`ImageScaleToTotalPixels`、`Florence2Run`、`Florence2ModelLoader`、`easy imageBatchToImageList`、`InjectLatentNoise+`、`easy cleanGpuUsed`、`LoadImage`、`KSampler`、`SaveImage`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
