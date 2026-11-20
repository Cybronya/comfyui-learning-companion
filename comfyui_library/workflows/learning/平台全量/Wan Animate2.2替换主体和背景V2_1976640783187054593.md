---
key: 平台全量/Wan Animate2.2替换主体和背景V2_1976640783187054593.json
name: Wan Animate2.2替换主体和背景V2_1976640783187054593
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan Animate2.2替换主体和背景V2_1976640783187054593.json
hash: f12d35e5ef9e0df7
coverage: 0.5
learned_at: 2026-11-14 01:04:05
nodes: [SetNode, SetNode, SetNode, JWInteger, SetNode, JWInteger, SetNode, JWInteger, GetNode, GetNode, WanVideoSetLoRAs, MarkdownNote, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoBlockSwap, GetNode, WanVideoClipVisionEncode, CLIPVisionLoader, Anything Everywhere, WanVideoSetBlockSwap, WanVideoVAELoader, Anything Everywhere, GetNode, GetNode, GetNode, SetNode, GetNode, WanVideoTextEncodeCached, WanVideoEncode, WanVideoUni3C_ControlnetLoader, ImageResizeKJv2, WanVideoUni3C_embeds, GetNode, GetNode, GetImageSizeAndCount, GetNode, GetNode, PreviewImage, easy cleanGpuUsed, PreviewImage, SetNode, ImageResizeKJv2, VHS_LoadVideo, PreviewImage, ImageFromBatch+, GetNode, GetNode, WanVideoDecode, VHS_VideoCombine, ImageConcatMulti, PreviewImage, LoadImage, WanVideoSampler, GetNode, GetNode, GetNode, CR Prompt Text, ImageConcatMulti, VHS_LoadVideo, WanVideoModelLoader, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, SetNode, SetNode, DrawViTPose, PoseAndFaceDetection, VHS_VideoCombine, VHS_VideoCombine, WanVideoAnimateEmbeds, VHS_VideoCombine, Manual XY Entry Info, SetNode, GetNode, SetNode]
patterns: []
missing: []
---

# 平台全量/Wan Animate2.2替换主体和背景V2_1976640783187054593.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan Animate2.2替换主体和背景V2_1976640783187054593.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（76 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `JWInteger`
- `SetNode`
- `JWInteger`
- `SetNode`
- `JWInteger`
- `GetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `MarkdownNote`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `GetNode`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `Anything Everywhere`
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`
- `Anything Everywhere`
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
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `easy cleanGpuUsed`
- `PreviewImage`
- `SetNode`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `PreviewImage`
- `ImageFromBatch+`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `PreviewImage`
- `LoadImage`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `CR Prompt Text`
- `ImageConcatMulti`
- `VHS_LoadVideo`
- `WanVideoModelLoader`
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `DrawViTPose`
- `PoseAndFaceDetection`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `VHS_VideoCombine`
- `Manual XY Entry Info`
- `SetNode`
- `GetNode`
- `SetNode`

## 知识

覆盖率 **50%**（38/76）

**有卡**：`JWInteger`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`ImageResizeKJv2`、`WanVideoUni3C_embeds`、`GetImageSizeAndCount`、`easy cleanGpuUsed`、`VHS_LoadVideo`、`ImageFromBatch+`、`WanVideoDecode`、`VHS_VideoCombine`、`ImageConcatMulti`、`LoadImage`、`WanVideoSampler`、`CR Prompt Text`、`WanVideoModelLoader`、`OnnxDetectionModelLoader`、`DrawViTPose`、`PoseAndFaceDetection`、`WanVideoAnimateEmbeds`、`Manual XY Entry Info`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeCached、WanVideoVAELoader
