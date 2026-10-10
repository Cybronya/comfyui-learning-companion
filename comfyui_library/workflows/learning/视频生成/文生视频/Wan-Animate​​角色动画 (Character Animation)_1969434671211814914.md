---
key: 视频生成/文生视频/Wan-Animate​​角色动画 (Character Animation)_1969434671211814914.json
name: Wan-Animate​​角色动画 (Character Animation)_1969434671211814914
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan-Animate​​角色动画 (Character Animation)_1969434671211814914.json
hash: ce195f962093a045
coverage: 0.5
learned_at: 2026-10-10 23:06:24
nodes: [ImageConcatMulti, GetNode, DWPreprocessor, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, PixelPerfectResolution, Reroute, FaceMaskFromPoseKeypoints, SetNode, ImageCropByMaskAndResize, SetNode, GetNode, CLIPVisionLoader, WanVideoClipVisionEncode, GetNode, WanVideoTorchCompileSettings, SetNode, ImageConcatMulti, GetNode, GetNode, GetImageSizeAndCount, WanVideoContextOptions, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, Note, VHS_VideoCombine, Fast Groups Bypasser (rgthree), WanVideoDecode, WanVideoVAELoader, ImageResizeKJv2, SetNode, SetNode, GetImageSize, VHS_VideoCombine, VHS_VideoCombine, LayerMask: LoadFlorence2Model, LayerUtility: PurgeVRAM, LayerUtility: Florence2Image2Prompt, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, WanVideoAnimateEmbeds, WanVideoTextEncodeCached, INTConstant, WanVideoSampler, VHS_LoadVideo, LoadImage, WanVideoModelLoader, WanVideoLoraSelectMulti, INTConstant, INTConstant]
patterns: []
missing: [LayerMask: LoadFlorence2Model, LayerUtility: PurgeVRAM, LayerUtility: Florence2Image2Prompt]
discoveries: [次要节点 `LayerMask: LoadFlorence2Model` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: Florence2Image2Prompt` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan-Animate​​角色动画 (Character Animation)_1969434671211814914.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan-Animate​​角色动画 (Character Animation)_1969434671211814914.json`

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

覆盖率 **50%**（31/62）

**有卡**：`ImageConcatMulti`、`DWPreprocessor`、`PixelPerfectResolution`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoTorchCompileSettings`、`GetImageSizeAndCount`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoVAELoader`、`ImageResizeKJv2`、`GetImageSize`、`WanVideoAnimateEmbeds`、`WanVideoTextEncodeCached`、`INTConstant`、`WanVideoSampler`、`VHS_LoadVideo`、`LoadImage`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`

**缺卡**（3）：`LayerMask: LoadFlorence2Model`、`LayerUtility: PurgeVRAM`、`LayerUtility: Florence2Image2Prompt`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti

## 学习发现

- 次要节点 `LayerMask: LoadFlorence2Model` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: Florence2Image2Prompt` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
