---
key: 平台全量/【视频万物消除】MiniMax-Remover1.3B（全自动）_1936098803994775553.json
name: 【视频万物消除】MiniMax-Remover1.3B（全自动）_1936098803994775553
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【视频万物消除】MiniMax-Remover1.3B（全自动）_1936098803994775553.json
hash: 0b49d1a6529e8edf
coverage: 0.614286
learned_at: 2026-11-14 01:25:06
nodes: [Anything Everywhere, Anything Everywhere, Note, WanVideoLoraSelect, WanVideoBlockSwap, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, CR String To Number, easy showAnything, GetNode, ImageResize+, SetNode, SetNode, SetNode, VHS_VideoInfoSource, SetNode, VHS_LoadVideo, CR String To Number, Anything Everywhere, ImageBatchGet, BBoxesToSAM2, GetNode, SetNode, GetNode, LayerMask: SAM2VideoUltra, MaskPreview+, ImageCompositeMasked, GetNode, GetNode, VHS_VideoCombine, easy cleanGpuUsed, DownloadAndLoadQwenModel, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSetBlockSwap, WanVideoModelLoader, QwenVLDetection, Note, CR Text, Note, PreviewImage, GrowMaskWithBlur, MaskPreview+, Note, Note, easy clearCacheAll, GetNode, WanVideoEncode, MaskToImage, easy clearCacheAll, MaskToImage, WanVideoEncode, GetNode, Note, Note, easy showAnything, SolidMask, ImageResize+, WanVideoSampler, WanVideoMiniMaxRemoverEmbeds, GetNode, WanVideoTextEncode, WanVideoDecode, SolidMask, LayerColor: AutoBrightness, Note, FluxResolutionNode, CR Text]
patterns: []
missing: []
---

# 平台全量/【视频万物消除】MiniMax-Remover1.3B（全自动）_1936098803994775553.json

> 来源文件 `comfyui_library/workflows/平台全量/【视频万物消除】MiniMax-Remover1.3B（全自动）_1936098803994775553.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（70 个）：
- `Anything Everywhere`
- `Anything Everywhere`
- `Note`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `CR String To Number`
- `easy showAnything`
- `GetNode`
- `ImageResize+`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfoSource`
- `SetNode`
- `VHS_LoadVideo`
- `CR String To Number`
- `Anything Everywhere`
- `ImageBatchGet`
- `BBoxesToSAM2`
- `GetNode`
- `SetNode`
- `GetNode`
- `LayerMask: SAM2VideoUltra`
- `MaskPreview+`
- `ImageCompositeMasked`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `DownloadAndLoadQwenModel`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `QwenVLDetection`
- `Note`
- `CR Text`
- `Note`
- `PreviewImage`
- `GrowMaskWithBlur`
- `MaskPreview+`
- `Note`
- `Note`
- `easy clearCacheAll`
- `GetNode`
- `WanVideoEncode`
- `MaskToImage`
- `easy clearCacheAll`
- `MaskToImage`
- `WanVideoEncode`
- `GetNode`
- `Note`
- `Note`
- `easy showAnything`
- `SolidMask`
- `ImageResize+`
- `WanVideoSampler` ★核心
- `WanVideoMiniMaxRemoverEmbeds`
- `GetNode`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `SolidMask`
- `LayerColor: AutoBrightness`
- `Note`
- `FluxResolutionNode`
- `CR Text`

## 知识

覆盖率 **61%**（43/70）

**有卡**：`WanVideoLoraSelect`、`WanVideoBlockSwap`、`MathExpression|pysssss`、`CR String To Number`、`ImageResize+`、`VHS_VideoInfoSource`、`VHS_LoadVideo`、`ImageBatchGet`、`BBoxesToSAM2`、`LayerMask: SAM2VideoUltra`、`MaskPreview+`、`ImageCompositeMasked`、`VHS_VideoCombine`、`easy cleanGpuUsed`、`DownloadAndLoadQwenModel`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`QwenVLDetection`、`CR Text`、`GrowMaskWithBlur`、`easy clearCacheAll`、`WanVideoEncode`、`MaskToImage`、`SolidMask`、`WanVideoSampler`、`WanVideoMiniMaxRemoverEmbeds`、`WanVideoTextEncode`、`WanVideoDecode`、`LayerColor: AutoBrightness`、`FluxResolutionNode`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、FluxResolutionNode
