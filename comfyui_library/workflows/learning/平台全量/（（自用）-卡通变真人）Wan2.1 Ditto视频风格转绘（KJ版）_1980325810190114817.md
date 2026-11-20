---
key: 平台全量/（（自用）-卡通变真人）Wan2.1 Ditto视频风格转绘（KJ版）_1980325810190114817.json
name: （（自用）-卡通变真人）Wan2.1 Ditto视频风格转绘（KJ版）_1980325810190114817
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/（（自用）-卡通变真人）Wan2.1 Ditto视频风格转绘（KJ版）_1980325810190114817.json
hash: 23929776c55d8a89
coverage: 0.777778
learned_at: 2026-11-14 02:54:19
nodes: [LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTextEncode, Note, Note, Note, WanVideoBlockSwap, JWInteger, Int, LayerUtility: ImageScaleByAspectRatio V2, WanVideoModelLoader, WanVideoLoraSelect, WanVideoVACEEncode, Reroute, JWInteger, Note, WanVideoVACEModelSelect, PrimitiveNode, CR Prompt Text, WanVideoSampler, SaveImage, TT_img_enc, SaveImage, WanVideoDecode, VHS_VideoInfo, TT_img_enc_v2, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/（（自用）-卡通变真人）Wan2.1 Ditto视频风格转绘（KJ版）_1980325810190114817.json

> 来源文件 `comfyui_library/workflows/平台全量/（（自用）-卡通变真人）Wan2.1 Ditto视频风格转绘（KJ版）_1980325810190114817.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

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
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoVACEEncode`
- `Reroute`
- `JWInteger`
- `Note`
- `WanVideoVACEModelSelect`
- `PrimitiveNode`
- `CR Prompt Text`
- `WanVideoSampler` ★核心
- `SaveImage`
- `TT_img_enc`
- `SaveImage`
- `WanVideoDecode`
- `VHS_VideoInfo`
- `TT_img_enc_v2`
- `VHS_LoadVideo`

## 知识

覆盖率 **78%**（21/27）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoBlockSwap`、`JWInteger`、`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoVACEEncode`、`WanVideoVACEModelSelect`、`CR Prompt Text`、`WanVideoSampler`、`SaveImage`、`TT_img_enc`、`WanVideoDecode`、`VHS_VideoInfo`、`TT_img_enc_v2`、`VHS_LoadVideo`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelect、CR Prompt Text
