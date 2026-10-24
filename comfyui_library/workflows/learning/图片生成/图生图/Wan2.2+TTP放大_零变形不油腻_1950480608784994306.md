---
key: 图片生成/图生图/Wan2.2+TTP放大_零变形不油腻_1950480608784994306.json
name: Wan2.2+TTP放大_零变形不油腻_1950480608784994306
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2+TTP放大_零变形不油腻_1950480608784994306.json
hash: ad82cb60779aa1f7
coverage: 0.903226
learned_at: 2026-10-23 11:28:04
nodes: [VAELoader, TTP_Image_Tile_Batch, easy imageBatchToImageList, PreviewImage, VAEEncode, CLIPTextEncode, VAEDecode, TTP_Image_Assy, UNETLoader, PathchSageAttentionKJ, CLIPTextEncode, TTP_Tile_image_size, ImageUpscaleWithModel, UpscaleModelLoader, ImageScaleToTotalPixels, ImageListToImageBatch, KSampler, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, Anything Everywhere3, EasyCache, ModelSamplingSD3, CFGZeroStar, GLM_Vision_ImageToPrompt, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, SaveImage, Float]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "sampler_name": "dpmpp_2m", "scheduler": "sgm_uniform", "seed": 828040935985997, "steps": 10}
---

# 图片生成/图生图/Wan2.2+TTP放大_零变形不油腻_1950480608784994306.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2+TTP放大_零变形不油腻_1950480608784994306.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `VAELoader`
- `TTP_Image_Tile_Batch`
- `easy imageBatchToImageList`
- `PreviewImage`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `TTP_Image_Assy`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `TTP_Tile_image_size`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `ImageScaleToTotalPixels`
- `ImageListToImageBatch`
- `KSampler` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Anything Everywhere3`
- `EasyCache`
- `ModelSamplingSD3`
- `CFGZeroStar`
- `GLM_Vision_ImageToPrompt`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `Float`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `828040935985997`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **90%**（28/31）

**有卡**：`VAELoader`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`VAEEncode`、`CLIPTextEncode`、`VAEDecode`、`TTP_Image_Assy`、`UNETLoader`、`PathchSageAttentionKJ`、`TTP_Tile_image_size`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`ImageScaleToTotalPixels`、`ImageListToImageBatch`、`KSampler`、`CLIPLoader`、`LoraLoaderModelOnly`、`EasyCache`、`ModelSamplingSD3`、`CFGZeroStar`、`GLM_Vision_ImageToPrompt`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`Float`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
