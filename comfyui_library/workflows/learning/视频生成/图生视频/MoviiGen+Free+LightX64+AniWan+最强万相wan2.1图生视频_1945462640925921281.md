---
key: 视频生成/图生视频/MoviiGen+Free+LightX64+AniWan+最强万相wan2.1图生视频_1945462640925921281.json
name: MoviiGen+Free+LightX64+AniWan+最强万相wan2.1图生视频_1945462640925921281.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MoviiGen+Free+LightX64+AniWan+最强万相wan2.1图生视频_1945462640925921281.json
hash: e1a951568d117dc8
coverage: 1
learned_at: 2026-10-15 22:30:42
nodes: [WanVideoVAELoader, LayerUtility: PurgeVRAM V2, WanVideoDecode, WanVideoExperimentalArgs, WanVideoEnhanceAVideo, LoadImage, CLIPVisionLoader, WanVideoClipVisionEncode, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, RH_OneShot_Prompter, WanVideoImageToVideoEncode, WanVideoSLG, SimpleMath+, WanVideoApplyNAG, WanVideoTextEncodeSingle, WanVideoTextEncodeSingle, VHS_VideoCombine, WanVideoFreeInitArgs, WanVideoSampler, WanVideoEasyCache, WanVideoBlockSwap, Text Multiline, JWInteger, JWInteger, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/MoviiGen+Free+LightX64+AniWan+最强万相wan2.1图生视频_1945462640925921281.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1945462640925921281.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（28 个）：
- `WanVideoVAELoader`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoEnhanceAVideo`
- `LoadImage`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `RH_OneShot_Prompter`
- `WanVideoImageToVideoEncode`
- `WanVideoSLG`
- `SimpleMath+`
- `WanVideoApplyNAG`
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncodeSingle`
- `VHS_VideoCombine`
- `WanVideoFreeInitArgs`
- `WanVideoSampler` ★核心
- `WanVideoEasyCache`
- `WanVideoBlockSwap`
- `Text Multiline`
- `JWInteger`
- `JWInteger`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`

## 知识

覆盖率 **100%**（28/28）

**有卡**：`WanVideoVAELoader`、`LayerUtility: PurgeVRAM V2`、`WanVideoDecode`、`WanVideoExperimentalArgs`、`WanVideoEnhanceAVideo`、`LoadImage`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`RH_OneShot_Prompter`、`WanVideoImageToVideoEncode`、`WanVideoSLG`、`SimpleMath+`、`WanVideoApplyNAG`、`WanVideoTextEncodeSingle`、`VHS_VideoCombine`、`WanVideoFreeInitArgs`、`WanVideoSampler`、`WanVideoEasyCache`、`WanVideoBlockSwap`、`Text Multiline`、`JWInteger`、`WanVideoLoraSelect`、`WanVideoModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeSingle
