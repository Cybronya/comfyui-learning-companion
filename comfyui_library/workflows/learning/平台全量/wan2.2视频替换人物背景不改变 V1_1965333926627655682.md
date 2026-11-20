---
key: 平台全量/wan2.2视频替换人物背景不改变 V1_1965333926627655682.json
name: wan2.2视频替换人物背景不改变 V1_1965333926627655682
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2视频替换人物背景不改变 V1_1965333926627655682.json
hash: be534a3f50e66a0a
coverage: 0.956522
learned_at: 2026-11-14 01:19:56
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, easy cleanGpuUsed, WanVideoSetLoRAs, AIO_Preprocessor, ImageResizeKJv2, GrowMaskWithBlur, easy cleanGpuUsed, CR Text Concatenate, CLIPTextEncode, CLIPTextEncode, LoadImage, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoCombine, RHHiddenNodes, InspyrenetRembgAdvanced, InspyrenetRembgAdvanced, LayerUtility: ImageRemoveAlpha, RHHiddenNodes, easy cleanGpuUsed, ImageStitch, ImageResizeKJv2, GetImageSizeAndCount, RHHiddenNodes, ImageResizeKJv2, WanVideoSetBlockSwap, LayerMask: SegmentAnythingUltra V2, WanVideoDecode, WanVideoBlockSwap, CLIPLoader, WanVideoTorchCompileSettings, WanVideoVAELoader, Florence2Run, WanVideoSampler, WanVideoTextEmbedBridge, WanVideoSampler, CR Prompt Text, ShowText|pysssss, PrimitiveNode, INTConstant, INTConstant, INTConstant, intToFloat _O, WanVideoEnhanceAVideo, Florence2ModelLoader]
patterns: []
missing: []
---

# 平台全量/wan2.2视频替换人物背景不改变 V1_1965333926627655682.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2视频替换人物背景不改变 V1_1965333926627655682.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（46 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `easy cleanGpuUsed`
- `WanVideoSetLoRAs`
- `AIO_Preprocessor`
- `ImageResizeKJv2`
- `GrowMaskWithBlur`
- `easy cleanGpuUsed`
- `CR Text Concatenate`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `RHHiddenNodes`
- `InspyrenetRembgAdvanced`
- `InspyrenetRembgAdvanced`
- `LayerUtility: ImageRemoveAlpha`
- `RHHiddenNodes`
- `easy cleanGpuUsed`
- `ImageStitch`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `RHHiddenNodes`
- `ImageResizeKJv2`
- `WanVideoSetBlockSwap`
- `LayerMask: SegmentAnythingUltra V2`
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `CLIPLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `Florence2Run`
- `WanVideoSampler` ★核心
- `WanVideoTextEmbedBridge`
- `WanVideoSampler` ★核心
- `CR Prompt Text`
- `ShowText|pysssss`
- `PrimitiveNode`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `intToFloat _O`
- `WanVideoEnhanceAVideo`
- `Florence2ModelLoader`

## 知识

覆盖率 **96%**（44/46）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`easy cleanGpuUsed`、`AIO_Preprocessor`、`ImageResizeKJv2`、`GrowMaskWithBlur`、`CR Text Concatenate`、`CLIPTextEncode`、`LoadImage`、`VHS_LoadVideo`、`VHS_VideoCombine`、`RHHiddenNodes`、`InspyrenetRembgAdvanced`、`LayerUtility: ImageRemoveAlpha`、`ImageStitch`、`GetImageSizeAndCount`、`LayerMask: SegmentAnythingUltra V2`、`WanVideoDecode`、`WanVideoBlockSwap`、`CLIPLoader`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`Florence2Run`、`WanVideoSampler`、`WanVideoTextEmbedBridge`、`CR Prompt Text`、`INTConstant`、`intToFloat _O`、`WanVideoEnhanceAVideo`、`Florence2ModelLoader`

**用到的条目**：CLIPLoader、CLIPTextEncode、LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoSetLoRAs、CR Prompt Text
