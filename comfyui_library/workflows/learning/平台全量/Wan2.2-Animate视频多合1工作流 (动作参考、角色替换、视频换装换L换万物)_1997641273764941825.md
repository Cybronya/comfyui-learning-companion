---
key: 平台全量/Wan2.2-Animate视频多合1工作流 (动作参考、角色替换、视频换装换L换万物)_1997641273764941825.json
name: Wan2.2-Animate视频多合1工作流 (动作参考、角色替换、视频换装换L换万物)_1997641273764941825
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2-Animate视频多合1工作流 (动作参考、角色替换、视频换装换L换万物)_1997641273764941825.json
hash: c497ca30e5ca1993
coverage: 0.505263
learned_at: 2026-11-14 01:05:57
nodes: [GetNode, GetNode, GetNode, GetNode, WanVideoTorchCompileSettings, SetNode, GetNode, WanVideoSetLoRAs, MarkdownNote, INTConstant, INTConstant, PreviewImage, WanVideoBlockSwap, Note, SetNode, GetNode, ImageConcatMulti, GetNode, WanVideoDecode, WanVideoSetBlockSwap, SetNode, GetNode, GetNode, WanVideoContextOptions, ImageConcatMulti, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, SetNode, easy clearCacheAll, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, BlockifyMask, DownloadAndLoadSAM2Model, Sam2Segmentation, GrowMaskWithBlur, BlockifyMask, GetNode, DrawMaskOnImage, SetNode, VHS_VideoCombine, DrawMaskOnImage, VHS_VideoCombine, WanVideoAnimateEmbeds, GetNode, PixelPerfectResolution, ImageCropByMaskAndResize, FaceMaskFromPoseKeypoints, SetNode, VHS_VideoCombine, SetNode, WanVideoClipVisionEncode, GrowMaskWithBlur, LoadImage, GetNode, SetNode, SetNode, GetNode, GetNode, LayerMask: SegformerB2ClothesUltra, MarkdownNote, easy cleanGpuUsed, MarkdownNote, GetNode, GetNode, GetNode, GetImageSizeAndCount, TT_img_enc, SaveImage, VHS_LoadVideo, INTConstant, WanVideoModelLoader, WanVideoVAELoader, CLIPVisionLoader, DWPreprocessor, WanVideoLoraSelectMulti, VHS_VideoCombine, ImageResizeKJv2, WanVideoTextEncodeCached, easy cleanGpuUsed, easy clearCacheAll, PointsEditor, WanVideoSampler, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/Wan2.2-Animate视频多合1工作流 (动作参考、角色替换、视频换装换L换万物)_1997641273764941825.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2-Animate视频多合1工作流 (动作参考、角色替换、视频换装换L换万物)_1997641273764941825.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（95 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `MarkdownNote`
- `INTConstant`
- `INTConstant`
- `PreviewImage`
- `WanVideoBlockSwap`
- `Note`
- `SetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoContextOptions`
- `ImageConcatMulti`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy clearCacheAll`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `BlockifyMask`
- `DownloadAndLoadSAM2Model`
- `Sam2Segmentation`
- `GrowMaskWithBlur`
- `BlockifyMask`
- `GetNode`
- `DrawMaskOnImage`
- `SetNode`
- `VHS_VideoCombine`
- `DrawMaskOnImage`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `PixelPerfectResolution`
- `ImageCropByMaskAndResize`
- `FaceMaskFromPoseKeypoints`
- `SetNode`
- `VHS_VideoCombine`
- `SetNode`
- `WanVideoClipVisionEncode`
- `GrowMaskWithBlur`
- `LoadImage`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LayerMask: SegformerB2ClothesUltra`
- `MarkdownNote`
- `easy cleanGpuUsed`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `TT_img_enc`
- `SaveImage`
- `VHS_LoadVideo`
- `INTConstant`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `WanVideoLoraSelectMulti`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `WanVideoTextEncodeCached`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `PointsEditor`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`

## 知识

覆盖率 **51%**（48/95）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`INTConstant`、`WanVideoBlockSwap`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoSetBlockSwap`、`WanVideoContextOptions`、`easy clearCacheAll`、`BlockifyMask`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`GrowMaskWithBlur`、`DrawMaskOnImage`、`VHS_VideoCombine`、`WanVideoAnimateEmbeds`、`PixelPerfectResolution`、`ImageCropByMaskAndResize`、`FaceMaskFromPoseKeypoints`、`WanVideoClipVisionEncode`、`LoadImage`、`LayerMask: SegformerB2ClothesUltra`、`easy cleanGpuUsed`、`GetImageSizeAndCount`、`TT_img_enc`、`SaveImage`、`VHS_LoadVideo`、`WanVideoModelLoader`、`WanVideoVAELoader`、`CLIPVisionLoader`、`DWPreprocessor`、`WanVideoLoraSelectMulti`、`ImageResizeKJv2`、`WanVideoTextEncodeCached`、`PointsEditor`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
