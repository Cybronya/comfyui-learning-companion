---
key: 平台全量/（卡通变真人）Wan2.1 Ditto视频风格转绘（KJI版）_1980318107703160834.json
name: （卡通变真人）Wan2.1 Ditto视频风格转绘（KJI版）_1980318107703160834
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/（卡通变真人）Wan2.1 Ditto视频风格转绘（KJI版）_1980318107703160834.json
hash: 8ecb93f4593d25fc
coverage: 0.777778
learned_at: 2026-11-14 02:53:55
nodes: [LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTextEncode, Note, Note, Note, WanVideoBlockSwap, JWInteger, Int, ImageConcatMulti, WanVideoDecode, LayerUtility: ImageScaleByAspectRatio V2, PDIMAGE_LongerSize, WanVideoModelLoader, WanVideoLoraSelect, WanVideoVACEEncode, Reroute, VHS_VideoInfo, VHS_VideoCombine, VHS_VideoCombine, JWInteger, Note, WanVideoVACEModelSelect, PrimitiveNode, CR Prompt Text, VHS_LoadVideo, WanVideoSampler]
patterns: []
missing: []
---

# 平台全量/（卡通变真人）Wan2.1 Ditto视频风格转绘（KJI版）_1980318107703160834.json

> 来源文件 `comfyui_library/workflows/平台全量/（卡通变真人）Wan2.1 Ditto视频风格转绘（KJI版）_1980318107703160834.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（27 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `Note`
- `Note`
- `Note`
- `WanVideoBlockSwap`
- `JWInteger`
- `Int`
- `ImageConcatMulti`
- `WanVideoDecode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PDIMAGE_LongerSize`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoVACEEncode`
- `Reroute`
- `VHS_VideoInfo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `JWInteger`
- `Note`
- `WanVideoVACEModelSelect`
- `PrimitiveNode`
- `CR Prompt Text`
- `VHS_LoadVideo`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **78%**（21/27）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoBlockSwap`、`JWInteger`、`Int`、`ImageConcatMulti`、`WanVideoDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`PDIMAGE_LongerSize`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoVACEEncode`、`VHS_VideoInfo`、`VHS_VideoCombine`、`WanVideoVACEModelSelect`、`CR Prompt Text`、`VHS_LoadVideo`、`WanVideoSampler`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelect、CR Prompt Text
