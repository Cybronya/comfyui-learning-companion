---
key: 视频生成/图生视频/万相wan2.1电影级特效极速生成：万物开花_1940735459234627585.json
name: 万相wan2.1电影级特效极速生成：万物开花_1940735459234627585.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1940735459234627585.json
hash: 5af8b9e470f0b383
coverage: 1
learned_at: 2026-10-15 22:30:34
nodes: [Int, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, LayerUtility: PurgeVRAM V2, VHS_VideoCombine, Int, Int, WanVideoBlockSwap, WanVideoTextEncodeSingle, WanVideoApplyNAG, WanVideoDecode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, LoadWanVideoClipTextEncoder, SimpleMath+, WanVideoEasyCache, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoImageClipEncode, VHS_VideoCombine, WanVideoSampler, WanVideoTextEncodeSingle, LoadImage, Text Multiline, WanVideoModelLoader, WanVideoLoraSelectMulti]
patterns: []
missing: []
---

# 视频生成/图生视频/万相wan2.1电影级特效极速生成：万物开花_1940735459234627585.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1940735459234627585.json`

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
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`

## 知识

覆盖率 **100%**（27/27）

**有卡**：`Int`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`LayerUtility: PurgeVRAM V2`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`WanVideoTextEncodeSingle`、`WanVideoApplyNAG`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`SimpleMath+`、`WanVideoEasyCache`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoImageClipEncode`、`WanVideoSampler`、`LoadImage`、`Text Multiline`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoVAELoader、WanVideoTextEncodeSingle
