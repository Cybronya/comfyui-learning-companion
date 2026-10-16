---
key: 视频生成/图生视频/wan2.2 fun vace 多帧视频生成_1967643220417142786.json
name: wan2.2 fun vace 多帧视频生成_1967643220417142786.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1967643220417142786.json
hash: 0496e7a6ff3965a6
coverage: 0.913043
learned_at: 2026-10-15 22:31:42
nodes: [LoadImage, LoadImage, CLIPTextEncode, LoadImage, CLIPTextEncode, VAEDecode, TrimVideoLatent, DiffusionModelLoaderKJ, DiffusionModelLoaderKJ, CLIPLoader, DiffusionModelSelector, ImageResizeKJ, ImageResizeKJ, ImageResizeKJ, easy batchAnything, ImageResizeKJ, WanVideoVACEStartToEndFrame, MathExpression|pysssss, VHS_GetImageCount, GetImageRangeFromBatch, MathExpression|pysssss, VHS_GetImageCount, GetImageRangeFromBatch, easy batchAnything, WanVaceToVideo, WanVideoVACEStartToEndFrame, MathExpression|pysssss, easy batchAnything, easy batchAnything, Int, Switch, VHS_GetMaskCount, easy showAnything, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, PathchSageAttentionKJ, DiffusionModelSelector, VHS_VideoCombine, PreviewImage, Switch, Switch, easy cleanGpuUsed, LayerUtility: ImageScaleByAspectRatio V2, SelectImageBatch, MathExpression|pysssss, SelectImageBatch, easy showAnything, easy imageCount, PreviewImage, MathExpression|pysssss, WanVideoVACEStartToEndFrame, WanVideoVACEStartToEndFrame, Reroute, Reroute, VAELoader, ModelSamplingSD3, VHS_VideoCombine, LoadImage, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, TextInput_, Int, Int, easy int, Int, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 3.5, "scheduler": "lcm", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2 fun vace 多帧视频生成_1967643220417142786.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1967643220417142786.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `DiffusionModelLoaderKJ`
- `DiffusionModelLoaderKJ`
- `CLIPLoader`
- `DiffusionModelSelector`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `easy batchAnything`
- `ImageResizeKJ`
- `WanVideoVACEStartToEndFrame`
- `MathExpression|pysssss`
- `VHS_GetImageCount`
- `GetImageRangeFromBatch`
- `MathExpression|pysssss`
- `VHS_GetImageCount`
- `GetImageRangeFromBatch`
- `easy batchAnything`
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`
- `MathExpression|pysssss`
- `easy batchAnything`
- `easy batchAnything`
- `Int`
- `Switch`
- `VHS_GetMaskCount`
- `easy showAnything`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `DiffusionModelSelector`
- `VHS_VideoCombine`
- `PreviewImage`
- `Switch`
- `Switch`
- `easy cleanGpuUsed`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SelectImageBatch`
- `MathExpression|pysssss`
- `SelectImageBatch`
- `easy showAnything`
- `easy imageCount`
- `PreviewImage`
- `MathExpression|pysssss`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVACEStartToEndFrame`
- `Reroute`
- `Reroute`
- `VAELoader`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `LoadImage`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `TextInput_`
- `Int`
- `Int`
- `easy int`
- `Int`
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `3.5`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **91%**（63/69）

**有卡**：`LoadImage`、`CLIPTextEncode`、`VAEDecode`、`TrimVideoLatent`、`DiffusionModelLoaderKJ`、`CLIPLoader`、`DiffusionModelSelector`、`ImageResizeKJ`、`easy batchAnything`、`WanVideoVACEStartToEndFrame`、`MathExpression|pysssss`、`VHS_GetImageCount`、`GetImageRangeFromBatch`、`WanVaceToVideo`、`Int`、`Switch`、`VHS_GetMaskCount`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`VHS_VideoCombine`、`easy cleanGpuUsed`、`LayerUtility: ImageScaleByAspectRatio V2`、`SelectImageBatch`、`easy imageCount`、`VAELoader`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`TextInput_`、`easy int`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
