---
key: 视频生成/图生视频/MAGREF+Phantom+lightx2v一致性图生视频海外商单专用抖胸特效万相wan2.1_1927606759882383362.json
name: MAGREF+Phantom+lightx2v一致性图生视频海外商单专用抖胸特效万相wan2.1_1927606759882383362.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1927606759882383362.json
hash: e9b1b77f2dca896b
coverage: 1
learned_at: 2026-10-15 22:29:55
nodes: [LoadImage, LayerUtility: PurgeVRAM V2, Int, DownloadAndLoadGIMMVFIModel, VHS_VideoCombine, GIMMVFI_interpolate, VHS_VideoCombine, WanVideoTextEncodeSingle, WanVideoTextEncodeSingle, WanVideoApplyNAG, ImageResizeKJ, SimpleMath+, Int, Int, WanVideoEnhanceAVideo, LoadWanVideoClipTextEncoder, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSLG, WanVideoDecode, WanVideoImageClipEncode, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, WanVideoSampler, CR Text, WanVideoBlockSwap, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/图生视频/MAGREF+Phantom+lightx2v一致性图生视频海外商单专用抖胸特效万相wan2.1_1927606759882383362.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1927606759882383362.json`

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
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncodeSingle`
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
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `CR Text`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`

## 知识

覆盖率 **100%**（29/29）

**有卡**：`LoadImage`、`LayerUtility: PurgeVRAM V2`、`Int`、`DownloadAndLoadGIMMVFIModel`、`VHS_VideoCombine`、`GIMMVFI_interpolate`、`WanVideoTextEncodeSingle`、`WanVideoApplyNAG`、`ImageResizeKJ`、`SimpleMath+`、`WanVideoEnhanceAVideo`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoSLG`、`WanVideoDecode`、`WanVideoImageClipEncode`、`WanVideoExperimentalArgs`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoSampler`、`CR Text`、`WanVideoBlockSwap`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoVAELoader、WanVideoTextEncodeSingle
