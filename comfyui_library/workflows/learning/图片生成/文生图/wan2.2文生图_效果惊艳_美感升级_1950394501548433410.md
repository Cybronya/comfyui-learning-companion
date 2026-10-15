---
key: 图片生成/文生图/wan2.2文生图_效果惊艳_美感升级_1950394501548433410.json
name: wan2.2文生图_效果惊艳_美感升级_1950394501548433410
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2文生图_效果惊艳_美感升级_1950394501548433410.json
hash: 60c354170c1d0300
coverage: 0.830189
learned_at: 2026-10-15 22:27:58
nodes: [VAELoader, CLIPLoader, Anything Everywhere3, TTP_Image_Tile_Batch, easy imageBatchToImageList, ImageScaleToTotalPixels, easy cleanGpuUsed, VAEEncode, easy cleanGpuUsed, SetNode, GetNode, TTP_Image_Assy, PreviewImage, ImageUpscaleWithModel, UpscaleModelLoader, SaveImage, ModelSamplingSD3, UNETLoader, CLIPLoader, VAELoader, UNETLoader, CLIPTextEncode, SDXLEmptyLatentSizePicker+, VAEDecode, Image Comparer (rgthree), CR Text Concatenate, RH_Prompter, ShowText|pysssss, KSampler, KSampler, easy seed, CR Text, RH_Translator, UNETLoader, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, ImageListToImageBatch, VAEDecode, SetNode, GetNode, TTP_Tile_image_size, KSampler, PreviewImage, easy cleanGpuUsed]
patterns: []
missing: []
parameters: {"batch_size": 0, "cfg": 1, "denoise": 0.06000000000000001, "height": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 407064752208603, "steps": 10, "width": "1280x768 (1.67)"}
---

# 图片生成/文生图/wan2.2文生图_效果惊艳_美感升级_1950394501548433410.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2文生图_效果惊艳_美感升级_1950394501548433410.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `VAELoader`
- `CLIPLoader`
- `Anything Everywhere3`
- `TTP_Image_Tile_Batch`
- `easy imageBatchToImageList`
- `ImageScaleToTotalPixels`
- `easy cleanGpuUsed`
- `VAEEncode` ★核心
- `easy cleanGpuUsed`
- `SetNode`
- `GetNode`
- `TTP_Image_Assy`
- `PreviewImage`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `SaveImage`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `SDXLEmptyLatentSizePicker+` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `CR Text Concatenate`
- `RH_Prompter`
- `ShowText|pysssss`
- `KSampler` ★核心
- `KSampler` ★核心
- `easy seed`
- `CR Text`
- `RH_Translator`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ImageListToImageBatch`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `TTP_Tile_image_size`
- `KSampler` ★核心
- `PreviewImage`
- `easy cleanGpuUsed`

## 关键参数

- `width` = `1280x768 (1.67)`
- `height` = `1`
- `batch_size` = `0`
- `seed` = `407064752208603`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.06000000000000001`

## 知识

覆盖率 **83%**（44/53）

**有卡**：`VAELoader`、`CLIPLoader`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`ImageScaleToTotalPixels`、`easy cleanGpuUsed`、`VAEEncode`、`TTP_Image_Assy`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`SaveImage`、`ModelSamplingSD3`、`UNETLoader`、`CLIPTextEncode`、`SDXLEmptyLatentSizePicker+`、`VAEDecode`、`CR Text Concatenate`、`RH_Prompter`、`KSampler`、`easy seed`、`CR Text`、`RH_Translator`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`ImageListToImageBatch`、`TTP_Tile_image_size`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、easy seed
