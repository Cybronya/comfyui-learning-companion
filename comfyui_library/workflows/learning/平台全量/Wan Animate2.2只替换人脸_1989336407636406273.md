---
key: 平台全量/Wan Animate2.2只替换人脸_1989336407636406273.json
name: Wan Animate2.2只替换人脸_1989336407636406273
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan Animate2.2只替换人脸_1989336407636406273.json
hash: 78f064942fa3140b
coverage: 0.5
learned_at: 2026-11-14 01:04:03
nodes: [SetNode, SetNode, SetNode, DrawMaskOnImage, JWInteger, SetNode, JWInteger, SetNode, JWInteger, WanVideoSetLoRAs, MarkdownNote, WanVideoBlockSwap, GetNode, WanVideoClipVisionEncode, SetNode, CLIPVisionLoader, Anything Everywhere, WanVideoSetBlockSwap, WanVideoVAELoader, Anything Everywhere, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, WanVideoTextEncodeCached, WanVideoEncode, WanVideoUni3C_ControlnetLoader, ImageResizeKJv2, WanVideoUni3C_embeds, SetNode, GetNode, GetNode, GetImageSizeAndCount, GetNode, GetNode, PreviewImage, easy cleanGpuUsed, WanVideoAnimateEmbeds, VHS_LoadVideo, Manual XY Entry Info, PreviewImage, VHS_VideoCombine, WanVideoSampler, PreviewImage, ImageFromBatch+, GetNode, LayerMask: MaskPreview, SetNode, GetNode, GetNode, GetNode, APersonMaskGenerator, BlockifyMask, GetNode, GetNode, GetNode, FaceProcessorLoader, ImageResizeKJv2, SetNode, VHS_VideoCombine, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoLoraSelectMulti, ApplyFaceProcessor, PreviewImage, ImageConcatMulti, GetNode, WanVideoDecode, ImageConcatMulti, ImageConcatMulti, PreviewImage, VHS_VideoCombine, LoadImage, VHS_LoadVideo, CR Prompt Text, GetNode, VHS_VideoCombine, SetNode, SetNode, DrawViTPose, GetNode, GetNode, PoseAndFaceDetection, OnnxDetectionModelLoader]
patterns: []
missing: []
---

# 平台全量/Wan Animate2.2只替换人脸_1989336407636406273.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan Animate2.2只替换人脸_1989336407636406273.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（90 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `DrawMaskOnImage`
- `JWInteger`
- `SetNode`
- `JWInteger`
- `SetNode`
- `JWInteger`
- `WanVideoSetLoRAs`
- `MarkdownNote`
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
- `VHS_LoadVideo`
- `Manual XY Entry Info`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `PreviewImage`
- `ImageFromBatch+`
- `GetNode`
- `LayerMask: MaskPreview`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `APersonMaskGenerator`
- `BlockifyMask`
- `GetNode`
- `GetNode`
- `GetNode`
- `FaceProcessorLoader`
- `ImageResizeKJv2`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `ApplyFaceProcessor`
- `PreviewImage`
- `ImageConcatMulti`
- `GetNode`
- `WanVideoDecode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `PreviewImage`
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_LoadVideo`
- `CR Prompt Text`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `DrawViTPose`
- `GetNode`
- `GetNode`
- `PoseAndFaceDetection`
- `OnnxDetectionModelLoader`

## 知识

覆盖率 **50%**（45/90）

**有卡**：`DrawMaskOnImage`、`JWInteger`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`ImageResizeKJv2`、`WanVideoUni3C_embeds`、`GetImageSizeAndCount`、`easy cleanGpuUsed`、`WanVideoAnimateEmbeds`、`VHS_LoadVideo`、`Manual XY Entry Info`、`VHS_VideoCombine`、`WanVideoSampler`、`ImageFromBatch+`、`LayerMask: MaskPreview`、`APersonMaskGenerator`、`BlockifyMask`、`FaceProcessorLoader`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`ApplyFaceProcessor`、`ImageConcatMulti`、`WanVideoDecode`、`LoadImage`、`CR Prompt Text`、`DrawViTPose`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeCached、WanVideoVAELoader
