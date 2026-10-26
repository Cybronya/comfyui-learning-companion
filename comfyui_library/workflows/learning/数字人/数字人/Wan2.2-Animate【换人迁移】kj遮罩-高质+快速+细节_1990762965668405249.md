---
key: 数字人/数字人/Wan2.2-Animate【换人迁移】kj遮罩-高质+快速+细节_1990762965668405249.json
name: Wan2.2-Animate【换人迁移】kj遮罩-高质+快速+细节_1990762965668405249
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.2-Animate【换人迁移】kj遮罩-高质+快速+细节_1990762965668405249.json
hash: b69f7d9c52710ac5
coverage: 0.380952
learned_at: 2026-10-26 01:57:55
nodes: [DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, PreviewImage, ImageResizeKJv2, DrawViTPose, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSetBlockSwap, SetNode, SetNode, Note, GetNode, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoTorchCompileSettings, SetNode, SetNode, SetNode, GetNode, ImageRemoveBackground+, GrowMask, ImageBlend, DrawMaskOnImage, BlockifyMask, VHS_VideoCombine, SetNode, PoseAndFaceDetection, SetNode, ImageConcatMulti, ImageConcatMulti, GetNode, GetImageSizeAndCount, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Seed (rgthree), SetNode, SetNode, PrimitiveStringMultiline, WanVideoSampler, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, WanVideoClipVisionEncode, WanVideoDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Note, WanVideoAnimateEmbeds, GetNode, GetNode, SetNode, GetNode, PreviewImage, PreviewImage, Note, Note, Note, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, OnnxDetectionModelLoader, RemBGSession+, INTConstant, INTConstant, Fast Groups Bypasser (rgthree), SetNode, SetNode, WanVideoVAELoader, CLIPVisionLoader, WanVideoTextEncodeCached, WanVideoModelLoader, INTConstant, LoadImage, VHS_LoadVideo, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoCombine, PrimitiveInt, PreviewAny, SetNode, PrimitiveFloat, VHS_VideoCombine]
patterns: []
missing: []
---

# 数字人/数字人/Wan2.2-Animate【换人迁移】kj遮罩-高质+快速+细节_1990762965668405249.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.2-Animate【换人迁移】kj遮罩-高质+快速+细节_1990762965668405249.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（105 个）：
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `PreviewImage`
- `ImageResizeKJv2`
- `DrawViTPose`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSetBlockSwap`
- `SetNode`
- `SetNode`
- `Note`
- `GetNode`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `ImageRemoveBackground+`
- `GrowMask`
- `ImageBlend`
- `DrawMaskOnImage`
- `BlockifyMask`
- `VHS_VideoCombine`
- `SetNode`
- `PoseAndFaceDetection`
- `SetNode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Seed (rgthree)`
- `SetNode`
- `SetNode`
- `PrimitiveStringMultiline`
- `WanVideoSampler` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `PreviewImage`
- `PreviewImage`
- `Note`
- `Note`
- `Note`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `OnnxDetectionModelLoader`
- `RemBGSession+`
- `INTConstant`
- `INTConstant`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `SetNode`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoTextEncodeCached`
- `WanVideoModelLoader`
- `INTConstant`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `PreviewAny`
- `SetNode`
- `PrimitiveFloat`
- `VHS_VideoCombine`

## 知识

覆盖率 **38%**（40/105）

**有卡**：`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`ImageResizeKJv2`、`DrawViTPose`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`ImageRemoveBackground+`、`GrowMask`、`ImageBlend`、`DrawMaskOnImage`、`BlockifyMask`、`VHS_VideoCombine`、`PoseAndFaceDetection`、`ImageConcatMulti`、`GetImageSizeAndCount`、`Seed (rgthree)`、`WanVideoSampler`、`WanVideoClipVisionEncode`、`WanVideoDecode`、`WanVideoAnimateEmbeds`、`WanVideoLoraSelectMulti`、`OnnxDetectionModelLoader`、`RemBGSession+`、`INTConstant`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoTextEncodeCached`、`WanVideoModelLoader`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、Seed (rgthree)、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs
