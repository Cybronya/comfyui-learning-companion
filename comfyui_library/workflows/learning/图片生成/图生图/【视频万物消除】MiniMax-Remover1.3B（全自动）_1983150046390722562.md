---
key: 图片生成/图生图/【视频万物消除】MiniMax-Remover1.3B（全自动）_1983150046390722562.json
name: 【视频万物消除】MiniMax-Remover1.3B（全自动）_1983150046390722562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【视频万物消除】MiniMax-Remover1.3B（全自动）_1983150046390722562.json
hash: adf3f15034e37c5c
coverage: 0.614286
learned_at: 2026-10-23 11:51:38
nodes: [Anything Everywhere, Anything Everywhere, Note, WanVideoLoraSelect, WanVideoBlockSwap, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, CR String To Number, easy showAnything, GetNode, ImageResize+, SetNode, SetNode, SetNode, SetNode, CR String To Number, Anything Everywhere, ImageBatchGet, BBoxesToSAM2, SetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, easy cleanGpuUsed, DownloadAndLoadQwenModel, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSetBlockSwap, WanVideoModelLoader, QwenVLDetection, Note, GrowMaskWithBlur, Note, Note, easy clearCacheAll, MaskToImage, WanVideoEncode, GetNode, Note, Note, easy showAnything, SolidMask, ImageResize+, WanVideoSampler, SolidMask, Note, CR Text, VHS_VideoInfoSource, FluxResolutionNode, VHS_LoadVideo, GetNode, WanVideoDecode, LayerColor: AutoBrightness, LayerMask: SAM2VideoUltra, Note, CR Text, MaskPreview+, PreviewImage, MaskToImage, easy clearCacheAll, MaskPreview+, ImageCompositeMasked, GetNode, WanVideoTextEncode, WanVideoEncode, WanVideoMiniMaxRemoverEmbeds, GetNode]
patterns: []
missing: []
---

# 图片生成/图生图/【视频万物消除】MiniMax-Remover1.3B（全自动）_1983150046390722562.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【视频万物消除】MiniMax-Remover1.3B（全自动）_1983150046390722562.json`

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
- `SetNode`
- `CR String To Number`
- `Anything Everywhere`
- `ImageBatchGet`
- `BBoxesToSAM2`
- `SetNode`
- `GetNode`
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
- `GrowMaskWithBlur`
- `Note`
- `Note`
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
- `SolidMask`
- `Note`
- `CR Text`
- `VHS_VideoInfoSource`
- `FluxResolutionNode`
- `VHS_LoadVideo`
- `GetNode`
- `WanVideoDecode`
- `LayerColor: AutoBrightness`
- `LayerMask: SAM2VideoUltra`
- `Note`
- `CR Text`
- `MaskPreview+`
- `PreviewImage`
- `MaskToImage`
- `easy clearCacheAll`
- `MaskPreview+`
- `ImageCompositeMasked`
- `GetNode`
- `WanVideoTextEncode`
- `WanVideoEncode`
- `WanVideoMiniMaxRemoverEmbeds`
- `GetNode`

## 知识

覆盖率 **61%**（43/70）

**有卡**：`WanVideoLoraSelect`、`WanVideoBlockSwap`、`MathExpression|pysssss`、`CR String To Number`、`ImageResize+`、`ImageBatchGet`、`BBoxesToSAM2`、`VHS_VideoCombine`、`easy cleanGpuUsed`、`DownloadAndLoadQwenModel`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`QwenVLDetection`、`GrowMaskWithBlur`、`easy clearCacheAll`、`MaskToImage`、`WanVideoEncode`、`SolidMask`、`WanVideoSampler`、`CR Text`、`VHS_VideoInfoSource`、`FluxResolutionNode`、`VHS_LoadVideo`、`WanVideoDecode`、`LayerColor: AutoBrightness`、`LayerMask: SAM2VideoUltra`、`MaskPreview+`、`ImageCompositeMasked`、`WanVideoTextEncode`、`WanVideoMiniMaxRemoverEmbeds`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoEncode、WanVideoLoraSelect、FluxResolutionNode
