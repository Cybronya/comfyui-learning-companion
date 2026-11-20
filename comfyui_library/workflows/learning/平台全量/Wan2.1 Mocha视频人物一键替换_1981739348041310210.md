---
key: 平台全量/Wan2.1 Mocha视频人物一键替换_1981739348041310210.json
name: Wan2.1 Mocha视频人物一键替换_1981739348041310210
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1 Mocha视频人物一键替换_1981739348041310210.json
hash: fb4197a91138df53
coverage: 0.64
learned_at: 2026-11-14 01:04:24
nodes: [GetNode, WanVideoSampler, GetNode, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, SetNode, WanVideoTextEncodeCached, MochaEmbeds, GetImageRangeFromBatch, GetNode, WanVideoVAELoader, SetNode, GetNode, GetNode, GetNode, LayerMask: SegmentAnythingUltra V2, GrowMask, SetNode, ImpactInt, VHS_VideoCombine, WanVideoDecode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, ImageResizeKJv2, ImageResizeKJv2, SetNode, FaceAnalysisModels, FaceBoundingBox, SetNode, VHS_VideoInfoSource, PreviewImage, PreviewImage, MarkdownNote, MarkdownNote, MarkdownNote, LoadImage, GetNode, MaskPreview+, BlockifyMask, easy cleanGpuUsed, VHS_VideoCombine, PDIMAGE_LongerSize, ImageConcanate, ImageConcanate, ImpactInt, VHS_LoadVideo, MathExpression|pysssss]
patterns: []
missing: []
---

# 平台全量/Wan2.1 Mocha视频人物一键替换_1981739348041310210.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1 Mocha视频人物一键替换_1981739348041310210.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（50 个）：
- `GetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoTextEncodeCached`
- `MochaEmbeds`
- `GetImageRangeFromBatch`
- `GetNode`
- `WanVideoVAELoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerMask: SegmentAnythingUltra V2`
- `GrowMask`
- `SetNode`
- `ImpactInt`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `SetNode`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `SetNode`
- `VHS_VideoInfoSource`
- `PreviewImage`
- `PreviewImage`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `GetNode`
- `MaskPreview+`
- `BlockifyMask`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `PDIMAGE_LongerSize`
- `ImageConcanate`
- `ImageConcanate`
- `ImpactInt`
- `VHS_LoadVideo`
- `MathExpression|pysssss`

## 知识

覆盖率 **64%**（32/50）

**有卡**：`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoTextEncodeCached`、`MochaEmbeds`、`GetImageRangeFromBatch`、`WanVideoVAELoader`、`LayerMask: SegmentAnythingUltra V2`、`GrowMask`、`ImpactInt`、`VHS_VideoCombine`、`WanVideoDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`FaceAnalysisModels`、`FaceBoundingBox`、`VHS_VideoInfoSource`、`LoadImage`、`MaskPreview+`、`BlockifyMask`、`easy cleanGpuUsed`、`PDIMAGE_LongerSize`、`ImageConcanate`、`VHS_LoadVideo`、`MathExpression|pysssss`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoSampler、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、ImageResizeKJv2
