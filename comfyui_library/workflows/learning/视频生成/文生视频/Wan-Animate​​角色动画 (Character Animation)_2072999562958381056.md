---
key: 视频生成/文生视频/Wan-Animate​​角色动画 (Character Animation)_2072999562958381056.json
name: Wan-Animate​​角色动画 (Character Animation)_2072999562958381056
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan-Animate​​角色动画 (Character Animation)_2072999562958381056.json
hash: cddc2ac70b2fd1b5
coverage: 0.548387
learned_at: 2026-10-15 22:47:07
nodes: [ImageConcatMulti, GetNode, DWPreprocessor, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, PixelPerfectResolution, Reroute, FaceMaskFromPoseKeypoints, SetNode, ImageCropByMaskAndResize, SetNode, GetNode, CLIPVisionLoader, WanVideoClipVisionEncode, GetNode, WanVideoTorchCompileSettings, SetNode, ImageConcatMulti, GetNode, GetNode, GetImageSizeAndCount, WanVideoContextOptions, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, Note, VHS_VideoCombine, Fast Groups Bypasser (rgthree), WanVideoDecode, WanVideoVAELoader, ImageResizeKJv2, SetNode, SetNode, GetImageSize, VHS_VideoCombine, VHS_VideoCombine, LayerMask: LoadFlorence2Model, LayerUtility: PurgeVRAM, LayerUtility: Florence2Image2Prompt, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, WanVideoAnimateEmbeds, WanVideoTextEncodeCached, INTConstant, WanVideoSampler, VHS_LoadVideo, LoadImage, WanVideoModelLoader, WanVideoLoraSelectMulti, INTConstant, INTConstant]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan-Animate​​角色动画 (Character Animation)_2072999562958381056.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan-Animate​​角色动画 (Character Animation)_2072999562958381056.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（62 个）：
- `ImageConcatMulti`
- `GetNode`
- `DWPreprocessor`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `PixelPerfectResolution`
- `Reroute`
- `FaceMaskFromPoseKeypoints`
- `SetNode`
- `ImageCropByMaskAndResize`
- `SetNode`
- `GetNode`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `WanVideoContextOptions`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `MarkdownNote`
- `Note`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `GetImageSize`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LayerMask: LoadFlorence2Model`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: Florence2Image2Prompt`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoAnimateEmbeds`
- `WanVideoTextEncodeCached`
- `INTConstant`
- `WanVideoSampler` ★核心
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `INTConstant`
- `INTConstant`

## 知识

覆盖率 **55%**（34/62）

**有卡**：`ImageConcatMulti`、`DWPreprocessor`、`PixelPerfectResolution`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoTorchCompileSettings`、`GetImageSizeAndCount`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoVAELoader`、`ImageResizeKJv2`、`GetImageSize`、`LayerMask: LoadFlorence2Model`、`LayerUtility: PurgeVRAM`、`LayerUtility: Florence2Image2Prompt`、`WanVideoAnimateEmbeds`、`WanVideoTextEncodeCached`、`INTConstant`、`WanVideoSampler`、`VHS_LoadVideo`、`LoadImage`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
