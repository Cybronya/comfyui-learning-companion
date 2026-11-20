---
key: 平台全量/跳舞模仿 wan2.2vace动作迁移_1967563554511556610.json
name: 跳舞模仿 wan2.2vace动作迁移_1967563554511556610
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/跳舞模仿 wan2.2vace动作迁移_1967563554511556610.json
hash: 12d506d9cfa6e5e4
coverage: 0.8
learned_at: 2026-11-14 02:47:27
nodes: [easy cleanGpuUsed, RH_Captioner, WanVideoVAELoader, WanVideoTeaCache, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoModelLoader, GetNode, Reroute, easy showAnything, easy showAnything, easy showAnything, easy showAnything, PixelPerfectResolution, AIO_Preprocessor, GetImageSizeAndCount, WanVideoSetBlockSwap, SetNode, Text Concatenate, WanVideoSLG, WanVideoTextEncode, LoadWanVideoT5TextEncoder, VHS_VideoCombine, PathchSageAttentionKJ, VAEEncode, VAEDecode, GetImageSizeAndCount, UNETLoader, LoraLoaderModelOnly, ModelSamplingSD3, VAELoader, WanVideoDecode, LoraLoaderModelOnly, CLIPLoader, VHS_VideoCombine, VHS_VideoCombine, Reroute, GetImageSizeAndCount, ImageFromBatch+, ImageResize+, ImageResize+, VHS_VideoCombine, WanVideoSampler, AddLabel, AddLabel, WanVideoLoraSelectMulti, WanVideoLoraSelect, Text Multiline, ApplyFaceProcessor, ImageResizeKJv2, easy imageRemBg, WanVideoEncode, FaceProcessorLoader, WanVideoVACEEncode, WanVideoAddStandInLatent, ImageResize+, GetNode, MathExpression|pysssss, Note, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, Note, Note, Note, Note, CLIPTextEncode, CLIPTextEncode, Note, Note, LoadImage, VHS_LoadVideo, ClownsharKSampler_Beta, EmptyImage, Int, Int, Int, Int, ImageResize+, ImageConcatMulti, ImageConcatMulti]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": 3.0000000000000004, "sampler_name": -1, "scheduler": 0.30000000000000004, "seed": 0.5, "steps": "beta57"}
---

# 平台全量/跳舞模仿 wan2.2vace动作迁移_1967563554511556610.json

> 来源文件 `comfyui_library/workflows/平台全量/跳舞模仿 wan2.2vace动作迁移_1967563554511556610.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（80 个）：
- `easy cleanGpuUsed`
- `RH_Captioner`
- `WanVideoVAELoader`
- `WanVideoTeaCache`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `GetNode`
- `Reroute`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `PixelPerfectResolution`
- `AIO_Preprocessor`
- `GetImageSizeAndCount`
- `WanVideoSetBlockSwap`
- `SetNode`
- `Text Concatenate`
- `WanVideoSLG`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `PathchSageAttentionKJ`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `GetImageSizeAndCount`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `VAELoader`
- `WanVideoDecode`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Reroute`
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `ImageResize+`
- `ImageResize+`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `AddLabel`
- `AddLabel`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelect`
- `Text Multiline`
- `ApplyFaceProcessor`
- `ImageResizeKJv2`
- `easy imageRemBg`
- `WanVideoEncode`
- `FaceProcessorLoader`
- `WanVideoVACEEncode`
- `WanVideoAddStandInLatent`
- `ImageResize+`
- `GetNode`
- `MathExpression|pysssss`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `Note`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `LoadImage`
- `VHS_LoadVideo`
- `ClownsharKSampler_Beta` ★核心
- `EmptyImage`
- `Int`
- `Int`
- `Int`
- `Int`
- `ImageResize+`
- `ImageConcatMulti`
- `ImageConcatMulti`

## 关键参数

- `seed` = `0.5`
- `steps` = `beta57`
- `cfg` = `4`
- `sampler_name` = `-1`
- `scheduler` = `0.30000000000000004`
- `denoise` = `3.0000000000000004`

## 知识

覆盖率 **80%**（64/80）

**有卡**：`easy cleanGpuUsed`、`RH_Captioner`、`WanVideoVAELoader`、`WanVideoTeaCache`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`PixelPerfectResolution`、`AIO_Preprocessor`、`GetImageSizeAndCount`、`WanVideoSetBlockSwap`、`Text Concatenate`、`WanVideoSLG`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`VHS_VideoCombine`、`PathchSageAttentionKJ`、`VAEEncode`、`VAEDecode`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`VAELoader`、`WanVideoDecode`、`CLIPLoader`、`ImageFromBatch+`、`ImageResize+`、`WanVideoSampler`、`AddLabel`、`WanVideoLoraSelectMulti`、`WanVideoLoraSelect`、`Text Multiline`、`ApplyFaceProcessor`、`ImageResizeKJv2`、`easy imageRemBg`、`WanVideoEncode`、`FaceProcessorLoader`、`WanVideoVACEEncode`、`WanVideoAddStandInLatent`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`LoadImage`、`VHS_LoadVideo`、`ClownsharKSampler_Beta`、`EmptyImage`、`Int`、`ImageConcatMulti`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、LoadImage、UNETLoader
