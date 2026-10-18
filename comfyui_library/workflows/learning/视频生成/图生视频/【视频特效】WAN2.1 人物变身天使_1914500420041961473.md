---
key: 视频生成/图生视频/【视频特效】WAN2.1 人物变身天使_1914500420041961473.json
name: 【视频特效】WAN2.1 人物变身天使_1914500420041961473.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【视频特效】WAN2.1 人物变身天使_1914500420041961473.json
hash: 82e0a05dd89fec56
coverage: 1
learned_at: 2026-10-15 22:29:36
nodes: [WanVideoImageClipEncode, WanVideoTeaCache, WanVideoTextEncode, WanVideoBlockSwap, WanVideoLoraSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoClipTextEncoder, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoModelLoader, LayerUtility: PurgeVRAM, WanVideoDecode, LayerUtility: PurgeVRAM, LayerUtility: TextBox, WanVideoSampler, LoadImage, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/【视频特效】WAN2.1 人物变身天使_1914500420041961473.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1914500420041961473.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（17 个）：
- `WanVideoImageClipEncode`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `LayerUtility: PurgeVRAM`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: TextBox`
- `WanVideoSampler` ★核心
- `LoadImage`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`WanVideoImageClipEncode`、`WanVideoTeaCache`、`WanVideoTextEncode`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`LayerUtility: PurgeVRAM`、`WanVideoDecode`、`LayerUtility: TextBox`、`WanVideoSampler`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
