---
key: 视频生成/图生视频/wan 2.2 Animate 视频动作迁移，人物替换，图生视频，脸部参考，基础用法简单演示_1970498046612172801.json
name: wan 2.2 Animate 视频动作迁移，人物替换，图生视频，脸部参考，基础用法简单演示_1970498046612172801.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan 2.2 Animate 视频动作迁移，人物替换，图生视频，脸部参考，基础用法简单演示_1970498046612172801.json
hash: 2566ed5e2ef22b8a
coverage: 0.878788
learned_at: 2026-10-15 22:31:53
nodes: [WanVideoVAELoader, WanVideoClipVisionEncode, SetNode, GetImageSizeAndCount, WanVideoDecode, ImageCropByMaskAndResize, Reroute, DownloadAndLoadSAM2Model, PointsEditor, Sam2Segmentation, GrowMask, BlockifyMask, ImageResizeKJv2, PreviewImage, PixelPerfectResolution, FaceMaskFromPoseKeypoints, DWPreprocessor, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoAnimateEmbeds, WanVideoTextEncodeCached, WanVideoSampler, GetImageSize+, DrawMaskOnImage, SetNode, VHS_VideoCombine, LoadImage, WanVideoModelLoader, WanVideoLoraSelectMulti, CLIPVisionLoader, VHS_LoadVideo, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/wan 2.2 Animate 视频动作迁移，人物替换，图生视频，脸部参考，基础用法简单演示_1970498046612172801.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1970498046612172801.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（33 个）：
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `SetNode`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `ImageCropByMaskAndResize`
- `Reroute`
- `DownloadAndLoadSAM2Model`
- `PointsEditor`
- `Sam2Segmentation`
- `GrowMask`
- `BlockifyMask`
- `ImageResizeKJv2`
- `PreviewImage`
- `PixelPerfectResolution`
- `FaceMaskFromPoseKeypoints`
- `DWPreprocessor`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoAnimateEmbeds`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `GetImageSize+`
- `DrawMaskOnImage`
- `SetNode`
- `VHS_VideoCombine`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `CLIPVisionLoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

## 知识

覆盖率 **88%**（29/33）

**有卡**：`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`GetImageSizeAndCount`、`WanVideoDecode`、`ImageCropByMaskAndResize`、`DownloadAndLoadSAM2Model`、`PointsEditor`、`Sam2Segmentation`、`GrowMask`、`BlockifyMask`、`ImageResizeKJv2`、`PixelPerfectResolution`、`FaceMaskFromPoseKeypoints`、`DWPreprocessor`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoAnimateEmbeds`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`GetImageSize+`、`DrawMaskOnImage`、`VHS_VideoCombine`、`LoadImage`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`CLIPVisionLoader`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
