---
key: 数字人/数字人/Wan2.2 Animate V2替换视频人物，保留原声_1983884901671993345.json
name: Wan2.2 Animate V2替换视频人物，保留原声_1983884901671993345
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.2 Animate V2替换视频人物，保留原声_1983884901671993345.json
hash: d598d5d2c36feb0a
coverage: 0.56338
learned_at: 2026-10-26 01:57:48
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, JWInteger, JWInteger, CR Prompt Text, WanVideoTorchCompileSettings, MarkdownNote, CLIPVisionLoader, WanVideoLoraSelectMulti, WanVideoSetLoRAs, SetNode, WanVideoBlockSwap, SetNode, ImageResizeKJv2, SetNode, SetNode, SetNode, SetNode, Sam2Segmentation, DownloadAndLoadSAM2Model, SetNode, GetNode, GrowMask, BlockifyMask, DrawMaskOnImage, SetNode, Reroute, SetNode, WanVideoSetBlockSwap, WanVideoVAELoader, WanVideoModelLoader, VHS_LoadVideo, GetImageSizeAndCount, ImageResizeKJv2, ImageConcatMulti, GetNode, ACE_ImageFaceCrop, PoseAndFaceDetection, easy showAnything, PoseRetargetPromptHelper, easy showAnything, DrawViTPose, SetNode, SetNode, PointsEditor, VHS_VideoCombine, WanVideoClipVisionEncode, GetNode, GetNode, WanVideoAnimateEmbeds, ImageConcatMulti, GetNode, GetImageSizeAndCount, WanVideoDecode, GetNode, WanVideoTextEncodeCached, WanVideoSampler, OnnxDetectionModelLoader, VHS_VideoCombine, VHS_LoadVideo, LoadImage, JWInteger]
patterns: []
missing: []
---

# 数字人/数字人/Wan2.2 Animate V2替换视频人物，保留原声_1983884901671993345.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.2 Animate V2替换视频人物，保留原声_1983884901671993345.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（71 个）：
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
- `VHS_VideoCombine`
- `JWInteger`
- `JWInteger`
- `CR Prompt Text`
- `WanVideoTorchCompileSettings`
- `MarkdownNote`
- `CLIPVisionLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoBlockSwap`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Sam2Segmentation`
- `DownloadAndLoadSAM2Model`
- `SetNode`
- `GetNode`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `SetNode`
- `Reroute`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `VHS_LoadVideo`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `ImageConcatMulti`
- `GetNode`
- `ACE_ImageFaceCrop`
- `PoseAndFaceDetection`
- `easy showAnything`
- `PoseRetargetPromptHelper`
- `easy showAnything`
- `DrawViTPose`
- `SetNode`
- `SetNode`
- `PointsEditor`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `ImageConcatMulti`
- `GetNode`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `OnnxDetectionModelLoader`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `JWInteger`

## 知识

覆盖率 **56%**（40/71）

**有卡**：`VHS_VideoCombine`、`JWInteger`、`CR Prompt Text`、`WanVideoTorchCompileSettings`、`CLIPVisionLoader`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`ImageResizeKJv2`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`WanVideoModelLoader`、`VHS_LoadVideo`、`GetImageSizeAndCount`、`ImageConcatMulti`、`ACE_ImageFaceCrop`、`PoseAndFaceDetection`、`PoseRetargetPromptHelper`、`DrawViTPose`、`PointsEditor`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`OnnxDetectionModelLoader`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
