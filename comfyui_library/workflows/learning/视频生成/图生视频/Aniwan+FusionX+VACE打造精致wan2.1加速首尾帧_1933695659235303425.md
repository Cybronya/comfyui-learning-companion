---
key: 视频生成/图生视频/Aniwan+FusionX+VACE打造精致wan2.1加速首尾帧_1933695659235303425.json
name: Aniwan+FusionX+VACE打造精致wan2.1加速首尾帧_1933695659235303425.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1933695659235303425.json
hash: 705c3dec416509c5
coverage: 1
learned_at: 2026-10-15 22:30:14
nodes: [LoadImage, LayerUtility: PurgeVRAM V2, DownloadAndLoadGIMMVFIModel, LoadWanVideoT5TextEncoder, LayerUtility: PurgeVRAM V2, VHS_VideoCombine, LoadInvSRModels, LayerUtility: PurgeVRAM V2, InvSRSampler, PMRF, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, GIMMVFI_interpolate, WanVideoEnhanceAVideo, CR Text, WanVideoApplyNAG, WanVideoSLG, WanVideoTextEncodeSingle, WanVideoTextEncodeSingle, LoadImage, Int, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler, WanVideoEasyCache, WanVideoModelLoader, WanVideoVACEModelSelect, LayerUtility: ImageScaleByAspectRatio V2, WanVideoDecode, WanVideoExperimentalArgs, WanVideoSetRadialAttention, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoVAELoader, WanVideoVACEEncode, WanVideoVACEStartToEndFrame, SimpleMath+, Int]
patterns: []
missing: []
---

# 视频生成/图生视频/Aniwan+FusionX+VACE打造精致wan2.1加速首尾帧_1933695659235303425.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1933695659235303425.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（38 个）：
- `LoadImage`
- `LayerUtility: PurgeVRAM V2`
- `DownloadAndLoadGIMMVFIModel`
- `LoadWanVideoT5TextEncoder`
- `LayerUtility: PurgeVRAM V2`
- `VHS_VideoCombine`
- `LoadInvSRModels`
- `LayerUtility: PurgeVRAM V2`
- `InvSRSampler` ★核心
- `PMRF`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GIMMVFI_interpolate`
- `WanVideoEnhanceAVideo`
- `CR Text`
- `WanVideoApplyNAG`
- `WanVideoSLG`
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncodeSingle`
- `LoadImage`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心
- `WanVideoEasyCache`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoSetRadialAttention`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `WanVideoVACEEncode`
- `WanVideoVACEStartToEndFrame`
- `SimpleMath+`
- `Int`

## 知识

覆盖率 **100%**（38/38）

**有卡**：`LoadImage`、`LayerUtility: PurgeVRAM V2`、`DownloadAndLoadGIMMVFIModel`、`LoadWanVideoT5TextEncoder`、`VHS_VideoCombine`、`LoadInvSRModels`、`InvSRSampler`、`PMRF`、`GIMMVFI_interpolate`、`WanVideoEnhanceAVideo`、`CR Text`、`WanVideoApplyNAG`、`WanVideoSLG`、`WanVideoTextEncodeSingle`、`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoEasyCache`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`WanVideoDecode`、`WanVideoExperimentalArgs`、`WanVideoSetRadialAttention`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`WanVideoVACEEncode`、`WanVideoVACEStartToEndFrame`、`SimpleMath+`

**用到的条目**：LoadImage、WanVideoSampler、InvSRSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、WanVideoVACEEncode
