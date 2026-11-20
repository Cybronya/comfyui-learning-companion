---
key: 平台全量/Wan Animate2.2动物主体替换_1976653610421567490.json
name: Wan Animate2.2动物主体替换_1976653610421567490
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan Animate2.2动物主体替换_1976653610421567490.json
hash: 9e4577433ded739a
coverage: 0.487179
learned_at: 2026-11-14 01:04:02
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, WanVideoSetLoRAs, MarkdownNote, WanVideoTorchCompileSettings, WanVideoBlockSwap, Anything Everywhere, WanVideoSetBlockSwap, WanVideoVAELoader, Anything Everywhere, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, WanVideoTextEncodeCached, GetNode, PreviewImage, easy cleanGpuUsed, SetNode, ImageResizeKJv2, Manual XY Entry Info, GetNode, GetNode, WanVideoDecode, ImageConcatMulti, VHS_VideoCombine, ImageConcatMulti, VHS_VideoCombine, PreviewImage, VHS_LoadVideo, JWInteger, JWInteger, PreviewImage, PreviewImage, WanVideoLoraSelectMulti, GetNode, AnimalPosePreprocessor, LayerUtility: PurgeVRAM, LoadImage, CR Prompt Text, WanVideoModelLoader, JWInteger, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoSampler, SetNode, CLIPVisionLoader, GetNode, SetNode, ImageFromBatch+, GetNode, PointsEditor, SetNode, GetNode, SeCVideoSegmentation, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, SeCModelLoader, SetNode, BlockifyMask, DrawMaskOnImage, DrawMaskOnImage]
patterns: []
missing: []
---

# 平台全量/Wan Animate2.2动物主体替换_1976653610421567490.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan Animate2.2动物主体替换_1976653610421567490.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（78 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `MarkdownNote`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `Anything Everywhere`
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`
- `Anything Everywhere`
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
- `GetNode`
- `PreviewImage`
- `easy cleanGpuUsed`
- `SetNode`
- `ImageResizeKJv2`
- `Manual XY Entry Info`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `PreviewImage`
- `VHS_LoadVideo`
- `JWInteger`
- `JWInteger`
- `PreviewImage`
- `PreviewImage`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `AnimalPosePreprocessor`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `CR Prompt Text`
- `WanVideoModelLoader`
- `JWInteger`
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoSampler` ★核心
- `SetNode`
- `CLIPVisionLoader`
- `GetNode`
- `SetNode`
- `ImageFromBatch+`
- `GetNode`
- `PointsEditor`
- `SetNode`
- `GetNode`
- `SeCVideoSegmentation`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SeCModelLoader`
- `SetNode`
- `BlockifyMask`
- `DrawMaskOnImage`
- `DrawMaskOnImage`

## 知识

覆盖率 **49%**（38/78）

**有卡**：`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`easy cleanGpuUsed`、`ImageResizeKJv2`、`Manual XY Entry Info`、`WanVideoDecode`、`ImageConcatMulti`、`VHS_VideoCombine`、`VHS_LoadVideo`、`JWInteger`、`WanVideoLoraSelectMulti`、`AnimalPosePreprocessor`、`LayerUtility: PurgeVRAM`、`LoadImage`、`CR Prompt Text`、`WanVideoModelLoader`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`CLIPVisionLoader`、`ImageFromBatch+`、`PointsEditor`、`SeCVideoSegmentation`、`SeCModelLoader`、`BlockifyMask`、`DrawMaskOnImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
