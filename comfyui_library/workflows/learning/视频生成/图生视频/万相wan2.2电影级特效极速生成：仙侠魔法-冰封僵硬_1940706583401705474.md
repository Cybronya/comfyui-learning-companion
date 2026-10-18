---
key: 视频生成/图生视频/万相wan2.2电影级特效极速生成：仙侠魔法-冰封僵硬_1940706583401705474.json
name: 万相wan2.2电影级特效极速生成：仙侠魔法-冰封僵硬_1940706583401705474.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/万相wan2.2电影级特效极速生成：仙侠魔法-冰封僵硬_1940706583401705474.json
hash: 2af1c81b8a703dee
coverage: 1
learned_at: 2026-10-15 22:30:34
nodes: [Int, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, LayerUtility: PurgeVRAM V2, LoadImage, VHS_VideoCombine, VHS_VideoCombine, Int, Int, WanVideoModelLoader, WanVideoBlockSwap, WanVideoTextEncodeSingle, WanVideoTextEncodeSingle, WanVideoApplyNAG, WanVideoDecode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, LoadWanVideoClipTextEncoder, SimpleMath+, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoImageClipEncode, WanVideoEasyCache, WanVideoSampler, Text Multiline, WanVideoLoraSelectMulti]
patterns: []
missing: []
---

# 视频生成/图生视频/万相wan2.2电影级特效极速生成：仙侠魔法-冰封僵硬_1940706583401705474.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1940706583401705474.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（27 个）：
- `Int`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Int`
- `Int`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncodeSingle`
- `WanVideoApplyNAG`
- `WanVideoDecode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `SimpleMath+`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoImageClipEncode`
- `WanVideoEasyCache`
- `WanVideoSampler` ★核心
- `Text Multiline`
- `WanVideoLoraSelectMulti`

## 知识

覆盖率 **100%**（27/27）

**有卡**：`Int`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`LayerUtility: PurgeVRAM V2`、`LoadImage`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoTextEncodeSingle`、`WanVideoApplyNAG`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`SimpleMath+`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoImageClipEncode`、`WanVideoEasyCache`、`WanVideoSampler`、`Text Multiline`、`WanVideoLoraSelectMulti`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoVAELoader、WanVideoTextEncodeSingle
