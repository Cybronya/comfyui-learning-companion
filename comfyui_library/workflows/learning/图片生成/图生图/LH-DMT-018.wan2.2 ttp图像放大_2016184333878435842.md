---
key: 图片生成/图生图/LH-DMT-018.wan2.2 ttp图像放大_2016184333878435842.json
name: LH-DMT-018.wan2.2 ttp图像放大_2016184333878435842
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/LH-DMT-018.wan2.2 ttp图像放大_2016184333878435842.json
hash: 34d622aa7385cae9
coverage: 0.962963
learned_at: 2026-10-23 11:08:37
nodes: [BaiduTranslateNode, Float, CLIPTextEncode, CLIPTextEncode, ImageUpscaleWithModel, ImageScaleToTotalPixels, TTP_Tile_image_size, easy cleanGpuUsed, easy cleanGpuUsed, VAEEncode, easy imageBatchToImageList, TTP_Image_Tile_Batch, ModelSamplingSD3, ImageListToImageBatch, KSampler, easy cleanGpuUsed, VAEDecode, TTP_Image_Assy, Image Comparer (rgthree), SaveImage, CLIPLoader, VAELoader, UpscaleModelLoader, UNETLoader, LoadImage, SaveImage, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.15, "sampler_name": "heun", "scheduler": "beta", "seed": 255707736291514, "steps": 10}
---

# 图片生成/图生图/LH-DMT-018.wan2.2 ttp图像放大_2016184333878435842.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/LH-DMT-018.wan2.2 ttp图像放大_2016184333878435842.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `BaiduTranslateNode`
- `Float`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageUpscaleWithModel`
- `ImageScaleToTotalPixels`
- `TTP_Tile_image_size`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VAEEncode` ★核心
- `easy imageBatchToImageList`
- `TTP_Image_Tile_Batch`
- `ModelSamplingSD3`
- `ImageListToImageBatch`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `TTP_Image_Assy`
- `Image Comparer (rgthree)`
- `SaveImage`
- `CLIPLoader`
- `VAELoader`
- `UpscaleModelLoader`
- `UNETLoader` ★核心
- `LoadImage`
- `SaveImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `255707736291514`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.15`

## 知识

覆盖率 **96%**（26/27）

**有卡**：`BaiduTranslateNode`、`Float`、`CLIPTextEncode`、`ImageUpscaleWithModel`、`ImageScaleToTotalPixels`、`TTP_Tile_image_size`、`easy cleanGpuUsed`、`VAEEncode`、`easy imageBatchToImageList`、`TTP_Image_Tile_Batch`、`ModelSamplingSD3`、`ImageListToImageBatch`、`KSampler`、`VAEDecode`、`TTP_Image_Assy`、`SaveImage`、`CLIPLoader`、`VAELoader`、`UpscaleModelLoader`、`UNETLoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEEncode
