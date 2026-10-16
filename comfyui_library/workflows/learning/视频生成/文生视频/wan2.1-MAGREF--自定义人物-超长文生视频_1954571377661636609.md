---
key: 视频生成/文生视频/wan2.1-MAGREF--自定义人物-超长文生视频_1954571377661636609.json
name: wan2.1-MAGREF--自定义人物-超长文生视频_1954571377661636609.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1954571377661636609.json
hash: 005da6c1a76258a3
coverage: 0.836364
learned_at: 2026-10-15 22:43:39
nodes: [easy clearCacheAll, WanVideoLoraSelect, ImageFromBatch, easy forLoopEnd, easy batchAnything, GetImageSizeAndCount, WanVideoTextEncode, WanVideoVAELoader, GetNode, GetNode, WanVideoLoraSelect, PreviewImage, MathExpression|pysssss, WanVideoModelLoader, VHS_VideoCombine, CLIPVisionLoader, LoadWanVideoT5TextEncoder, LayerUtility: PurgeVRAM, Text Load Line From File, easy showAnything, easy forLoopStart, ConditionalTextOutput, easy convertAnything, WanVideoImageToVideoEncode, LayerUtility: PurgeVRAM, SetNode, WanVideoBlockSwap, WanVideoDecode, VHS_VideoCombine, WanVideoTorchCompileSettings, ImageSmartSharpen+, SetNode, easy showAnything, easy cleanGpuUsed, WanVideoSampler, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoClipVisionEncode, ImageResizeKJv2, GetImageSize, PreviewImage, PreviewImage, LayerUtility: PurgeVRAM, NewLayer, Text Multiline, Int, CR Image Input Switch, easy imageRemBg, LayerUtility: ImageScaleByAspectRatio V2, Int, Int, LoadImage, EmptyImage, MergeLayers, SimpleMath+]
patterns: []
missing: []
---

# 视频生成/文生视频/wan2.1-MAGREF--自定义人物-超长文生视频_1954571377661636609.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1954571377661636609.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（55 个）：
- `easy clearCacheAll`
- `WanVideoLoraSelect`
- `ImageFromBatch`
- `easy forLoopEnd`
- `easy batchAnything`
- `GetImageSizeAndCount`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `GetNode`
- `GetNode`
- `WanVideoLoraSelect`
- `PreviewImage`
- `MathExpression|pysssss`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `CLIPVisionLoader`
- `LoadWanVideoT5TextEncoder`
- `LayerUtility: PurgeVRAM`
- `Text Load Line From File`
- `easy showAnything`
- `easy forLoopStart`
- `ConditionalTextOutput`
- `easy convertAnything`
- `WanVideoImageToVideoEncode`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `ImageSmartSharpen+`
- `SetNode`
- `easy showAnything`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoClipVisionEncode`
- `ImageResizeKJv2`
- `GetImageSize`
- `PreviewImage`
- `PreviewImage`
- `LayerUtility: PurgeVRAM`
- `NewLayer`
- `Text Multiline`
- `Int`
- `CR Image Input Switch`
- `easy imageRemBg`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `Int`
- `LoadImage`
- `EmptyImage`
- `MergeLayers`
- `SimpleMath+`

## 知识

覆盖率 **84%**（46/55）

**有卡**：`easy clearCacheAll`、`WanVideoLoraSelect`、`ImageFromBatch`、`easy forLoopEnd`、`easy batchAnything`、`GetImageSizeAndCount`、`WanVideoTextEncode`、`WanVideoVAELoader`、`MathExpression|pysssss`、`WanVideoModelLoader`、`VHS_VideoCombine`、`CLIPVisionLoader`、`LoadWanVideoT5TextEncoder`、`LayerUtility: PurgeVRAM`、`Text Load Line From File`、`easy forLoopStart`、`ConditionalTextOutput`、`easy convertAnything`、`WanVideoImageToVideoEncode`、`WanVideoBlockSwap`、`WanVideoDecode`、`WanVideoTorchCompileSettings`、`ImageSmartSharpen+`、`easy cleanGpuUsed`、`WanVideoSampler`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoClipVisionEncode`、`ImageResizeKJv2`、`GetImageSize`、`NewLayer`、`Text Multiline`、`Int`、`CR Image Input Switch`、`easy imageRemBg`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`EmptyImage`、`MergeLayers`、`SimpleMath+`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
