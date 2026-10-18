---
key: 视频生成/图生视频/MAGREF+Phantom+lightx2v一致性图生视频海外商单专用吻屏特效万相wan2.1_1927678754154528770.json
name: MAGREF+Phantom+lightx2v一致性图生视频海外商单专用吻屏特效万相wan2.1_1927678754154528770.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MAGREF+Phantom+lightx2v一致性图生视频海外商单专用吻屏特效万相wan2.1_1927678754154528770.json
hash: fd7105e0c6475c48
coverage: 1
learned_at: 2026-10-15 22:29:55
nodes: [LoadImage, LayerUtility: PurgeVRAM V2, Int, DownloadAndLoadGIMMVFIModel, VHS_VideoCombine, GIMMVFI_interpolate, VHS_VideoCombine, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoTextEncodeSingle, CR Text, WanVideoApplyNAG, ImageResizeKJ, SimpleMath+, Int, Int, WanVideoEnhanceAVideo, LoadWanVideoClipTextEncoder, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSLG, WanVideoDecode, WanVideoImageClipEncode, WanVideoExperimentalArgs, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/图生视频/MAGREF+Phantom+lightx2v一致性图生视频海外商单专用吻屏特效万相wan2.1_1927678754154528770.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1927678754154528770.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（29 个）：
- `LoadImage`
- `LayerUtility: PurgeVRAM V2`
- `Int`
- `DownloadAndLoadGIMMVFIModel`
- `VHS_VideoCombine`
- `GIMMVFI_interpolate`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncodeSingle`
- `CR Text`
- `WanVideoApplyNAG`
- `ImageResizeKJ`
- `SimpleMath+`
- `Int`
- `Int`
- `WanVideoEnhanceAVideo`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSLG`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoExperimentalArgs`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`

## 知识

覆盖率 **100%**（29/29）

**有卡**：`LoadImage`、`LayerUtility: PurgeVRAM V2`、`Int`、`DownloadAndLoadGIMMVFIModel`、`VHS_VideoCombine`、`GIMMVFI_interpolate`、`WanVideoSampler`、`WanVideoTextEncodeSingle`、`CR Text`、`WanVideoApplyNAG`、`ImageResizeKJ`、`SimpleMath+`、`WanVideoEnhanceAVideo`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoSLG`、`WanVideoDecode`、`WanVideoImageClipEncode`、`WanVideoExperimentalArgs`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelect`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoVAELoader、WanVideoTextEncodeSingle
