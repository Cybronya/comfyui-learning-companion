---
key: 平台全量/Wan2.1VACE图像姿势迁移（K神）_1951625828994068482.json
name: Wan2.1VACE图像姿势迁移（K神）_1951625828994068482
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1VACE图像姿势迁移（K神）_1951625828994068482.json
hash: 18fbc94c3312a42a
coverage: 0.864865
learned_at: 2026-11-14 01:04:40
nodes: [MarkdownNote, MarkdownNote, LoadWanVideoT5TextEncoder, WanVideoTextEncodeSingle, WanVideoVAELoader, MarkdownNote, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoEnhanceAVideo, WanVideoEasyCache, WanVideoSLG, WanVideoVACEEncode, SimpleMath+, WanVideoTorchCompileSettings, WanVideoVACEModelSelect, WanVideoModelLoader, JWInteger, WanVideoSampler, WanVideoExperimentalArgs, PreviewImage, ImageRepeat, ImageResizeKJv2, JWInteger, JWInteger, DepthAnythingPreprocessor, CannyEdgePreprocessor, ImageBlend, DWPreprocessor, OpenposePreprocessor, WanVideoTextEncodeSingle, LoadImage, LoadImage, WanVideoDecode, GetImageRangeFromBatch, easy imageConcat, PreviewImage, SaveImage]
patterns: []
missing: []
---

# 平台全量/Wan2.1VACE图像姿势迁移（K神）_1951625828994068482.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1VACE图像姿势迁移（K神）_1951625828994068482.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（37 个）：
- `MarkdownNote`
- `MarkdownNote`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncodeSingle`
- `WanVideoVAELoader`
- `MarkdownNote`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoEnhanceAVideo`
- `WanVideoEasyCache`
- `WanVideoSLG`
- `WanVideoVACEEncode`
- `SimpleMath+`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `JWInteger`
- `WanVideoSampler` ★核心
- `WanVideoExperimentalArgs`
- `PreviewImage`
- `ImageRepeat`
- `ImageResizeKJv2`
- `JWInteger`
- `JWInteger`
- `DepthAnythingPreprocessor`
- `CannyEdgePreprocessor`
- `ImageBlend`
- `DWPreprocessor`
- `OpenposePreprocessor`
- `WanVideoTextEncodeSingle`
- `LoadImage`
- `LoadImage`
- `WanVideoDecode`
- `GetImageRangeFromBatch`
- `easy imageConcat`
- `PreviewImage`
- `SaveImage`

## 知识

覆盖率 **86%**（32/37）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoTextEncodeSingle`、`WanVideoVAELoader`、`WanVideoApplyNAG`、`WanVideoBlockSwap`、`WanVideoEnhanceAVideo`、`WanVideoEasyCache`、`WanVideoSLG`、`WanVideoVACEEncode`、`SimpleMath+`、`WanVideoTorchCompileSettings`、`WanVideoVACEModelSelect`、`WanVideoModelLoader`、`JWInteger`、`WanVideoSampler`、`WanVideoExperimentalArgs`、`ImageRepeat`、`ImageResizeKJv2`、`DepthAnythingPreprocessor`、`CannyEdgePreprocessor`、`ImageBlend`、`DWPreprocessor`、`OpenposePreprocessor`、`LoadImage`、`WanVideoDecode`、`GetImageRangeFromBatch`、`easy imageConcat`、`SaveImage`

**用到的条目**：LoadImage、CannyEdgePreprocessor、DepthAnythingPreprocessor、OpenposePreprocessor、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncodeSingle
