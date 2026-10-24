---
key: 图片生成/图生图/wan2.1-fusionX-图生视频（RH自动提示词）_1934133372832632834.json
name: wan2.1-fusionX-图生视频（RH自动提示词）_1934133372832632834
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.1-fusionX-图生视频（RH自动提示词）_1934133372832632834.json
hash: a0bac976e5c5911c
coverage: 0.630435
learned_at: 2026-10-23 11:45:49
nodes: [GIMMVFI_interpolate, WanVideoDecode, GetNode, WanVideoClipVisionEncode, SetNode, GetNode, WanVideoBlockSwap, WanVideoModelLoader, DownloadAndLoadGIMMVFIModel, CLIPVisionLoader, SetNode, SetNode, WanVideoVAELoader, GetNode, UpscaleModelLoader, GetNode, WanVideoImageToVideoEncode, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, ImageScaleToMegapixels, WanVideoTextEncodeSingle, WanVideoTeaCache, WanVideoTextEncodeSingle, WanVideoSampler, ImageResizeKJ, ShowText|pysssss, WanVideoTextEncode, WanVideoApplyNAG, ImpactSwitch, SetNode, LoadImage, SetNode, LoadWanVideoT5TextEncoder, SetNode, GetNode, CR Text, RH_Captioner, CR Text Concatenate, ShowText|pysssss, RH_Prompter, VHS_VideoCombine, Note, GetNode, Int, Note]
patterns: []
missing: []
---

# 图片生成/图生图/wan2.1-fusionX-图生视频（RH自动提示词）_1934133372832632834.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.1-fusionX-图生视频（RH自动提示词）_1934133372832632834.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（46 个）：
- `GIMMVFI_interpolate`
- `WanVideoDecode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `SetNode`
- `GetNode`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `DownloadAndLoadGIMMVFIModel`
- `CLIPVisionLoader`
- `SetNode`
- `SetNode`
- `WanVideoVAELoader`
- `GetNode`
- `UpscaleModelLoader`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `ImageScaleToMegapixels`
- `WanVideoTextEncodeSingle`
- `WanVideoTeaCache`
- `WanVideoTextEncodeSingle`
- `WanVideoSampler` ★核心
- `ImageResizeKJ`
- `ShowText|pysssss`
- `WanVideoTextEncode`
- `WanVideoApplyNAG`
- `ImpactSwitch`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `GetNode`
- `CR Text`
- `RH_Captioner`
- `CR Text Concatenate`
- `ShowText|pysssss`
- `RH_Prompter`
- `VHS_VideoCombine`
- `Note`
- `GetNode`
- `Int`
- `Note`

## 知识

覆盖率 **63%**（29/46）

**有卡**：`GIMMVFI_interpolate`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`DownloadAndLoadGIMMVFIModel`、`CLIPVisionLoader`、`WanVideoVAELoader`、`UpscaleModelLoader`、`WanVideoImageToVideoEncode`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`ImageScaleToMegapixels`、`WanVideoTextEncodeSingle`、`WanVideoTeaCache`、`WanVideoSampler`、`ImageResizeKJ`、`WanVideoTextEncode`、`WanVideoApplyNAG`、`LoadImage`、`LoadWanVideoT5TextEncoder`、`CR Text`、`RH_Captioner`、`CR Text Concatenate`、`RH_Prompter`、`VHS_VideoCombine`、`Int`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
