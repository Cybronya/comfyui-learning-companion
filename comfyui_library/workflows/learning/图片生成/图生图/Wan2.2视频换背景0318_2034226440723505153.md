---
key: 图片生成/图生图/Wan2.2视频换背景0318_2034226440723505153.json
name: Wan2.2视频换背景0318_2034226440723505153
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2视频换背景0318_2034226440723505153.json
hash: 52cbce4aaacc099d
coverage: 0.910256
learned_at: 2026-10-23 11:28:25
nodes: [easy cleanGpuUsed, easy cleanGpuUsed, CLIPTextEncode, CLIPTextEncode, WanVideoTextEmbedBridge, WanVideoSampler, ImageStitch, ImageStitch, VHS_VideoCombine, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoDecode, SimpleMath+, INTConstant, INTConstant, INTConstant, PrimitiveNode, ImpactMinMax, Florence2Run, SeedVR2LoadVAEModel, WanVideoTorchCompileSettings, WanVideoBlockSwap, SetNode, WanVideoVACEModelSelect, WanVideoVACEModelSelect, WanVideoSetLoRAs, WanVideoSetBlockSwap, CLIPLoader, DownloadAndLoadSAM2Model, WanVideoVAELoader, FloatConstant, DownloadAndLoadFlorence2Model, Florence2toCoordinates, PrimitiveString, ImageResizeKJv2, INTConstant, WanVideoContextOptions, Fast Groups Bypasser (rgthree), INTConstant, SAM3VideoModelLoader, SAM3Propagate, SAM3VideoOutput, GetImageSizeAndCount, SeedVR2VideoUpscaler, Mask Invert, SAM3VideoSegmentation, Reroute, MaskToImage, easy clearCacheAll, easy cleanGpuUsed, WanVideoSampler, InpaintPreprocessor, Float to Int, WanVideoSetBlockSwap, Sam2Segmentation, WanVideoSetLoRAs, SetNode, WanVideoLoraSelectMulti, SeedVR2LoadDiTModel, SeedVR2TorchCompileSettings, VHS_VideoCombine, ImageResizeKJv2, VHS_VideoCombine, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelectMulti, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, Reroute, WanVideoVACEEncode, GrowMaskWithBlur, MaskBlur+, InpaintCrop, CR Prompt Text, VHS_LoadVideo, LoadImage, SAM3PointCollector]
patterns: []
missing: []
---

# 图片生成/图生图/Wan2.2视频换背景0318_2034226440723505153.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2视频换背景0318_2034226440723505153.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（78 个）：
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
- `WanVideoDecode`
- `SimpleMath+`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `PrimitiveNode`
- `ImpactMinMax`
- `Florence2Run`
- `SeedVR2LoadVAEModel`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `SetNode`
- `WanVideoVACEModelSelect`
- `WanVideoVACEModelSelect`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `CLIPLoader`
- `DownloadAndLoadSAM2Model`
- `WanVideoVAELoader`
- `FloatConstant`
- `DownloadAndLoadFlorence2Model`
- `Florence2toCoordinates`
- `PrimitiveString`
- `ImageResizeKJv2`
- `INTConstant`
- `WanVideoContextOptions`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `SAM3VideoModelLoader`
- `SAM3Propagate`
- `SAM3VideoOutput`
- `GetImageSizeAndCount`
- `SeedVR2VideoUpscaler`
- `Mask Invert`
- `SAM3VideoSegmentation`
- `Reroute`
- `MaskToImage`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `InpaintPreprocessor`
- `Float to Int`
- `WanVideoSetBlockSwap`
- `Sam2Segmentation`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `SeedVR2LoadDiTModel`
- `SeedVR2TorchCompileSettings`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Reroute`
- `WanVideoVACEEncode`
- `GrowMaskWithBlur`
- `MaskBlur+`
- `InpaintCrop`
- `CR Prompt Text`
- `VHS_LoadVideo`
- `LoadImage`
- `SAM3PointCollector`

## 知识

覆盖率 **91%**（71/78）

**有卡**：`easy cleanGpuUsed`、`CLIPTextEncode`、`WanVideoTextEmbedBridge`、`WanVideoSampler`、`ImageStitch`、`VHS_VideoCombine`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoDecode`、`SimpleMath+`、`INTConstant`、`ImpactMinMax`、`Florence2Run`、`SeedVR2LoadVAEModel`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoVACEModelSelect`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`CLIPLoader`、`DownloadAndLoadSAM2Model`、`WanVideoVAELoader`、`FloatConstant`、`DownloadAndLoadFlorence2Model`、`Florence2toCoordinates`、`ImageResizeKJv2`、`WanVideoContextOptions`、`SAM3VideoModelLoader`、`SAM3Propagate`、`SAM3VideoOutput`、`GetImageSizeAndCount`、`SeedVR2VideoUpscaler`、`Mask Invert`、`SAM3VideoSegmentation`、`MaskToImage`、`easy clearCacheAll`、`InpaintPreprocessor`、`Float to Int`、`Sam2Segmentation`、`WanVideoLoraSelectMulti`、`SeedVR2LoadDiTModel`、`SeedVR2TorchCompileSettings`、`WanVideoModelLoader`、`WanVideoVACEEncode`、`GrowMaskWithBlur`、`MaskBlur+`、`InpaintCrop`、`CR Prompt Text`、`VHS_LoadVideo`、`LoadImage`、`SAM3PointCollector`

**用到的条目**：CLIPTextEncode、CLIPLoader、LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、WanVideoSampler、SeedVR2TorchCompileSettings
