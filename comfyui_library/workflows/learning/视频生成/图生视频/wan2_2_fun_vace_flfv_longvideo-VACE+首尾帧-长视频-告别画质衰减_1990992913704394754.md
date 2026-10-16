---
key: 视频生成/图生视频/wan2_2_fun_vace_flfv_longvideo-VACE+首尾帧-长视频-告别画质衰减_1990992913704394754.json
name: wan2_2_fun_vace_flfv_longvideo-VACE+首尾帧-长视频-告别画质衰减_1990992913704394754.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1990992913704394754.json
hash: a0bb9a3a0595b50d
coverage: 0.519608
learned_at: 2026-10-15 22:33:12
nodes: [SetNode, GetNode, SetNode, CLIPTextEncode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, VAELoader, ModelSamplingSD3, SetNode, SetNode, DiffusionModelSelector, ModelSamplingSD3, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, CLIPLoader, KSamplerAdvanced, easy showAnything, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, WanVaceToVideo, GetNode, GetImageSizeAndCount, ImageResizeKJv2, GetNode, GetNode, GetNode, KSamplerAdvanced, easy forLoopStart, GetNode, GetImageSizeAndCount, KSamplerAdvanced, ImageBatchMulti, MathExpression|pysssss, GetImageRangeFromBatch, GetNode, VAEDecode, GetImageRangeFromBatch, DiffusionModelSelector, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, WanVideoVACEStartToEndFrame, WanVaceToVideo, GetNode, GetNode, TrimVideoLatent, TrimVideoLatent, GetNode, CLIPTextEncode, PreviewImage, MaskPreview, GetNode, CLIPTextEncode, ImageBatchMulti, KSamplerAdvanced, WanVideoVACEStartToEndFrame, PreviewImage, MaskPreview, GetNode, GetNode, ImageResizeKJv2, GetNode, GetNode, GetNode, GetImageRangeFromBatch, easy forLoopEnd, LoadImage, VHS_VideoCombine, VAEDecode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, ImageResizeKJv2, LoadImage, LoadImage, LoadImage, LoadImage, Int, Int, Int, Int]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2_2_fun_vace_flfv_longvideo-VACE+首尾帧-长视频-告别画质衰减_1990992913704394754.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1990992913704394754.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（102 个）：
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
- `VAELoader`
- `ModelSamplingSD3`
- `SetNode`
- `SetNode`
- `DiffusionModelSelector`
- `ModelSamplingSD3`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `easy showAnything`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVaceToVideo`
- `GetNode`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `easy forLoopStart`
- `GetNode`
- `GetImageSizeAndCount`
- `KSamplerAdvanced` ★核心
- `ImageBatchMulti`
- `MathExpression|pysssss`
- `GetImageRangeFromBatch`
- `GetNode`
- `VAEDecode` ★核心
- `GetImageRangeFromBatch`
- `DiffusionModelSelector`
- `DiffusionModelLoaderKJ`
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `WanVideoVACEStartToEndFrame`
- `WanVaceToVideo`
- `GetNode`
- `GetNode`
- `TrimVideoLatent`
- `TrimVideoLatent`
- `GetNode`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `MaskPreview`
- `GetNode`
- `CLIPTextEncode` ★核心
- `ImageBatchMulti`
- `KSamplerAdvanced` ★核心
- `WanVideoVACEStartToEndFrame`
- `PreviewImage`
- `MaskPreview`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `easy forLoopEnd`
- `LoadImage`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Int`
- `Int`
- `Int`
- `Int`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **52%**（53/102）

**有卡**：`CLIPTextEncode`、`VAELoader`、`ModelSamplingSD3`、`DiffusionModelSelector`、`CLIPLoader`、`KSamplerAdvanced`、`WanVaceToVideo`、`GetImageSizeAndCount`、`ImageResizeKJv2`、`easy forLoopStart`、`ImageBatchMulti`、`MathExpression|pysssss`、`GetImageRangeFromBatch`、`VAEDecode`、`DiffusionModelLoaderKJ`、`LoraLoaderModelOnly`、`WanVideoVACEStartToEndFrame`、`TrimVideoLatent`、`MaskPreview`、`easy forLoopEnd`、`LoadImage`、`VHS_VideoCombine`、`Int`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、TrimVideoLatent
