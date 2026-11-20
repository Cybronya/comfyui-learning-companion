---
key: 平台全量/Wan2.1 最新图生视频_文生视频_姿势控制_1905489614994608130.json
name: Wan2.1 最新图生视频_文生视频_姿势控制_1905489614994608130
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1 最新图生视频_文生视频_姿势控制_1905489614994608130.json
hash: e2c96600fdd19326
coverage: 0.732558
learned_at: 2026-11-14 01:04:30
nodes: [WanVideoBlockSwap, ImageResizeKJv2, SetNode, EmptyImage, SetNode, PreviewImage, SetNode, ImpactMakeImageBatch, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoVACEEncode, WanVideoSampler, PreviewImage, WanVideoDecode, RH_Translator, INTConstant, INTConstant, INTConstant, SimpleMath+, LoadImage, CLIPTextEncode, UNETLoader, LoraLoaderModelOnly, TorchCompileModel, PathchSageAttentionKJ, ModelSamplingSD3, EmptyHunyuanLatentVideo, KSampler, VAEDecode, RIFE VFI, VHS_VideoCombine, VHS_VideoCombine, CLIPTextEncode, RH_Translator, VAELoader, CLIPLoader, SetNode, RMBG, VHS_LoadVideo, ImageResizeKJ, OpenposePreprocessor, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoVACEModelSelect, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoVACEModelSelect, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoSampler, WanVideoDecode, WanVideoVACEEncode, WanVideoEnhanceAVideo, WanVideoModelLoader, GetNode, INTConstant, INTConstant, ImageResizeKJv2, PreviewImage, SetNode, SetNode, ImageResizeKJ, VHS_VideoCombine, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, WanVideoLoraSelect, LoadImage, VHS_VideoCombine, INTConstant, WanVideoTextEncode, WanVideoModelLoader, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoTeaCache, WanVideoExperimentalArgs, WanVideoTorchCompileSettings]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 0, "steps": 10}
---

# 平台全量/Wan2.1 最新图生视频_文生视频_姿势控制_1905489614994608130.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1 最新图生视频_文生视频_姿势控制_1905489614994608130.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（86 个）：
- `WanVideoBlockSwap`
- `ImageResizeKJv2`
- `SetNode`
- `EmptyImage`
- `SetNode`
- `PreviewImage`
- `SetNode`
- `ImpactMakeImageBatch`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoVACEEncode`
- `WanVideoSampler` ★核心
- `PreviewImage`
- `WanVideoDecode`
- `RH_Translator`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `SimpleMath+`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `TorchCompileModel`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `EmptyHunyuanLatentVideo`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `RIFE VFI`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `RH_Translator`
- `VAELoader`
- `CLIPLoader`
- `SetNode`
- `RMBG`
- `VHS_LoadVideo`
- `ImageResizeKJ`
- `OpenposePreprocessor`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoVACEModelSelect`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoVACEEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoModelLoader`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJv2`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `ImageResizeKJ`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoLoraSelect`
- `LoadImage`
- `VHS_VideoCombine`
- `INTConstant`
- `WanVideoTextEncode`
- `WanVideoModelLoader`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoTeaCache`
- `WanVideoExperimentalArgs`
- `WanVideoTorchCompileSettings`

## 关键参数

- `seed` = `0`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **73%**（63/86）

**有卡**：`WanVideoBlockSwap`、`ImageResizeKJv2`、`EmptyImage`、`ImpactMakeImageBatch`、`WanVideoVACEEncode`、`WanVideoSampler`、`WanVideoDecode`、`RH_Translator`、`INTConstant`、`SimpleMath+`、`LoadImage`、`CLIPTextEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`TorchCompileModel`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`EmptyHunyuanLatentVideo`、`KSampler`、`VAEDecode`、`RIFE VFI`、`VHS_VideoCombine`、`VAELoader`、`CLIPLoader`、`RMBG`、`VHS_LoadVideo`、`ImageResizeKJ`、`OpenposePreprocessor`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoVACEModelSelect`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`WanVideoEnhanceAVideo`、`WanVideoModelLoader`、`WanVideoSLG`、`WanVideoTeaCache`、`WanVideoExperimentalArgs`、`WanVideoTorchCompileSettings`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader
