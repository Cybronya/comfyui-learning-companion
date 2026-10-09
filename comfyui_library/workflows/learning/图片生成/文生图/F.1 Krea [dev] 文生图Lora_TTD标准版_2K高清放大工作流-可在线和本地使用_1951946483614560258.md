---
key: 图片生成/文生图/F.1 Krea [dev] 文生图Lora_TTD标准版_2K高清放大工作流-可在线和本地使用_1951946483614560258.json
name: F.1 Krea [dev] 文生图Lora_TTD标准版_2K高清放大工作流-可在线和本地使用_1951946483614560258.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/F.1 Krea [dev] 文生图Lora_TTD标准版_2K高清放大工作流-可在线和本地使用_1951946483614560258.json
hash: 1536dcd04d00cb0d
coverage: 0.733333
learned_at: 2026-10-07 23:04:29
nodes: [ConditioningZeroOut, VAEDecode, CLIPTextEncode, CLIPTextEncode, ImageResizeKJ, Reroute, easy imageListToImageBatch, VAEEncode, KSampler, TTP_Image_Assy, easy imageBatchToImageList, TTP_Image_Tile_Batch, ImageUpscaleWithModel, SaveImage, CLIPTextEncode, PreviewImage, TTP_Tile_image_size, KSampler, VAEDecodeTiled, Image Comparer (rgthree), SaveImage, Fast Groups Muter (rgthree), UNETLoader, DualCLIPLoader, VAELoader, LoraLoaderModelOnly, UpscaleModelLoader, EmptySD3LatentImage, Image Comparer (rgthree), ImageSmartSharpen+]
patterns: []
missing: [ImageSmartSharpen+, easy imageBatchToImageList, easy imageListToImageBatch]
parameters: {"cfg": 2.5, "denoise": 0.30000000000000004, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 328338393162286, "steps": 20}
discoveries: [次要节点 `ImageSmartSharpen+` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/F.1 Krea [dev] 文生图Lora_TTD标准版_2K高清放大工作流-可在线和本地使用_1951946483614560258.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1951946483614560258.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageResizeKJ`
- `Reroute`
- `easy imageListToImageBatch`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `TTP_Image_Assy`
- `easy imageBatchToImageList`
- `TTP_Image_Tile_Batch`
- `ImageUpscaleWithModel`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `TTP_Tile_image_size`
- `KSampler` ★核心
- `VAEDecodeTiled` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `Fast Groups Muter (rgthree)`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UpscaleModelLoader`
- `EmptySD3LatentImage`
- `Image Comparer (rgthree)`
- `ImageSmartSharpen+`

## 关键参数

- `seed` = `328338393162286`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **73%**（22/30）

**有卡**：`ConditioningZeroOut`、`VAEDecode`、`CLIPTextEncode`、`ImageResizeKJ`、`VAEEncode`、`KSampler`、`TTP_Image_Assy`、`TTP_Image_Tile_Batch`、`ImageUpscaleWithModel`、`SaveImage`、`TTP_Tile_image_size`、`VAEDecodeTiled`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`UpscaleModelLoader`、`EmptySD3LatentImage`

**缺卡**（3）：`ImageSmartSharpen+`、`easy imageBatchToImageList`、`easy imageListToImageBatch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、UNETLoader、VAEDecodeTiled

## 学习发现

- 次要节点 `ImageSmartSharpen+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识
