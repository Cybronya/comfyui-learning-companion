---
key: 图片生成/图生图/产品融图+背景透视纠正The Fusion of Light and Shadow_2113428078218268673.json
name: 产品融图+背景透视纠正The Fusion of Light and Shadow_2113428078218268673
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/产品融图+背景透视纠正The Fusion of Light and Shadow_2113428078218268673.json
hash: 03e0f8e060d7b1ab
coverage: 0.875
learned_at: 2026-10-26 22:04:54
nodes: [easy getNode, SeedVR2LoadDiTModel, TTP_Tile_image_size, easy imageSize, easy imageBatchToImageList, easy cleanGpuUsed, TTP_Image_Tile_Batch, Reroute, SeedVR2VideoUpscaler, easy setNode, SeedVR2LoadVAEModel, easy setNode, easy setNode, easy setNode, RepeatLatentBatch, easy setNode, easy getNode, ImageResize+, LoraLoaderModelOnly, ConditioningZeroOut, KSampler, VAELoader, easy getNode, easy getNode, JjkText, CR Text Concatenate, TextEncodeQwenImageEditPlusPro_lrzjason, ImageResize+, ImageAutoSelector, easy getNode, VAEDecode, FluxKontextMultiReferenceLatentMethod, easy getNode, UNETLoader, LoraLoaderModelOnly, ImageResize+, CLIPLoader, Int, LoadImage, easy getNode, easy getNode, JjkText, Image Comparer (rgthree), SaveImage, easy getNode, easy getNode, easy getNode, SaveImage, easy getNode, ImageAutoSelector, Image Comparer (rgthree), ImpactMinMax, easy imageListToImageBatch, TTP_Image_Assy, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 909893889473097, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/产品融图+背景透视纠正The Fusion of Light and Shadow_2113428078218268673.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/产品融图+背景透视纠正The Fusion of Light and Shadow_2113428078218268673.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `easy getNode`
- `SeedVR2LoadDiTModel`
- `TTP_Tile_image_size`
- `easy imageSize`
- `easy imageBatchToImageList`
- `easy cleanGpuUsed`
- `TTP_Image_Tile_Batch`
- `Reroute`
- `SeedVR2VideoUpscaler`
- `easy setNode`
- `SeedVR2LoadVAEModel`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `RepeatLatentBatch`
- `easy setNode`
- `easy getNode`
- `ImageResize+`
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAELoader`
- `easy getNode`
- `easy getNode`
- `JjkText`
- `CR Text Concatenate`
- `TextEncodeQwenImageEditPlusPro_lrzjason`
- `ImageResize+`
- `ImageAutoSelector`
- `easy getNode`
- `VAEDecode` ★核心
- `FluxKontextMultiReferenceLatentMethod`
- `easy getNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageResize+`
- `CLIPLoader`
- `Int`
- `LoadImage`
- `easy getNode`
- `easy getNode`
- `JjkText`
- `Image Comparer (rgthree)`
- `SaveImage`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `SaveImage`
- `easy getNode`
- `ImageAutoSelector`
- `Image Comparer (rgthree)`
- `ImpactMinMax`
- `easy imageListToImageBatch`
- `TTP_Image_Assy`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `909893889473097`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（49/56）

**有卡**：`easy getNode`、`SeedVR2LoadDiTModel`、`TTP_Tile_image_size`、`easy imageSize`、`easy imageBatchToImageList`、`easy cleanGpuUsed`、`TTP_Image_Tile_Batch`、`SeedVR2VideoUpscaler`、`easy setNode`、`SeedVR2LoadVAEModel`、`RepeatLatentBatch`、`ImageResize+`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`KSampler`、`VAELoader`、`CR Text Concatenate`、`TextEncodeQwenImageEditPlusPro_lrzjason`、`ImageAutoSelector`、`VAEDecode`、`FluxKontextMultiReferenceLatentMethod`、`UNETLoader`、`CLIPLoader`、`Int`、`LoadImage`、`SaveImage`、`ImpactMinMax`、`easy imageListToImageBatch`、`TTP_Image_Assy`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
