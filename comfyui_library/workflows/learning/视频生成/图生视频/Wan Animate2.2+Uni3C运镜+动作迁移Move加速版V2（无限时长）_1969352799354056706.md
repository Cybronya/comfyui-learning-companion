---
key: 视频生成/图生视频/Wan Animate2.2+Uni3C运镜+动作迁移Move加速版V2（无限时长）_1969352799354056706.json
name: Wan Animate2.2+Uni3C运镜+动作迁移Move加速版V2（无限时长）_1969352799354056706.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1969352799354056706.json
hash: 26089118e94ac475
coverage: 0.555556
learned_at: 2026-10-15 22:31:49
nodes: [ImageConcatMulti, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, DownloadAndLoadSAM2Model, SetNode, SetNode, PixelPerfectResolution, Reroute, FaceMaskFromPoseKeypoints, SetNode, GrowMask, BlockifyMask, SetNode, Note, SetNode, ImageConcatMulti, GetNode, GetNode, GetImageSizeAndCount, WanVideoAnimateEmbeds, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, DWPreprocessor, Sam2Segmentation, ImageResizeKJv2, ImageResizeKJv2, SetNode, GetNode, GetNode, WanVideoUni3C_embeds, GetImageSizeAndCount, GetNode, WanVideoEncode, VHS_VideoCombine, SetNode, LoadImage, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoLoraSelectMulti, CLIPVisionLoader, WanVideoVAELoader, WanVideoTextEncodeCached, ImageCropByMaskAndResize, SetNode, WanVideoClipVisionEncode, Note, WanVideoContextOptions, WanVideoSampler, GetNode, VHS_LoadVideo, GetNode, GetNode, SetNode, VHS_VideoCombine, GetNode, DrawMaskOnImage, GetNode, PointsEditor, SetNode, GetNode, Note, VHS_VideoCombine, VHS_VideoCombine, Note, Note, WanVideoModelLoader, Note, Note, JWInteger, JWInteger, VHS_LoadVideo, WanVideoUni3C_ControlnetLoader, JWInteger, CR Prompt Text, VHS_VideoCombine, WanVideoDecode]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan Animate2.2+Uni3C运镜+动作迁移Move加速版V2（无限时长）_1969352799354056706.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1969352799354056706.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（81 个）：
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `DownloadAndLoadSAM2Model`
- `SetNode`
- `SetNode`
- `PixelPerfectResolution`
- `Reroute`
- `FaceMaskFromPoseKeypoints`
- `SetNode`
- `GrowMask`
- `BlockifyMask`
- `SetNode`
- `Note`
- `SetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `WanVideoAnimateEmbeds`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `MarkdownNote`
- `DWPreprocessor`
- `Sam2Segmentation`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoUni3C_embeds`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoEncode`
- `VHS_VideoCombine`
- `SetNode`
- `LoadImage`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `ImageCropByMaskAndResize`
- `SetNode`
- `WanVideoClipVisionEncode`
- `Note`
- `WanVideoContextOptions`
- `WanVideoSampler` ★核心
- `GetNode`
- `VHS_LoadVideo`
- `GetNode`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `DrawMaskOnImage`
- `GetNode`
- `PointsEditor`
- `SetNode`
- `GetNode`
- `Note`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `WanVideoModelLoader`
- `Note`
- `Note`
- `JWInteger`
- `JWInteger`
- `VHS_LoadVideo`
- `WanVideoUni3C_ControlnetLoader`
- `JWInteger`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `WanVideoDecode`

## 知识

覆盖率 **56%**（45/81）

**有卡**：`ImageConcatMulti`、`DownloadAndLoadSAM2Model`、`PixelPerfectResolution`、`FaceMaskFromPoseKeypoints`、`GrowMask`、`BlockifyMask`、`GetImageSizeAndCount`、`WanVideoAnimateEmbeds`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`DWPreprocessor`、`Sam2Segmentation`、`ImageResizeKJv2`、`WanVideoUni3C_embeds`、`WanVideoEncode`、`VHS_VideoCombine`、`LoadImage`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`ImageCropByMaskAndResize`、`WanVideoClipVisionEncode`、`WanVideoContextOptions`、`WanVideoSampler`、`VHS_LoadVideo`、`DrawMaskOnImage`、`PointsEditor`、`WanVideoModelLoader`、`JWInteger`、`WanVideoUni3C_ControlnetLoader`、`CR Prompt Text`、`WanVideoDecode`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode
