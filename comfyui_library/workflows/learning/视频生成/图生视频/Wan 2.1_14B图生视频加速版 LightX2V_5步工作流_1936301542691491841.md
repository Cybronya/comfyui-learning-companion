---
key: 视频生成/图生视频/Wan 2.1_14B图生视频加速版 LightX2V_5步工作流_1936301542691491841.json
name: Wan 2.1_14B图生视频加速版 LightX2V_5步工作流_1936301542691491841.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan 2.1_14B图生视频加速版 LightX2V_5步工作流_1936301542691491841.json
hash: 4e44f043797db089
coverage: 0.482759
learned_at: 2026-10-15 22:30:25
nodes: [WanVideoTextEncode, Note, Note, LoadWanVideoT5TextEncoder, GetNode, SetNode, SetNode, WanVideoVAELoader, Note, Note, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, Note, VHS_VideoCombine, Note, Note, Int, MathExpression|pysssss, UpscaleModelLoader, Note, SetNode, LoadImage, GetNode, WanVideoImageToVideoEncode, GetNode, GetNode, WanVideoClipVisionEncode, LayerUtility: ImageScaleByAspectRatio V2, easy cleanGpuUsed, CLIPVisionLoader, easy showAnything, RH_OneShot_Prompter, Note, SetNode, Text, ImageUpscaleWithModel, GetNode, GetNode, SetNode, VHS_VideoCombine, WanVideoDecode, GetNode, GetNode, WanVideoSampler, WanVideoModelLoader, Note, Note, Note, Int, Note, Note, WanVideoLoraSelect, SetNode, Fast Groups Bypasser (rgthree), Int]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan 2.1_14B图生视频加速版 LightX2V_5步工作流_1936301542691491841.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1936301542691491841.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（58 个）：
- `WanVideoTextEncode`
- `Note`
- `Note`
- `LoadWanVideoT5TextEncoder`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoVAELoader`
- `Note`
- `Note`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `Note`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `Int`
- `MathExpression|pysssss`
- `UpscaleModelLoader`
- `Note`
- `SetNode`
- `LoadImage`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy cleanGpuUsed`
- `CLIPVisionLoader`
- `easy showAnything`
- `RH_OneShot_Prompter`
- `Note`
- `SetNode`
- `Text`
- `ImageUpscaleWithModel`
- `GetNode`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `Note`
- `Note`
- `Note`
- `Int`
- `Note`
- `Note`
- `WanVideoLoraSelect`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `Int`

## 知识

覆盖率 **48%**（28/58）

**有卡**：`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`VHS_VideoCombine`、`Int`、`MathExpression|pysssss`、`UpscaleModelLoader`、`LoadImage`、`WanVideoImageToVideoEncode`、`WanVideoClipVisionEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy cleanGpuUsed`、`CLIPVisionLoader`、`RH_OneShot_Prompter`、`Text`、`ImageUpscaleWithModel`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoLoraSelect`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
