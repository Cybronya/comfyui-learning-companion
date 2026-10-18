---
key: 视频生成/图生视频/Wan2.2 Animate 角色替换+背景动作迁移 KJ加速版-StarAI_1969240711893839873.json
name: Wan2.2 Animate 角色替换+背景动作迁移 KJ加速版-StarAI_1969240711893839873.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Animate 角色替换+背景动作迁移 KJ加速版-StarAI_1969240711893839873.json
hash: d17e71c27fc5a3bc
coverage: 0.475
learned_at: 2026-10-15 22:31:48
nodes: [VHS_LoadVideo, DrawMaskOnImage, GrowMask, SetNode, SetNode, SetNode, VHS_VideoCombine, BlockifyMask, SetNode, GetNode, GetNode, PixelPerfectResolution, DWPreprocessor, GetNode, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, SetNode, SetNode, WanVideoTorchCompileSettings, WanVideoVAELoader, CLIPVisionLoader, WanVideoModelLoader, SetNode, WanVideoLoraSelectMulti, SetNode, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, WanVideoTextEncodeCached, WanVideoAnimateEmbeds, WanVideoDecode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, LayerMask: SAM2VideoUltra, LayerMask: LoadFlorence2Model, SetNode, SetNode, LayerMask: ObjectDetectorFL2, GetNode, SetNode, SetNode, CR Text, CR Text, JWInteger, SetNode, JWInteger, Int, GetNode, GetNode, SetNode, ImageResizeKJv2, LoadImage, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageConcatMulti, GetImageSizeAndCount, WanVideoSampler, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, ImageConcatMulti, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate 角色替换+背景动作迁移 KJ加速版-StarAI_1969240711893839873.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1969240711893839873.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（80 个）：
- `VHS_LoadVideo`
- `DrawMaskOnImage`
- `GrowMask`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `BlockifyMask`
- `SetNode`
- `GetNode`
- `GetNode`
- `PixelPerfectResolution`
- `DWPreprocessor`
- `GetNode`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `SetNode`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `WanVideoModelLoader`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `WanVideoTextEncodeCached`
- `WanVideoAnimateEmbeds`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerMask: SAM2VideoUltra`
- `LayerMask: LoadFlorence2Model`
- `SetNode`
- `SetNode`
- `LayerMask: ObjectDetectorFL2`
- `GetNode`
- `SetNode`
- `SetNode`
- `CR Text`
- `CR Text`
- `JWInteger`
- `SetNode`
- `JWInteger`
- `Int`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `MarkdownNote`

## 知识

覆盖率 **48%**（38/80）

**有卡**：`VHS_LoadVideo`、`DrawMaskOnImage`、`GrowMask`、`VHS_VideoCombine`、`BlockifyMask`、`PixelPerfectResolution`、`DWPreprocessor`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`LayerMask: SAM2VideoUltra`、`LayerMask: LoadFlorence2Model`、`LayerMask: ObjectDetectorFL2`、`CR Text`、`JWInteger`、`Int`、`ImageResizeKJv2`、`LoadImage`、`ImageConcatMulti`、`GetImageSizeAndCount`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
