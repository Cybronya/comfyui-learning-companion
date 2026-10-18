---
key: 视频生成/图生视频/万相wan2.2电影级特效极速生成：万物爆炸_1963808996464611329.json
name: 万相wan2.2电影级特效极速生成：万物爆炸_1963808996464611329.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/万相wan2.2电影级特效极速生成：万物爆炸_1963808996464611329.json
hash: eea7e01efad5e9c8
coverage: 1
learned_at: 2026-10-15 22:31:33
nodes: [DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, VHS_VideoCombine, Int, Int, WanVideoBlockSwap, WanVideoApplyNAG, WanVideoDecode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, LoadWanVideoClipTextEncoder, SimpleMath+, WanVideoEasyCache, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoImageClipEncode, VHS_VideoCombine, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoTextEncodeSingle, Int, WanVideoModelLoader, WanVideoLoraSelectMulti, LoadImage, Text Multiline, LayerUtility: PurgeVRAM V2]
patterns: []
missing: []
---

# 视频生成/图生视频/万相wan2.2电影级特效极速生成：万物爆炸_1963808996464611329.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1963808996464611329.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（27 个）：
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `VHS_VideoCombine`
- `Int`
- `Int`
- `WanVideoBlockSwap`
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
- `WanVideoTextEncodeSingle`
- `Int`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `LoadImage`
- `Text Multiline`
- `LayerUtility: PurgeVRAM V2`

## 知识

覆盖率 **100%**（27/27）

**有卡**：`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`VHS_VideoCombine`、`Int`、`WanVideoBlockSwap`、`WanVideoApplyNAG`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`SimpleMath+`、`WanVideoEasyCache`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoImageClipEncode`、`WanVideoSampler`、`WanVideoTextEncodeSingle`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`LoadImage`、`Text Multiline`、`LayerUtility: PurgeVRAM V2`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoVAELoader、WanVideoTextEncodeSingle
