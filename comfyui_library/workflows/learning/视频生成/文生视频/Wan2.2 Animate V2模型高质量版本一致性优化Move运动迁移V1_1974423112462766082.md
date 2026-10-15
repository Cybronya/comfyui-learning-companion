---
key: 视频生成/文生视频/Wan2.2 Animate V2模型高质量版本一致性优化Move运动迁移V1_1974423112462766082.json
name: Wan2.2 Animate V2模型高质量版本一致性优化Move运动迁移V1_1974423112462766082
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 Animate V2模型高质量版本一致性优化Move运动迁移V1_1974423112462766082.json
hash: 311eacb8d683e37d
coverage: 0.584416
learned_at: 2026-10-15 22:47:08
nodes: [ImageConcatMulti, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, SetNode, Note, GetNode, SetNode, ImageConcatMulti, GetNode, GetNode, GetImageSizeAndCount, WanVideoAnimateEmbeds, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, ImageResizeKJv2, SetNode, GetNode, DrawMaskOnImage, SetNode, WanVideoEncode, VHS_VideoCombine, WanVideoTorchCompileSettings, WanVideoBlockSwap, CLIPVisionLoader, WanVideoVAELoader, WanVideoContextOptions, GetNode, WanVideoUni3C_embeds, Note, Note, SetNode, WanVideoTextEncodeCached, CR Prompt Text, WanVideoDecode, GrowMask, BlockifyMask, PoseRetargetPromptHelper, Sam2Segmentation, DownloadAndLoadSAM2Model, GetImageSizeAndCount, LoadImage, ImageResizeKJv2, WanVideoUni3C_ControlnetLoader, VHS_VideoCombine, WanVideoClipVisionEncode, JWInteger, VHS_LoadVideo, JWInteger, JWInteger, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, PointsEditor, GetNode, GetNode, GetNode, Note, SetNode, VHS_LoadVideo, VHS_VideoCombine, GetNode, PoseAndFaceDetection, OnnxDetectionModelLoader, DrawViTPose, easy showAnything, easy showAnything, SetNode, SetNode, Reroute, ACE_ImageFaceCrop, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2 Animate V2模型高质量版本一致性优化Move运动迁移V1_1974423112462766082.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 Animate V2模型高质量版本一致性优化Move运动迁移V1_1974423112462766082.json`

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
- `WanVideoEncode`
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `WanVideoContextOptions`
- `GetNode`
- `WanVideoUni3C_embeds`
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
- `ImageResizeKJv2`
- `WanVideoUni3C_ControlnetLoader`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `JWInteger`
- `VHS_LoadVideo`
- `JWInteger`
- `JWInteger`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
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

## 知识

覆盖率 **58%**（45/77）

**有卡**：`ImageConcatMulti`、`GetImageSizeAndCount`、`WanVideoAnimateEmbeds`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageResizeKJv2`、`DrawMaskOnImage`、`WanVideoEncode`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoContextOptions`、`WanVideoUni3C_embeds`、`WanVideoTextEncodeCached`、`CR Prompt Text`、`WanVideoDecode`、`GrowMask`、`BlockifyMask`、`PoseRetargetPromptHelper`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`LoadImage`、`WanVideoUni3C_ControlnetLoader`、`WanVideoClipVisionEncode`、`JWInteger`、`VHS_LoadVideo`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoSampler`、`PointsEditor`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`DrawViTPose`、`ACE_ImageFaceCrop`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode
