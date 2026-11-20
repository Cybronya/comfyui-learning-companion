---
key: 平台全量/wan2.2-动作迁移-Fun_control加速lora-4步极速-3种控制方式_1956575761157246978.json
name: wan2.2-动作迁移-Fun_control加速lora-4步极速-3种控制方式_1956575761157246978
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2-动作迁移-Fun_control加速lora-4步极速-3种控制方式_1956575761157246978.json
hash: 464b76707f679b03
coverage: 0.886364
learned_at: 2026-11-14 01:19:33
nodes: [WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSetLoRAs, DepthAnything_V2, AIO_Preprocessor, Canny, DownloadAndLoadDepthAnythingV2Model, ImageResizeKJv2, WanVideoEncode, WanVideoImageToVideoEncode, PrimitiveNode, PrimitiveNode, PrimitiveNode, PrimitiveNode, easy anythingIndexSwitch, WanVideoControlEmbeds, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSampler, WanVideoSampler, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine, GetImageSizeAndCount, SimpleMath+, GetImageRangeFromBatch, ImageConcanate, VHS_VideoCombine, ImageResizeKJv2, LoadImage, Note, VHS_LoadVideo, ImpactInt, WanVideoTextEncode, ImpactInt, ImpactInt, ImpactInt]
patterns: []
missing: []
---

# 平台全量/wan2.2-动作迁移-Fun_control加速lora-4步极速-3种控制方式_1956575761157246978.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2-动作迁移-Fun_control加速lora-4步极速-3种控制方式_1956575761157246978.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（44 个）：
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `DepthAnything_V2`
- `AIO_Preprocessor`
- `Canny`
- `DownloadAndLoadDepthAnythingV2Model`
- `ImageResizeKJv2`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveNode`
- `easy anythingIndexSwitch`
- `WanVideoControlEmbeds`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `SimpleMath+`
- `GetImageRangeFromBatch`
- `ImageConcanate`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `LoadImage`
- `Note`
- `VHS_LoadVideo`
- `ImpactInt`
- `WanVideoTextEncode`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`

## 知识

覆盖率 **89%**（39/44）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`DepthAnything_V2`、`AIO_Preprocessor`、`Canny`、`DownloadAndLoadDepthAnythingV2Model`、`ImageResizeKJv2`、`WanVideoEncode`、`WanVideoImageToVideoEncode`、`easy anythingIndexSwitch`、`WanVideoControlEmbeds`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`SimpleMath+`、`GetImageRangeFromBatch`、`ImageConcanate`、`LoadImage`、`VHS_LoadVideo`、`ImpactInt`、`WanVideoTextEncode`

**用到的条目**：LoadImage、Canny、DepthAnything_V2、DownloadAndLoadDepthAnythingV2Model、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode
