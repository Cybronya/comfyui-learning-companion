---
key: 平台全量/wanvideo_WanAnimate_v2-kj_1975189830646804481.json
name: wanvideo_WanAnimate_v2-kj_1975189830646804481
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wanvideo_WanAnimate_v2-kj_1975189830646804481.json
hash: cb391db237b3df74
coverage: 0.527027
learned_at: 2026-11-14 01:20:12
nodes: [GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, ImageResizeKJv2, SetNode, DrawMaskOnImage, GetNode, SetNode, GetNode, CLIPVisionLoader, WanVideoClipVisionEncode, GetNode, GetNode, WanVideoTorchCompileSettings, SetNode, ImageConcatMulti, GetNode, WanVideoDecode, GetNode, WanVideoContextOptions, Note, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, GrowMaskWithBlur, BlockifyMask, Note, Sam2Segmentation, GetImageSizeAndCount, SetNode, SetNode, GetNode, DownloadAndLoadSAM2Model, Note, WanVideoSampler, MarkdownNote, MarkdownNote, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoVAELoader, OnnxDetectionModelLoader, DrawViTPose, PoseAndFaceDetection, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, WanVideoAnimateEmbeds, VHS_LoadVideo, LoadImage, ImageResizeKJv2, VHS_VideoCombine, VHS_VideoCombine, GetNode, ImageConcatMulti, GetImageSizeAndCount, ImageConcatMulti, GetNode, GetNode, LoadImage, WanVideoTextEncodeCached, JjkText, SetNode, SetNode, Int, Int]
patterns: []
missing: []
---

# 平台全量/wanvideo_WanAnimate_v2-kj_1975189830646804481.json

> 来源文件 `comfyui_library/workflows/平台全量/wanvideo_WanAnimate_v2-kj_1975189830646804481.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（74 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `DrawMaskOnImage`
- `GetNode`
- `SetNode`
- `GetNode`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `ImageConcatMulti`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `WanVideoContextOptions`
- `Note`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `GrowMaskWithBlur`
- `BlockifyMask`
- `Note`
- `Sam2Segmentation`
- `GetImageSizeAndCount`
- `SetNode`
- `SetNode`
- `GetNode`
- `DownloadAndLoadSAM2Model`
- `Note`
- `WanVideoSampler` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `OnnxDetectionModelLoader`
- `DrawViTPose`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `VHS_LoadVideo`
- `LoadImage`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `LoadImage`
- `WanVideoTextEncodeCached`
- `JjkText`
- `SetNode`
- `SetNode`
- `Int`
- `Int`

## 知识

覆盖率 **53%**（39/74）

**有卡**：`ImageResizeKJv2`、`DrawMaskOnImage`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoTorchCompileSettings`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`GrowMaskWithBlur`、`BlockifyMask`、`Sam2Segmentation`、`GetImageSizeAndCount`、`DownloadAndLoadSAM2Model`、`WanVideoSampler`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`DrawViTPose`、`PoseAndFaceDetection`、`VHS_VideoCombine`、`WanVideoAnimateEmbeds`、`VHS_LoadVideo`、`LoadImage`、`WanVideoTextEncodeCached`、`Int`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
