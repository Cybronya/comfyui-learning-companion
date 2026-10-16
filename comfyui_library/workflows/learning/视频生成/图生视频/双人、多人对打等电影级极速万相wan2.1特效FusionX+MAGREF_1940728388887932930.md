---
key: 视频生成/图生视频/双人、多人对打等电影级极速万相wan2.1特效FusionX+MAGREF_1940728388887932930.json
name: 双人、多人对打等电影级极速万相wan2.1特效FusionX+MAGREF_1940728388887932930.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1940728388887932930.json
hash: 43e574fb2cfcf879
coverage: 1
learned_at: 2026-10-15 22:30:34
nodes: [RH_OneShot_Prompter, WanVideoApplyNAG, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoTextEncodeSingle, WanVideoTextEncodeSingle, WanVideoVAELoader, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoMagCache, LoadWanVideoClipTextEncoder, WanVideoModelLoader, WanVideoImageClipEncode, Int, WanVideoLoraSelect, Int, Int, SimpleMath+, WanVideoDecode, WanVideoSLG, WanVideoSampler, DownloadAndLoadGIMMVFIModel, VHS_VideoCombine, GIMMVFI_interpolate, LayerUtility: PurgeVRAM V2, VHS_VideoCombine, WanVideoLoraSelect, WanVideoLoraSelect, LoadImage, Text Multiline]
patterns: []
missing: []
---

# 视频生成/图生视频/双人、多人对打等电影级极速万相wan2.1特效FusionX+MAGREF_1940728388887932930.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1940728388887932930.json`

## 结构

**生成流程**：Model → Condition → Sampling → Other

**节点**（30 个）：
- `RH_OneShot_Prompter`
- `WanVideoApplyNAG`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncodeSingle`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoMagCache`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoModelLoader`
- `WanVideoImageClipEncode`
- `Int`
- `WanVideoLoraSelect`
- `Int`
- `Int`
- `SimpleMath+`
- `WanVideoDecode`
- `WanVideoSLG`
- `WanVideoSampler` ★核心
- `DownloadAndLoadGIMMVFIModel`
- `VHS_VideoCombine`
- `GIMMVFI_interpolate`
- `LayerUtility: PurgeVRAM V2`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadImage`
- `Text Multiline`

## 知识

覆盖率 **100%**（30/30）

**有卡**：`RH_OneShot_Prompter`、`WanVideoApplyNAG`、`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`WanVideoTextEncodeSingle`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoMagCache`、`LoadWanVideoClipTextEncoder`、`WanVideoModelLoader`、`WanVideoImageClipEncode`、`Int`、`WanVideoLoraSelect`、`SimpleMath+`、`WanVideoDecode`、`WanVideoSLG`、`WanVideoSampler`、`DownloadAndLoadGIMMVFIModel`、`VHS_VideoCombine`、`GIMMVFI_interpolate`、`LayerUtility: PurgeVRAM V2`、`LoadImage`、`Text Multiline`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoVAELoader、WanVideoTextEncodeSingle
