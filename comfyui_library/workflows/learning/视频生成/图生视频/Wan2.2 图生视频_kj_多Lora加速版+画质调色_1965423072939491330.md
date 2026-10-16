---
key: 视频生成/图生视频/Wan2.2 图生视频_kj_多Lora加速版+画质调色_1965423072939491330.json
name: Wan2.2 图生视频_kj_多Lora加速版+画质调色_1965423072939491330.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1965423072939491330.json
hash: 885f21d4f9b9d167
coverage: 0.945946
learned_at: 2026-10-15 22:31:37
nodes: [WanVideoLoraSelectMulti, WanVideoVAELoader, WanVideoDecode, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoEnhanceAVideo, WanVideoTextEncode, LoadWanVideoT5TextEncoder, Display Any (rgthree), LayerUtility: PurgeVRAM, ColorMatch, LayerUtility: PurgeVRAM, WanVideoSLG, WanVideoLoraSelectMulti, VHS_VideoCombine, Text Concatenate, INTConstant, INTConstant, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoSampler, Wan22PromptSelector, ImpactInt, ImpactInt, easy globalSeed, WanVideoImageToVideoEncode, MathExpression_UTK, ImpactInt, LoadImage, CR Text, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, ImageResizeKJv2, WanVideoLoraSelect, easy showAnything, PreviewImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 图生视频_kj_多Lora加速版+画质调色_1965423072939491330.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1965423072939491330.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（37 个）：
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoEnhanceAVideo`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `Display Any (rgthree)`
- `LayerUtility: PurgeVRAM`
- `ColorMatch`
- `LayerUtility: PurgeVRAM`
- `WanVideoSLG`
- `WanVideoLoraSelectMulti`
- `VHS_VideoCombine`
- `Text Concatenate`
- `INTConstant`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `Wan22PromptSelector`
- `ImpactInt`
- `ImpactInt`
- `easy globalSeed`
- `WanVideoImageToVideoEncode`
- `MathExpression_UTK`
- `ImpactInt`
- `LoadImage`
- `CR Text`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `ImageResizeKJv2`
- `WanVideoLoraSelect`
- `easy showAnything`
- `PreviewImage`

## 知识

覆盖率 **95%**（35/37）

**有卡**：`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`WanVideoDecode`、`WanVideoBlockSwap`、`WanVideoEnhanceAVideo`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`Display Any (rgthree)`、`LayerUtility: PurgeVRAM`、`ColorMatch`、`WanVideoSLG`、`VHS_VideoCombine`、`Text Concatenate`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`Wan22PromptSelector`、`ImpactInt`、`easy globalSeed`、`WanVideoImageToVideoEncode`、`MathExpression_UTK`、`LoadImage`、`CR Text`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`ImageResizeKJv2`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、easy globalSeed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
