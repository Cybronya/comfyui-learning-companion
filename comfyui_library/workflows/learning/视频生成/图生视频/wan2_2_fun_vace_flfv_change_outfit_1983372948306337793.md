---
key: 视频生成/图生视频/wan2_2_fun_vace_flfv_change_outfit_1983372948306337793.json
name: wan2_2_fun_vace_flfv_change_outfit_1983372948306337793.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1983372948306337793.json
hash: 7b8c97f9a5fead75
coverage: 0.54717
learned_at: 2026-10-15 22:32:44
nodes: [SetNode, GetNode, SetNode, CLIPTextEncode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, Label (rgthree), Label (rgthree), Label (rgthree), ModelSamplingSD3, SetNode, SetNode, ModelSamplingSD3, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, Label (rgthree), SetNode, Label (rgthree), KSamplerAdvanced, Label (rgthree), GetNode, GetNode, Label (rgthree), SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, VAEDecode, GetImageSizeAndCount, GetNode, GetNode, easy forLoopEnd, GetNode, GetImageSizeAndCount, GetImageRangeFromBatch, VHS_VideoCombine, VHS_VideoCombine, GetNode, KSamplerAdvanced, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, LoraLoaderModelOnly, PreviewImage, WanVaceToVideo, easy showAnything, TrimVideoLatent, ImageResizeKJv2, SetNode, SetNode, easy forLoopStart, MathExpression|pysssss, GetNode, WanVideoVACEStartToEndFrame, KSamplerAdvanced, KSamplerAdvanced, TrimVideoLatent, GetImageRangeFromBatch, VAEDecode, GetNode, ImageBatchMulti, LoadImage, LoadImage, ImageBatchMulti, INTConstant, INTConstant, INTConstant, GetNode, GetNode, WanVaceToVideo, CLIPTextEncode, DiffusionModelSelector, DiffusionModelSelector, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ, CLIPLoader, VAELoader, LoraLoaderModelOnly, INTConstant, LoadImage, LoadImage, ImageResizeKJv2, ImageResizeKJv2, MaskPreview, WanVideoVACEStartToEndFrame, VHS_VideoCombine, GetImageRangeFromBatch, GetNode, MaskPreview, PreviewImage]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2_2_fun_vace_flfv_change_outfit_1983372948306337793.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1983372948306337793.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（106 个）：
- `SetNode`
- `GetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `ModelSamplingSD3`
- `SetNode`
- `SetNode`
- `ModelSamplingSD3`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `Label (rgthree)`
- `SetNode`
- `Label (rgthree)`
- `KSamplerAdvanced` ★核心
- `Label (rgthree)`
- `GetNode`
- `GetNode`
- `Label (rgthree)`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `easy forLoopEnd`
- `GetNode`
- `GetImageSizeAndCount`
- `GetImageRangeFromBatch`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `WanVaceToVideo`
- `easy showAnything`
- `TrimVideoLatent`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `easy forLoopStart`
- `MathExpression|pysssss`
- `GetNode`
- `WanVideoVACEStartToEndFrame`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `TrimVideoLatent`
- `GetImageRangeFromBatch`
- `VAEDecode` ★核心
- `GetNode`
- `ImageBatchMulti`
- `LoadImage`
- `LoadImage`
- `ImageBatchMulti`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `WanVaceToVideo`
- `CLIPTextEncode` ★核心
- `DiffusionModelSelector`
- `DiffusionModelSelector`
- `DiffusionModelLoaderKJ`
- `DiffusionModelLoaderKJ`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `LoadImage`
- `LoadImage`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `MaskPreview`
- `WanVideoVACEStartToEndFrame`
- `VHS_VideoCombine`
- `GetImageRangeFromBatch`
- `GetNode`
- `MaskPreview`
- `PreviewImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **55%**（58/106）

**有卡**：`CLIPTextEncode`、`Label (rgthree)`、`ModelSamplingSD3`、`KSamplerAdvanced`、`VAEDecode`、`GetImageSizeAndCount`、`easy forLoopEnd`、`GetImageRangeFromBatch`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`WanVaceToVideo`、`TrimVideoLatent`、`ImageResizeKJv2`、`easy forLoopStart`、`MathExpression|pysssss`、`WanVideoVACEStartToEndFrame`、`ImageBatchMulti`、`LoadImage`、`INTConstant`、`DiffusionModelSelector`、`DiffusionModelLoaderKJ`、`CLIPLoader`、`VAELoader`、`MaskPreview`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、TrimVideoLatent
