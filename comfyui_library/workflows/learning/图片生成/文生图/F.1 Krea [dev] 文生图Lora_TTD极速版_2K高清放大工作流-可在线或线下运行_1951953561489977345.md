---
key: 图片生成/文生图/F.1 Krea [dev] 文生图Lora_TTD极速版_2K高清放大工作流-可在线或线下运行_1951953561489977345.json
name: F.1 Krea [dev] 文生图Lora_TTD极速版_2K高清放大工作流-可在线或线下运行_1951953561489977345.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/F.1 Krea [dev] 文生图Lora_TTD极速版_2K高清放大工作流-可在线或线下运行_1951953561489977345.json
hash: dc3c0ba30a245f00
coverage: 0.741935
learned_at: 2026-10-07 23:04:30
nodes: [ConditioningZeroOut, VAEDecode, CLIPTextEncode, ImageResizeKJ, Reroute, easy imageListToImageBatch, VAEEncode, TTP_Image_Assy, easy imageBatchToImageList, TTP_Image_Tile_Batch, ImageUpscaleWithModel, SaveImage, CLIPTextEncode, PreviewImage, ImageSmartSharpen+, Image Comparer (rgthree), SaveImage, Image Comparer (rgthree), EmptySD3LatentImage, Fast Groups Muter (rgthree), KSampler, CLIPTextEncode, VAEDecodeTiled, KSampler, TTP_Tile_image_size, UNETLoader, DualCLIPLoader, VAELoader, LoraLoaderModelOnly, UpscaleModelLoader, LoraLoaderModelOnly]
patterns: []
missing: [ImageSmartSharpen+, easy imageBatchToImageList, easy imageListToImageBatch]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 2.5, "denoise": 0.30000000000000004, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 328338393162286, "steps": 4}
discoveries: [次要节点 `ImageSmartSharpen+` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/F.1 Krea [dev] 文生图Lora_TTD极速版_2K高清放大工作流-可在线或线下运行_1951953561489977345.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1951953561489977345.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `ImageResizeKJ`
- `Reroute`
- `easy imageListToImageBatch`
- `VAEEncode` ★核心
- `TTP_Image_Assy`
- `easy imageBatchToImageList`
- `TTP_Image_Tile_Batch`
- `ImageUpscaleWithModel`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `ImageSmartSharpen+`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Image Comparer (rgthree)`
- `EmptySD3LatentImage`
- `Fast Groups Muter (rgthree)`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecodeTiled` ★核心
- `KSampler` ★核心
- `TTP_Tile_image_size`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `328338393162286`
- `steps` = `4`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **74%**（23/31）

**有卡**：`ConditioningZeroOut`、`VAEDecode`、`CLIPTextEncode`、`ImageResizeKJ`、`VAEEncode`、`TTP_Image_Assy`、`TTP_Image_Tile_Batch`、`ImageUpscaleWithModel`、`SaveImage`、`EmptySD3LatentImage`、`KSampler`、`VAEDecodeTiled`、`TTP_Tile_image_size`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`UpscaleModelLoader`

**缺卡**（3）：`ImageSmartSharpen+`、`easy imageBatchToImageList`、`easy imageListToImageBatch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、UNETLoader、VAEDecodeTiled

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `ImageSmartSharpen+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
