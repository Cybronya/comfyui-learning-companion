---
key: 平台全量/Wan2.1ditto视频风格转绘_1981590967713185793.json
name: Wan2.1ditto视频风格转绘_1981590967713185793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1ditto视频风格转绘_1981590967713185793.json
hash: 36bc54762037b2fd
coverage: 0.769231
learned_at: 2026-11-14 01:04:45
nodes: [LayerUtility: ImageScaleByAspectRatio V2, WanVideoVACEEncode, WanVideoBlockSwap, WanVideoVACEModelSelect, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, Note, PDIMAGE_LongerSize, WanVideoDecode, Reroute, WanVideoLoraSelect, VHS_VideoInfo, JWInteger, Note, Note, Note, WanVideoVAELoader, JWInteger, CR Prompt Text, VHS_LoadVideo, PrimitiveNode]
patterns: []
missing: []
---

# 平台全量/Wan2.1ditto视频风格转绘_1981590967713185793.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1ditto视频风格转绘_1981590967713185793.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（26 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoVACEEncode`
- `WanVideoBlockSwap`
- `WanVideoVACEModelSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Note`
- `PDIMAGE_LongerSize`
- `WanVideoDecode`
- `Reroute`
- `WanVideoLoraSelect`
- `VHS_VideoInfo`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `WanVideoVAELoader`
- `JWInteger`
- `CR Prompt Text`
- `VHS_LoadVideo`
- `PrimitiveNode`

## 知识

覆盖率 **77%**（20/26）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoVACEEncode`、`WanVideoBlockSwap`、`WanVideoVACEModelSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoTextEncode`、`WanVideoSampler`、`ImageConcatMulti`、`VHS_VideoCombine`、`PDIMAGE_LongerSize`、`WanVideoDecode`、`WanVideoLoraSelect`、`VHS_VideoInfo`、`JWInteger`、`WanVideoVAELoader`、`CR Prompt Text`、`VHS_LoadVideo`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelect、CR Prompt Text
