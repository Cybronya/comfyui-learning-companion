---
key: 图片生成/文生图/wan2.2文生图 高清放大_1950888087578681345.json
name: wan2.2文生图 高清放大_1950888087578681345.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2文生图 高清放大_1950888087578681345.json
hash: 0f79f93d3dfadde1
coverage: 0.8
learned_at: 2026-10-07 22:58:42
nodes: [ImageScaleToTotalPixels, UpscaleModelLoader, CLIPLoader, CLIPTextEncode, UNETLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, KSampler, ModelSamplingSD3, CLIPTextEncode, UNETLoader, CLIPLoader, VAELoader, ModelSamplingSD3, LoraLoaderModelOnly, PathchSageAttentionKJ, Anything Everywhere3, TTP_Tile_image_size, TTP_Image_Tile_Batch, easy imageBatchToImageList, VAEEncode, easy cleanGpuUsed, easy cleanGpuUsed, ImageUpscaleWithModel, TTP_Image_Assy, VAELoader, CLIPTextEncode, easy cleanGpuUsed, Image Comparer (rgthree), LoraLoaderModelOnly, ImageListToImageBatch, VAEDecode, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, KSampler, RH_Prompter, CLIPTextEncode, KSampler, RH_Translator, PreviewImage, easy seed, SDXLEmptyLatentSizePicker+]
patterns: []
missing: [easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy imageBatchToImageList, SDXLEmptyLatentSizePicker+, easy seed]
parameters: {"batch_size": 0, "cfg": 1, "denoise": 1, "height": 1, "sampler_name": "heun", "scheduler": "beta", "seed": 497163970725457, "steps": 10, "width": "768x1280 (0.6)"}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识, 核心节点 `SDXLEmptyLatentSizePicker+` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/wan2.2文生图 高清放大_1950888087578681345.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1950888087578681345.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `ImageScaleToTotalPixels`
- `UpscaleModelLoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `KSampler` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `Anything Everywhere3`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `easy imageBatchToImageList`
- `VAEEncode` ★核心
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ImageUpscaleWithModel`
- `TTP_Image_Assy`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `ImageListToImageBatch`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `RH_Prompter`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `RH_Translator`
- `PreviewImage`
- `easy seed`
- `SDXLEmptyLatentSizePicker+` ★核心

## 关键参数

- `seed` = `497163970725457`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `768x1280 (0.6)`
- `height` = `1`
- `batch_size` = `0`

## 知识

覆盖率 **80%**（36/45）

**有卡**：`ImageScaleToTotalPixels`、`UpscaleModelLoader`、`CLIPLoader`、`CLIPTextEncode`、`UNETLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`KSampler`、`VAELoader`、`LoraLoaderModelOnly`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`VAEEncode`、`ImageUpscaleWithModel`、`TTP_Image_Assy`、`ImageListToImageBatch`、`VAEDecode`、`SaveImage`、`RH_Prompter`、`RH_Translator`

**缺卡**（6）：`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy imageBatchToImageList`、`SDXLEmptyLatentSizePicker+`、`easy seed`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、VAEEncode

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识
- 核心节点 `SDXLEmptyLatentSizePicker+` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
