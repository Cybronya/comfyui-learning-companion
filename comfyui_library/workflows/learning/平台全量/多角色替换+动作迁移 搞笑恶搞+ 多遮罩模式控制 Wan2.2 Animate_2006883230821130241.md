---
key: 平台全量/多角色替换+动作迁移 搞笑恶搞+ 多遮罩模式控制 Wan2.2 Animate_2006883230821130241.json
name: 多角色替换+动作迁移 搞笑恶搞+ 多遮罩模式控制 Wan2.2 Animate_2006883230821130241
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/多角色替换+动作迁移 搞笑恶搞+ 多遮罩模式控制 Wan2.2 Animate_2006883230821130241.json
hash: 484e94e62d1b46c7
coverage: 0.956522
learned_at: 2026-11-14 01:58:16
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, easy cleanGpuUsed, WanVideoSetLoRAs, AIO_Preprocessor, ImageResizeKJv2, GrowMaskWithBlur, easy cleanGpuUsed, CR Text Concatenate, CLIPTextEncode, CLIPTextEncode, VHS_VideoCombine, VHS_VideoCombine, RHHiddenNodes, InspyrenetRembgAdvanced, InspyrenetRembgAdvanced, LayerUtility: ImageRemoveAlpha, RHHiddenNodes, easy cleanGpuUsed, ImageStitch, ImageResizeKJv2, GetImageSizeAndCount, RHHiddenNodes, ImageResizeKJv2, WanVideoSetBlockSwap, LayerMask: SegmentAnythingUltra V2, WanVideoDecode, WanVideoBlockSwap, CLIPLoader, WanVideoTorchCompileSettings, WanVideoVAELoader, Florence2Run, WanVideoSampler, WanVideoTextEmbedBridge, WanVideoSampler, CR Prompt Text, ShowText|pysssss, PrimitiveNode, INTConstant, INTConstant, INTConstant, intToFloat _O, WanVideoEnhanceAVideo, Florence2ModelLoader, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 平台全量/多角色替换+动作迁移 搞笑恶搞+ 多遮罩模式控制 Wan2.2 Animate_2006883230821130241.json

> 来源文件 `comfyui_library/workflows/平台全量/多角色替换+动作迁移 搞笑恶搞+ 多遮罩模式控制 Wan2.2 Animate_2006883230821130241.json`

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
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **96%**（44/46）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`easy cleanGpuUsed`、`AIO_Preprocessor`、`ImageResizeKJv2`、`GrowMaskWithBlur`、`CR Text Concatenate`、`CLIPTextEncode`、`VHS_VideoCombine`、`RHHiddenNodes`、`InspyrenetRembgAdvanced`、`LayerUtility: ImageRemoveAlpha`、`ImageStitch`、`GetImageSizeAndCount`、`LayerMask: SegmentAnythingUltra V2`、`WanVideoDecode`、`WanVideoBlockSwap`、`CLIPLoader`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`Florence2Run`、`WanVideoSampler`、`WanVideoTextEmbedBridge`、`CR Prompt Text`、`INTConstant`、`intToFloat _O`、`WanVideoEnhanceAVideo`、`Florence2ModelLoader`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：CLIPLoader、CLIPTextEncode、LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoSetLoRAs、CR Prompt Text
