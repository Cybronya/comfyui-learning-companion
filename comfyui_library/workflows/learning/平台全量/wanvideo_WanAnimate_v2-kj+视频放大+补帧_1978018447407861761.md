---
key: 平台全量/wanvideo_WanAnimate_v2-kj+视频放大+补帧_1978018447407861761.json
name: wanvideo_WanAnimate_v2-kj+视频放大+补帧_1978018447407861761
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wanvideo_WanAnimate_v2-kj+视频放大+补帧_1978018447407861761.json
hash: e656173fc105b844
coverage: 0.510638
learned_at: 2026-11-14 01:20:12
nodes: [GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, ImageResizeKJv2, SetNode, DrawMaskOnImage, GetNode, SetNode, GetNode, CLIPVisionLoader, WanVideoClipVisionEncode, GetNode, GetNode, WanVideoTorchCompileSettings, SetNode, ImageConcatMulti, GetNode, WanVideoDecode, GetNode, WanVideoContextOptions, Note, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, GrowMaskWithBlur, BlockifyMask, Note, Sam2Segmentation, GetImageSizeAndCount, SetNode, SetNode, GetNode, DownloadAndLoadSAM2Model, Note, WanVideoSampler, MarkdownNote, MarkdownNote, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoVAELoader, OnnxDetectionModelLoader, DrawViTPose, PoseAndFaceDetection, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, WanVideoAnimateEmbeds, VHS_LoadVideo, LoadImage, ImageResizeKJv2, VHS_VideoCombine, GetImageSizeAndCount, GetNode, GetNode, LoadImage, WanVideoTextEncodeCached, SetNode, VHS_VideoCombine, GetNode, ImageConcatMulti, ImageConcatMulti, PreviewImage, VHS_VideoCombine, PreviewImage, JjkText, Int, Int, SetNode, Int, SetNode, Fast Bypasser (rgthree), Mute / Bypass Repeater (rgthree), Int, CR Upscale Image, SimpleMath+, SetNode, Fast Groups Bypasser (rgthree), RIFE VFI, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, Int]
patterns: []
missing: []
---

# 平台全量/wanvideo_WanAnimate_v2-kj+视频放大+补帧_1978018447407861761.json

> 来源文件 `comfyui_library/workflows/平台全量/wanvideo_WanAnimate_v2-kj+视频放大+补帧_1978018447407861761.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（94 个）：
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
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `LoadImage`
- `WanVideoTextEncodeCached`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `PreviewImage`
- `VHS_VideoCombine`
- `PreviewImage`
- `JjkText`
- `Int`
- `Int`
- `SetNode`
- `Int`
- `SetNode`
- `Fast Bypasser (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Int`
- `CR Upscale Image`
- `SimpleMath+`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `RIFE VFI`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `Int`

## 知识

覆盖率 **51%**（48/94）

**有卡**：`ImageResizeKJv2`、`DrawMaskOnImage`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoTorchCompileSettings`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`GrowMaskWithBlur`、`BlockifyMask`、`Sam2Segmentation`、`GetImageSizeAndCount`、`DownloadAndLoadSAM2Model`、`WanVideoSampler`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoVAELoader`、`OnnxDetectionModelLoader`、`DrawViTPose`、`PoseAndFaceDetection`、`VHS_VideoCombine`、`WanVideoAnimateEmbeds`、`VHS_LoadVideo`、`LoadImage`、`WanVideoTextEncodeCached`、`Int`、`Fast Bypasser (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`CR Upscale Image`、`SimpleMath+`、`RIFE VFI`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
