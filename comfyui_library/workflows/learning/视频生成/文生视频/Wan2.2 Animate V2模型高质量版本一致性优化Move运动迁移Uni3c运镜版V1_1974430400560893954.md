---
key: 视频生成/文生视频/Wan2.2 Animate V2模型高质量版本一致性优化Move运动迁移Uni3c运镜版V1_1974430400560893954.json
name: Wan2.2 Animate V2模型高质量版本一致性优化Move运动迁移Uni3c运镜版V1_1974430400560893954
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 Animate V2模型高质量版本一致性优化Move运动迁移Uni3c运镜版V1_1974430400560893954.json
hash: d279b157ed03747d
coverage: 0.571429
learned_at: 2026-10-10 23:06:41
nodes: [ImageConcatMulti, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, SetNode, Note, GetNode, SetNode, ImageConcatMulti, GetNode, GetNode, GetImageSizeAndCount, WanVideoAnimateEmbeds, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, ImageResizeKJv2, SetNode, GetNode, DrawMaskOnImage, SetNode, VHS_VideoCombine, WanVideoTorchCompileSettings, WanVideoBlockSwap, CLIPVisionLoader, WanVideoVAELoader, WanVideoContextOptions, GetNode, Note, Note, SetNode, WanVideoTextEncodeCached, CR Prompt Text, WanVideoDecode, GrowMask, BlockifyMask, PoseRetargetPromptHelper, Sam2Segmentation, DownloadAndLoadSAM2Model, GetImageSizeAndCount, LoadImage, VHS_VideoCombine, WanVideoClipVisionEncode, JWInteger, JWInteger, WanVideoLoraSelectMulti, WanVideoModelLoader, PointsEditor, GetNode, GetNode, GetNode, Note, SetNode, VHS_LoadVideo, VHS_VideoCombine, GetNode, PoseAndFaceDetection, OnnxDetectionModelLoader, DrawViTPose, easy showAnything, easy showAnything, SetNode, SetNode, Reroute, ACE_ImageFaceCrop, VHS_VideoCombine, ImageResizeKJv2, WanVideoSampler, WanVideoEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, VHS_LoadVideo, JWInteger]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan2.2 Animate V2模型高质量版本一致性优化Move运动迁移Uni3c运镜版V1_1974430400560893954.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 Animate V2模型高质量版本一致性优化Move运动迁移Uni3c运镜版V1_1974430400560893954.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（77 个）：
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `Note`
- `GetNode`
- `SetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `WanVideoAnimateEmbeds`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `MarkdownNote`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `DrawMaskOnImage`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `WanVideoContextOptions`
- `GetNode`
- `Note`
- `Note`
- `SetNode`
- `WanVideoTextEncodeCached`
- `CR Prompt Text`
- `WanVideoDecode`
- `GrowMask`
- `BlockifyMask`
- `PoseRetargetPromptHelper`
- `Sam2Segmentation`
- `DownloadAndLoadSAM2Model`
- `GetImageSizeAndCount`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `JWInteger`
- `JWInteger`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `PointsEditor`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `GetNode`
- `PoseAndFaceDetection`
- `OnnxDetectionModelLoader`
- `DrawViTPose`
- `easy showAnything`
- `easy showAnything`
- `SetNode`
- `SetNode`
- `Reroute`
- `ACE_ImageFaceCrop`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `WanVideoSampler` ★核心
- `WanVideoEncode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `VHS_LoadVideo`
- `JWInteger`

## 知识

覆盖率 **57%**（44/77）

**有卡**：`ImageConcatMulti`、`GetImageSizeAndCount`、`WanVideoAnimateEmbeds`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageResizeKJv2`、`DrawMaskOnImage`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoContextOptions`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`GrowMask`、`BlockifyMask`、`PoseRetargetPromptHelper`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`LoadImage`、`WanVideoClipVisionEncode`、`JWInteger`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`PointsEditor`、`VHS_LoadVideo`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`DrawViTPose`、`ACE_ImageFaceCrop`、`WanVideoSampler`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`WanVideoUni3C_embeds`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
