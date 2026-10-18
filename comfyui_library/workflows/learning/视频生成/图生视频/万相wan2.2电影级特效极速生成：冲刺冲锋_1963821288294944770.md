---
key: 视频生成/图生视频/万相wan2.2电影级特效极速生成：冲刺冲锋_1963821288294944770.json
name: 万相wan2.2电影级特效极速生成：冲刺冲锋_1963821288294944770.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/万相wan2.2电影级特效极速生成：冲刺冲锋_1963821288294944770.json
hash: 75b50161fce68b80
coverage: 1
learned_at: 2026-10-15 22:31:33
nodes: [Int, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, LayerUtility: PurgeVRAM V2, VHS_VideoCombine, Int, Int, WanVideoModelLoader, WanVideoBlockSwap, WanVideoTextEncodeSingle, WanVideoApplyNAG, WanVideoDecode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, LoadWanVideoClipTextEncoder, SimpleMath+, WanVideoEasyCache, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoImageClipEncode, VHS_VideoCombine, WanVideoSampler, WanVideoTextEncodeSingle, LoadImage, WanVideoLoraSelectMulti, Text Multiline]
patterns: []
missing: []
---

# 视频生成/图生视频/万相wan2.2电影级特效极速生成：冲刺冲锋_1963821288294944770.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1963821288294944770.json`

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
- `WanVideoLoraSelectMulti`
- `Text Multiline`

## 知识

覆盖率 **100%**（27/27）

**有卡**：`Int`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`LayerUtility: PurgeVRAM V2`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoTextEncodeSingle`、`WanVideoApplyNAG`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`SimpleMath+`、`WanVideoEasyCache`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoImageClipEncode`、`WanVideoSampler`、`LoadImage`、`WanVideoLoraSelectMulti`、`Text Multiline`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoVAELoader、WanVideoTextEncodeSingle
