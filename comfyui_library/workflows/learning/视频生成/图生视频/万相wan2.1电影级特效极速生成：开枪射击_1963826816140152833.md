---
key: 视频生成/图生视频/万相wan2.1电影级特效极速生成：开枪射击_1963826816140152833.json
name: 万相wan2.1电影级特效极速生成：开枪射击_1963826816140152833.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1963826816140152833.json
hash: 6ed2eee9cdbde2be
coverage: 1
learned_at: 2026-10-15 22:31:33
nodes: [Int, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, LayerUtility: PurgeVRAM V2, VHS_VideoCombine, Int, Int, WanVideoBlockSwap, WanVideoTextEncodeSingle, WanVideoApplyNAG, WanVideoDecode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, LoadWanVideoClipTextEncoder, SimpleMath+, WanVideoEasyCache, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoImageClipEncode, VHS_VideoCombine, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoLoraSelectMulti, Text Multiline, LoadImage, WanVideoModelLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/万相wan2.1电影级特效极速生成：开枪射击_1963826816140152833.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1963826816140152833.json`

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
- `WanVideoLoraSelectMulti`
- `Text Multiline`
- `LoadImage`
- `WanVideoModelLoader`

## 知识

覆盖率 **100%**（27/27）

**有卡**：`Int`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`LayerUtility: PurgeVRAM V2`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`WanVideoTextEncodeSingle`、`WanVideoApplyNAG`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`SimpleMath+`、`WanVideoEasyCache`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoImageClipEncode`、`WanVideoSampler`、`WanVideoLoraSelectMulti`、`Text Multiline`、`LoadImage`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoVAELoader、WanVideoTextEncodeSingle
