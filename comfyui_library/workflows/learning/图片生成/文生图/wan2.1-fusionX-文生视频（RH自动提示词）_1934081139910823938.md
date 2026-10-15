---
key: 图片生成/文生图/wan2.1-fusionX-文生视频（RH自动提示词）_1934081139910823938.json
name: wan2.1-fusionX-文生视频（RH自动提示词）_1934081139910823938
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.1-fusionX-文生视频（RH自动提示词）_1934081139910823938.json
hash: 4ffe8143a0df8fbf
coverage: 0.714286
learned_at: 2026-10-15 22:27:57
nodes: [GIMMVFI_interpolate, ImageScaleToMegapixels, UpscaleModelLoader, WanVideoDecode, GetNode, WanVideoSampler, WanVideoExperimentalArgs, WanVideoSLG, WanVideoEnhanceAVideo, GetNode, SetNode, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoTorchCompileSettings, GetNode, DownloadAndLoadGIMMVFIModel, VHS_VideoCombine, WanVideoEmptyEmbeds, WanVideoTeaCache, WanVideoTextEncodeSingle, LoadWanVideoT5TextEncoder, WanVideoModelLoader, SetNode, WanVideoVAELoader, SetNode, CR Text Concatenate, WanVideoTextEncodeSingle, RH_Prompter, ShowText|pysssss, ImpactSwitch, CR Text, Note, CR Text, CR Text, Note]
patterns: []
missing: []
---

# 图片生成/文生图/wan2.1-fusionX-文生视频（RH自动提示词）_1934081139910823938.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.1-fusionX-文生视频（RH自动提示词）_1934081139910823938.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（35 个）：
- `GIMMVFI_interpolate`
- `ImageScaleToMegapixels`
- `UpscaleModelLoader`
- `WanVideoDecode`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `GetNode`
- `SetNode`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `GetNode`
- `DownloadAndLoadGIMMVFIModel`
- `VHS_VideoCombine`
- `WanVideoEmptyEmbeds`
- `WanVideoTeaCache`
- `WanVideoTextEncodeSingle`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `CR Text Concatenate`
- `WanVideoTextEncodeSingle`
- `RH_Prompter`
- `ShowText|pysssss`
- `ImpactSwitch`
- `CR Text`
- `Note`
- `CR Text`
- `CR Text`
- `Note`

## 知识

覆盖率 **71%**（25/35）

**有卡**：`GIMMVFI_interpolate`、`ImageScaleToMegapixels`、`UpscaleModelLoader`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoExperimentalArgs`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoApplyNAG`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`DownloadAndLoadGIMMVFIModel`、`VHS_VideoCombine`、`WanVideoEmptyEmbeds`、`WanVideoTeaCache`、`WanVideoTextEncodeSingle`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoVAELoader`、`CR Text Concatenate`、`RH_Prompter`、`CR Text`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、UpscaleModelLoader、UpscaleModelLoader、RH_Prompter
