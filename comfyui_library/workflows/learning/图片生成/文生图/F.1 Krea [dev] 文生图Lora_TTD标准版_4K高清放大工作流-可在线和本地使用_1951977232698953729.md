---
key: 图片生成/文生图/F.1 Krea [dev] 文生图Lora_TTD标准版_4K高清放大工作流-可在线和本地使用_1951977232698953729.json
name: F.1 Krea [dev] 文生图Lora_TTD标准版_4K高清放大工作流-可在线和本地使用_1951977232698953729
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/F.1 Krea [dev] 文生图Lora_TTD标准版_4K高清放大工作流-可在线和本地使用_1951977232698953729.json
hash: f1ca177aa4f77941
coverage: 0.733333
learned_at: 2026-10-10 20:58:30
nodes: [ConditioningZeroOut, VAEDecode, CLIPTextEncode, ImageResizeKJ, Reroute, easy imageListToImageBatch, VAEEncode, TTP_Image_Assy, easy imageBatchToImageList, TTP_Image_Tile_Batch, ImageUpscaleWithModel, SaveImage, CLIPTextEncode, PreviewImage, KSampler, ImageSmartSharpen+, Image Comparer (rgthree), SaveImage, Image Comparer (rgthree), EmptySD3LatentImage, Fast Groups Muter (rgthree), KSampler, CLIPTextEncode, TTP_Tile_image_size, VAEDecodeTiled, UNETLoader, DualCLIPLoader, VAELoader, LoraLoaderModelOnly, UpscaleModelLoader]
patterns: []
missing: [ImageSmartSharpen+, easy imageBatchToImageList, easy imageListToImageBatch]
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1113397394038095, "steps": 30}
discoveries: [次要节点 `ImageSmartSharpen+` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/F.1 Krea [dev] 文生图Lora_TTD标准版_4K高清放大工作流-可在线和本地使用_1951977232698953729.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/F.1 Krea [dev] 文生图Lora_TTD标准版_4K高清放大工作流-可在线和本地使用_1951977232698953729.json`

## 结构

**节点**（30 个）：
- `ConditioningZeroOut`
- `VAEDecode`
- `CLIPTextEncode`
- `ImageResizeKJ`
- `Reroute`
- `easy imageListToImageBatch`
- `VAEEncode`
- `TTP_Image_Assy`
- `easy imageBatchToImageList`
- `TTP_Image_Tile_Batch`
- `ImageUpscaleWithModel`
- `SaveImage`
- `CLIPTextEncode`
- `PreviewImage`
- `KSampler`
- `ImageSmartSharpen+`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Image Comparer (rgthree)`
- `EmptySD3LatentImage`
- `Fast Groups Muter (rgthree)`
- `KSampler`
- `CLIPTextEncode`
- `TTP_Tile_image_size`
- `VAEDecodeTiled`
- `UNETLoader`
- `DualCLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly`
- `UpscaleModelLoader`

## 关键参数

- `cfg` = `2.5`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `1113397394038095`
- `steps` = `30`

## 知识

覆盖率 **73%**（22/30）

**有卡**：`ConditioningZeroOut`、`VAEDecode`、`CLIPTextEncode`、`ImageResizeKJ`、`Reroute`、`easy imageListToImageBatch`、`VAEEncode`、`TTP_Image_Assy`、`easy imageBatchToImageList`、`TTP_Image_Tile_Batch`、`ImageUpscaleWithModel`、`SaveImage`、`PreviewImage`、`KSampler`、`ImageSmartSharpen+`、`Image Comparer (rgthree)`、`EmptySD3LatentImage`、`Fast Groups Muter (rgthree)`

**缺卡**（3）：`ImageSmartSharpen+`、`easy imageBatchToImageList`、`easy imageListToImageBatch`

## 学习发现

- 次要节点 `ImageSmartSharpen+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识
