---
key: 平台全量/Wan2.2 animate表情动作迁移（适合中近景））_1970410230880346113.json
name: Wan2.2 animate表情动作迁移（适合中近景））_1970410230880346113
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 animate表情动作迁移（适合中近景））_1970410230880346113.json
hash: 6ce8731621e4e8ae
coverage: 0.549296
learned_at: 2026-11-14 01:05:38
nodes: [ImageConcatMulti, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, Sam2Segmentation, DownloadAndLoadSAM2Model, SetNode, SetNode, Reroute, SetNode, SetNode, GrowMask, BlockifyMask, SetNode, DrawMaskOnImage, GetNode, Note, SetNode, GetNode, GetNode, SetNode, ImageConcatMulti, GetNode, GetNode, WanVideoSetBlockSwap, MarkdownNote, GetNode, PreviewImage, ImageCropByMaskAndResize, FaceMaskFromPoseKeypoints, Note, WanVideoBlockSwap, ImageResizeKJv2, DWPreprocessor, VHS_VideoCombine, VHS_VideoCombine, WanVideoAnimateEmbeds, GetNode, GetNode, WanVideoClipVisionEncode, WanVideoSampler, CLIPVisionLoader, WanVideoVAELoader, WanVideoTextEncodeCached, WanVideoSetLoRAs, WanVideoModelLoader, GetImageSizeAndCount, WanVideoDecode, VHS_VideoCombine, GetNode, PointsEditor, VHS_VideoCombine, SetNode, SetNode, LoadImage, WanVideoLoraSelectMulti, WanVideoTorchCompileSettings, PixelPerfectResolution, SetNode, VHS_VideoCombine, VHS_VideoInfo, VHS_LoadVideo, Int, Int, Int, Int]
patterns: []
missing: []
---

# 平台全量/Wan2.2 animate表情动作迁移（适合中近景））_1970410230880346113.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 animate表情动作迁移（适合中近景））_1970410230880346113.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（71 个）：
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Sam2Segmentation`
- `DownloadAndLoadSAM2Model`
- `SetNode`
- `SetNode`
- `Reroute`
- `SetNode`
- `SetNode`
- `GrowMask`
- `BlockifyMask`
- `SetNode`
- `DrawMaskOnImage`
- `GetNode`
- `Note`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `WanVideoSetBlockSwap`
- `MarkdownNote`
- `GetNode`
- `PreviewImage`
- `ImageCropByMaskAndResize`
- `FaceMaskFromPoseKeypoints`
- `Note`
- `WanVideoBlockSwap`
- `ImageResizeKJv2`
- `DWPreprocessor`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `WanVideoSampler` ★核心
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `GetNode`
- `PointsEditor`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `LoadImage`
- `WanVideoLoraSelectMulti`
- `WanVideoTorchCompileSettings`
- `PixelPerfectResolution`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `VHS_LoadVideo`
- `Int`
- `Int`
- `Int`
- `Int`

## 知识

覆盖率 **55%**（39/71）

**有卡**：`ImageConcatMulti`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`WanVideoSetBlockSwap`、`ImageCropByMaskAndResize`、`FaceMaskFromPoseKeypoints`、`WanVideoBlockSwap`、`ImageResizeKJv2`、`DWPreprocessor`、`VHS_VideoCombine`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`GetImageSizeAndCount`、`WanVideoDecode`、`PointsEditor`、`LoadImage`、`WanVideoLoraSelectMulti`、`WanVideoTorchCompileSettings`、`PixelPerfectResolution`、`VHS_VideoInfo`、`VHS_LoadVideo`、`Int`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
