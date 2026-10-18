---
key: 视频生成/图生视频/万相wan2.2电影级特效极速生成：仙侠魔法-聚气_1940711079049670657.json
name: 万相wan2.2电影级特效极速生成：仙侠魔法-聚气_1940711079049670657.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/万相wan2.2电影级特效极速生成：仙侠魔法-聚气_1940711079049670657.json
hash: 1f5f7e9b0bc1c902
coverage: 1
learned_at: 2026-10-15 22:30:34
nodes: [Int, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, LayerUtility: PurgeVRAM V2, LoadImage, VHS_VideoCombine, Int, Int, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoBlockSwap, Text Multiline, WanVideoTextEncodeSingle, WanVideoTextEncodeSingle, WanVideoApplyNAG, WanVideoDecode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, LoadWanVideoClipTextEncoder, SimpleMath+, WanVideoEasyCache, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoImageClipEncode, VHS_VideoCombine, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/万相wan2.2电影级特效极速生成：仙侠魔法-聚气_1940711079049670657.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1940711079049670657.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（27 个）：
- `Int`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `VHS_VideoCombine`
- `Int`
- `Int`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `Text Multiline`
- `WanVideoTextEncodeSingle`
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

## 知识

覆盖率 **100%**（27/27）

**有卡**：`Int`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`LayerUtility: PurgeVRAM V2`、`LoadImage`、`VHS_VideoCombine`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`Text Multiline`、`WanVideoTextEncodeSingle`、`WanVideoApplyNAG`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`SimpleMath+`、`WanVideoEasyCache`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoImageClipEncode`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoVAELoader、WanVideoTextEncodeSingle
