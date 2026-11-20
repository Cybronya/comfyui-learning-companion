---
key: 平台全量/啊！AI在疯狂模仿JYP顶胯？Wan2.2 VACE Fun初体验！_1968615329893109761.json
name: 啊！AI在疯狂模仿JYP顶胯？Wan2.2 VACE Fun初体验！_1968615329893109761
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/啊！AI在疯狂模仿JYP顶胯？Wan2.2 VACE Fun初体验！_1968615329893109761.json
hash: aa259323f0dd9fc6
coverage: 0.774194
learned_at: 2026-11-14 01:52:52
nodes: [WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoScheduler, StringToFloatList, WanVideoLoraSelect, WanVideoExtraModelSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoExtraModelSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoScheduler, Bjornulf_ShowInt, CLIPLoader, SetNode, CLIPTextEncode, WanVideoVAELoader, GetNode, SetNode, GetImageSizeAndCount, GetNode, SetNode, WanVideoSetLoRAs, GetNode, WanVideoSetLoRAs, SetNode, GetNode, WanVideoDecode, SetNode, WanVideoTextEmbedBridge, INTConstant, StringToFloatList, WanVideoSigmaToStep, FloatConstant, GetNode, ImageResizeKJv2, VHS_VideoCombine, DWPreprocessor, WanVideoSampler, WanVideoVACEEncode, SetNode, GetNode, VHS_VideoCombine, DownloadAndLoadSAM2Model, Sam2Segmentation, ImageResizeKJv2, GetImageRangeFromBatch, VHS_VideoCombine, MaskToImage, GrowMaskWithBlur, Mix Color By Mask, Reroute, VHS_LoadVideo, PointsEditor, LoadImage, ImageResizeKJv2, PreviewImage, CLIPTextEncode, WanVideoSampler, Label (rgthree)]
patterns: []
missing: []
---

# 平台全量/啊！AI在疯狂模仿JYP顶胯？Wan2.2 VACE Fun初体验！_1968615329893109761.json

> 来源文件 `comfyui_library/workflows/平台全量/啊！AI在疯狂模仿JYP顶胯？Wan2.2 VACE Fun初体验！_1968615329893109761.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（62 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoScheduler`
- `StringToFloatList`
- `WanVideoLoraSelect`
- `WanVideoExtraModelSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoExtraModelSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoScheduler`
- `Bjornulf_ShowInt`
- `CLIPLoader`
- `SetNode`
- `CLIPTextEncode` ★核心
- `WanVideoVAELoader`
- `GetNode`
- `SetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `SetNode`
- `WanVideoSetLoRAs`
- `GetNode`
- `WanVideoSetLoRAs`
- `SetNode`
- `GetNode`
- `WanVideoDecode`
- `SetNode`
- `WanVideoTextEmbedBridge`
- `INTConstant`
- `StringToFloatList`
- `WanVideoSigmaToStep`
- `FloatConstant`
- `GetNode`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `DWPreprocessor`
- `WanVideoSampler` ★核心
- `WanVideoVACEEncode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `DownloadAndLoadSAM2Model`
- `Sam2Segmentation`
- `ImageResizeKJv2`
- `GetImageRangeFromBatch`
- `VHS_VideoCombine`
- `MaskToImage`
- `GrowMaskWithBlur`
- `Mix Color By Mask`
- `Reroute`
- `VHS_LoadVideo`
- `PointsEditor`
- `LoadImage`
- `ImageResizeKJv2`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `WanVideoSampler` ★核心
- `Label (rgthree)`

## 知识

覆盖率 **77%**（48/62）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoScheduler`、`StringToFloatList`、`WanVideoLoraSelect`、`WanVideoExtraModelSelect`、`WanVideoModelLoader`、`Bjornulf_ShowInt`、`CLIPLoader`、`CLIPTextEncode`、`WanVideoVAELoader`、`GetImageSizeAndCount`、`WanVideoSetLoRAs`、`WanVideoDecode`、`WanVideoTextEmbedBridge`、`INTConstant`、`WanVideoSigmaToStep`、`FloatConstant`、`ImageResizeKJv2`、`VHS_VideoCombine`、`DWPreprocessor`、`WanVideoSampler`、`WanVideoVACEEncode`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`GetImageRangeFromBatch`、`MaskToImage`、`GrowMaskWithBlur`、`Mix Color By Mask`、`VHS_LoadVideo`、`PointsEditor`、`LoadImage`、`Label (rgthree)`

**用到的条目**：CLIPLoader、CLIPTextEncode、LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelect
