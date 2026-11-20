---
key: 平台全量/Wan2.2视频换背景&换人_2027288927790436353.json
name: Wan2.2视频换背景&换人_2027288927790436353
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2视频换背景&换人_2027288927790436353.json
hash: 07428056c6b6f43e
coverage: 0.90625
learned_at: 2026-11-14 01:06:25
nodes: [easy cleanGpuUsed, easy cleanGpuUsed, CLIPTextEncode, CLIPTextEncode, WanVideoTextEmbedBridge, WanVideoSampler, ImageStitch, ImageStitch, VHS_VideoCombine, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoSampler, VHS_VideoCombine, VHS_VideoCombine, WanVideoDecode, SimpleMath+, INTConstant, INTConstant, INTConstant, PrimitiveNode, ImpactMinMax, Reroute, Florence2Run, Sam2Segmentation, GetImageSizeAndCount, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, SeedVR2TorchCompileSettings, VHS_VideoCombine, SeedVR2LoadVAEModel, InpaintPreprocessor, WanVideoVACEEncode, WanVideoTorchCompileSettings, WanVideoBlockSwap, SetNode, WanVideoVACEModelSelect, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoSetBlockSwap, CLIPLoader, DownloadAndLoadSAM2Model, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, SetNode, WanVideoLoraSelectMulti, WanVideoVAELoader, CR Prompt Text, FloatConstant, Float to Int, DownloadAndLoadFlorence2Model, Florence2toCoordinates, VHS_LoadVideo, PrimitiveString, GrowMaskWithBlur, ImageResizeKJv2, LoadImage, INTConstant, WanVideoContextOptions, Fast Groups Bypasser (rgthree), INTConstant, ImageResizeKJv2]
patterns: []
missing: []
---

# 平台全量/Wan2.2视频换背景&换人_2027288927790436353.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2视频换背景&换人_2027288927790436353.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（64 个）：
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanVideoTextEmbedBridge`
- `WanVideoSampler` ★核心
- `ImageStitch`
- `ImageStitch`
- `VHS_VideoCombine`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `SimpleMath+`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `PrimitiveNode`
- `ImpactMinMax`
- `Reroute`
- `Florence2Run`
- `Sam2Segmentation`
- `GetImageSizeAndCount`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `SeedVR2TorchCompileSettings`
- `VHS_VideoCombine`
- `SeedVR2LoadVAEModel`
- `InpaintPreprocessor`
- `WanVideoVACEEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `SetNode`
- `WanVideoVACEModelSelect`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `CLIPLoader`
- `DownloadAndLoadSAM2Model`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `CR Prompt Text`
- `FloatConstant`
- `Float to Int`
- `DownloadAndLoadFlorence2Model`
- `Florence2toCoordinates`
- `VHS_LoadVideo`
- `PrimitiveString`
- `GrowMaskWithBlur`
- `ImageResizeKJv2`
- `LoadImage`
- `INTConstant`
- `WanVideoContextOptions`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `ImageResizeKJv2`

## 知识

覆盖率 **91%**（58/64）

**有卡**：`easy cleanGpuUsed`、`CLIPTextEncode`、`WanVideoTextEmbedBridge`、`WanVideoSampler`、`ImageStitch`、`VHS_VideoCombine`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoDecode`、`SimpleMath+`、`INTConstant`、`ImpactMinMax`、`Florence2Run`、`Sam2Segmentation`、`GetImageSizeAndCount`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`SeedVR2TorchCompileSettings`、`SeedVR2LoadVAEModel`、`InpaintPreprocessor`、`WanVideoVACEEncode`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoVACEModelSelect`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`CLIPLoader`、`DownloadAndLoadSAM2Model`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`CR Prompt Text`、`FloatConstant`、`Float to Int`、`DownloadAndLoadFlorence2Model`、`Florence2toCoordinates`、`VHS_LoadVideo`、`GrowMaskWithBlur`、`ImageResizeKJv2`、`LoadImage`、`WanVideoContextOptions`

**用到的条目**：CLIPLoader、CLIPTextEncode、LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2TorchCompileSettings、SeedVR2VideoUpscaler、WanVideoSampler
