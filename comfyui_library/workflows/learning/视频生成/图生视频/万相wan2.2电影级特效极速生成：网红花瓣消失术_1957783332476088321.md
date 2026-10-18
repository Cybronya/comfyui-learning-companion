---
key: 视频生成/图生视频/万相wan2.2电影级特效极速生成：网红花瓣消失术_1957783332476088321.json
name: 万相wan2.2电影级特效极速生成：网红花瓣消失术_1957783332476088321.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/万相wan2.2电影级特效极速生成：网红花瓣消失术_1957783332476088321.json
hash: d3862249a1266269
coverage: 1
learned_at: 2026-10-15 22:31:18
nodes: [Int, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, LayerUtility: PurgeVRAM V2, VHS_VideoCombine, Int, Int, WanVideoModelLoader, WanVideoBlockSwap, WanVideoTextEncodeSingle, WanVideoApplyNAG, WanVideoDecode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, LoadWanVideoClipTextEncoder, SimpleMath+, WanVideoEasyCache, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoImageClipEncode, VHS_VideoCombine, WanVideoSampler, WanVideoTextEncodeSingle, LoadImage, Text Multiline, WanVideoLoraSelectMulti]
patterns: []
missing: []
---

# 视频生成/图生视频/万相wan2.2电影级特效极速生成：网红花瓣消失术_1957783332476088321.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1957783332476088321.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（27 个）：
- `Int`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `LayerUtility: PurgeVRAM V2`
- `VHS_VideoCombine`
- `Int`
- `Int`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeSingle`
- `WanVideoApplyNAG`
- `WanVideoDecode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `SimpleMath+`
- `WanVideoEasyCache`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoImageClipEncode`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeSingle`
- `LoadImage`
- `Text Multiline`
- `WanVideoLoraSelectMulti`

## 知识

覆盖率 **100%**（27/27）

**有卡**：`Int`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`LayerUtility: PurgeVRAM V2`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoTextEncodeSingle`、`WanVideoApplyNAG`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`SimpleMath+`、`WanVideoEasyCache`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoImageClipEncode`、`WanVideoSampler`、`LoadImage`、`Text Multiline`、`WanVideoLoraSelectMulti`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoVAELoader、WanVideoTextEncodeSingle
