---
key: 平台全量/Wan2.1 Ditto视频风格转绘_1980640342271770625.json
name: Wan2.1 Ditto视频风格转绘_1980640342271770625
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1 Ditto视频风格转绘_1980640342271770625.json
hash: b89b10ed4982ddc4
coverage: 0.75
learned_at: 2026-11-14 01:04:24
nodes: [SetNode, SetNode, WanVideoVACEModelSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoTorchCompileSettings, WanVideoBlockSwap, GetImageSizeAndCount, LayerUtility: ImageScaleByAspectRatio V2, WanVideoTextEncode, WanVideoSLG, WanVideoSampler, SetNode, GetNode, GetNode, GetNode, VHS_LoadVideo, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine, ImageScaleToTotalPixels, JWInteger, ImageConcatMulti, CR Text, WanVideoVACEEncode, MarkdownNote]
patterns: []
missing: []
---

# 平台全量/Wan2.1 Ditto视频风格转绘_1980640342271770625.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1 Ditto视频风格转绘_1980640342271770625.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（28 个）：
- `SetNode`
- `SetNode`
- `WanVideoVACEModelSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `GetImageSizeAndCount`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoTextEncode`
- `WanVideoSLG`
- `WanVideoSampler` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageScaleToTotalPixels`
- `JWInteger`
- `ImageConcatMulti`
- `CR Text`
- `WanVideoVACEEncode`
- `MarkdownNote`

## 知识

覆盖率 **75%**（21/28）

**有卡**：`WanVideoVACEModelSelect`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`GetImageSizeAndCount`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoTextEncode`、`WanVideoSLG`、`WanVideoSampler`、`VHS_LoadVideo`、`WanVideoDecode`、`VHS_VideoCombine`、`ImageScaleToTotalPixels`、`JWInteger`、`ImageConcatMulti`、`CR Text`、`WanVideoVACEEncode`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelect、GetImageSizeAndCount
