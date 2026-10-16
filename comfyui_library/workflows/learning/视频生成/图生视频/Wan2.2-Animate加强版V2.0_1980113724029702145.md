---
key: 视频生成/图生视频/Wan2.2-Animate加强版V2.0_1980113724029702145.json
name: Wan2.2-Animate加强版V2.0_1980113724029702145.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1980113724029702145.json
hash: 608f7e2ef4f35824
coverage: 0.428571
learned_at: 2026-10-15 22:32:27
nodes: [BlockifyMask, SetNode, SetNode, ImageBlend, SetNode, SetNode, SetNode, SetNode, SetNode, Int, SetNode, SetNode, PoseAndFaceDetection, DrawViTPose, SetNode, VHS_VideoCombine, GetNode, RIFE VFI, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageConcatMulti, ImageConcatMulti, WanVideoDecode, GetNode, ImageFromBatch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, VHS_VideoCombine, SetNode, GetNode, SetNode, SetNode, SetNode, GetNode, SetNode, RemBGSession+, GrowMask, DrawMaskOnImage, GetNode, GetNode, VHS_VideoCombine, GetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, GetNode, GetNode, Note, MathExpression|pysssss, GetNode, ImpactInt, GetNode, OnnxDetectionModelLoader, GetNode, GetNode, WanVideoAnimateEmbeds, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, easy positive, MarkdownNote, ImpactInt, WanVideoVAELoader, CLIPVisionLoader, WanVideoTextEncodeCached, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, WanVideoModelLoader, WanVideoSampler, ImageRemoveBackground+, GetNode, Note, WanVideoLoraSelectMulti, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-Animate加强版V2.0_1980113724029702145.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1980113724029702145.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（98 个）：
- `BlockifyMask`
- `SetNode`
- `SetNode`
- `ImageBlend`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Int`
- `SetNode`
- `SetNode`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `RIFE VFI`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `WanVideoDecode`
- `GetNode`
- `ImageFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `RemBGSession+`
- `GrowMask`
- `DrawMaskOnImage`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `SetNode`
- `GetNode`
- `GetNode`
- `Note`
- `MathExpression|pysssss`
- `GetNode`
- `ImpactInt`
- `GetNode`
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `easy positive`
- `MarkdownNote`
- `ImpactInt`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoTextEncodeCached`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `ImageRemoveBackground+`
- `GetNode`
- `Note`
- `WanVideoLoraSelectMulti`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **43%**（42/98）

**有卡**：`BlockifyMask`、`ImageBlend`、`Int`、`PoseAndFaceDetection`、`DrawViTPose`、`VHS_VideoCombine`、`RIFE VFI`、`ImageConcatMulti`、`WanVideoDecode`、`ImageFromBatch`、`WanVideoClipVisionEncode`、`RemBGSession+`、`GrowMask`、`DrawMaskOnImage`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`MathExpression|pysssss`、`ImpactInt`、`OnnxDetectionModelLoader`、`WanVideoAnimateEmbeds`、`easy positive`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoTextEncodeCached`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoModelLoader`、`WanVideoSampler`、`ImageRemoveBackground+`、`WanVideoLoraSelectMulti`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs
