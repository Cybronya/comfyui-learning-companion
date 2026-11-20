---
key: 平台全量/Wan Animate2.2 替换主体，保留背景_1988619047652737026.json
name: Wan Animate2.2 替换主体，保留背景_1988619047652737026
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan Animate2.2 替换主体，保留背景_1988619047652737026.json
hash: 5367570139cd3885
coverage: 0.488636
learned_at: 2026-11-14 01:03:58
nodes: [DownloadAndLoadSAM2Model, GetNode, Sam2Segmentation, GetNode, SetNode, SetNode, SetNode, DrawMaskOnImage, JWInteger, SetNode, JWInteger, SetNode, JWInteger, GetNode, GetNode, SetNode, WanVideoSetLoRAs, MarkdownNote, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoBlockSwap, GetNode, WanVideoClipVisionEncode, SetNode, CLIPVisionLoader, Anything Everywhere, WanVideoSetBlockSwap, WanVideoVAELoader, Anything Everywhere, SetNode, SetNode, BlockifyMask, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, WanVideoTextEncodeCached, WanVideoEncode, WanVideoUni3C_ControlnetLoader, ImageResizeKJv2, WanVideoUni3C_embeds, SetNode, GetNode, GetNode, GetImageSizeAndCount, GetNode, GetNode, PreviewImage, easy cleanGpuUsed, WanVideoAnimateEmbeds, PreviewImage, SetNode, ImageResizeKJv2, GetNode, VHS_LoadVideo, CR Prompt Text, VHS_VideoCombine, Manual XY Entry Info, VHS_LoadVideo, PointsEditor, PreviewImage, ImageFromBatch+, GetNode, GetNode, WanVideoDecode, ImageConcatMulti, VHS_VideoCombine, ImageConcatMulti, VHS_VideoCombine, WanVideoSampler, PreviewImage, LoadImage, SetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, OnnxDetectionModelLoader, PoseAndFaceDetection, DrawViTPose]
patterns: []
missing: []
---

# 平台全量/Wan Animate2.2 替换主体，保留背景_1988619047652737026.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan Animate2.2 替换主体，保留背景_1988619047652737026.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（88 个）：
- `DownloadAndLoadSAM2Model`
- `GetNode`
- `Sam2Segmentation`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `DrawMaskOnImage`
- `JWInteger`
- `SetNode`
- `JWInteger`
- `SetNode`
- `JWInteger`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoSetLoRAs`
- `MarkdownNote`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `GetNode`
- `WanVideoClipVisionEncode`
- `SetNode`
- `CLIPVisionLoader`
- `Anything Everywhere`
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`
- `Anything Everywhere`
- `SetNode`
- `SetNode`
- `BlockifyMask`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `WanVideoEncode`
- `WanVideoUni3C_ControlnetLoader`
- `ImageResizeKJv2`
- `WanVideoUni3C_embeds`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `easy cleanGpuUsed`
- `WanVideoAnimateEmbeds`
- `PreviewImage`
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `VHS_LoadVideo`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `Manual XY Entry Info`
- `VHS_LoadVideo`
- `PointsEditor`
- `PreviewImage`
- `ImageFromBatch+`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `PreviewImage`
- `LoadImage`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `DrawViTPose`

## 知识

覆盖率 **49%**（43/88）

**有卡**：`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`DrawMaskOnImage`、`JWInteger`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`BlockifyMask`、`WanVideoTextEncodeCached`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`ImageResizeKJv2`、`WanVideoUni3C_embeds`、`GetImageSizeAndCount`、`easy cleanGpuUsed`、`WanVideoAnimateEmbeds`、`VHS_LoadVideo`、`CR Prompt Text`、`VHS_VideoCombine`、`Manual XY Entry Info`、`PointsEditor`、`ImageFromBatch+`、`WanVideoDecode`、`ImageConcatMulti`、`WanVideoSampler`、`LoadImage`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawViTPose`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeCached、WanVideoVAELoader
