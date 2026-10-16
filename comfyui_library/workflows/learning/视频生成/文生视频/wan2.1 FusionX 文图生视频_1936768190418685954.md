---
key: 视频生成/文生视频/wan2.1 FusionX 文图生视频_1936768190418685954.json
name: wan2.1 FusionX 文图生视频_1936768190418685954.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1936768190418685954.json
hash: bd53cc60cdf47a0a
coverage: 0.484848
learned_at: 2026-10-15 22:43:29
nodes: [SetNode, PrimitiveString, StringConcatenate, StringConcatenate, PrimitiveString, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Mute / Bypass Relay (rgthree), WanVideoEmptyEmbeds, Mute / Bypass Relay (rgthree), easy seed, Note, Mute / Bypass Repeater (rgthree), WanVideoModelLoader, WanVideoLoraSelect, SetNode, Fast Groups Muter (rgthree), WanVideoImageClipEncode, GetNode, GetNode, GetNode, GetNode, GetNode, easy int, SetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, LoadImage, easy int, SetNode, WanVideoTextEncodeSingle, PrimitiveStringMultiline, WanVideoTorchCompileSettings, WanVideoVAELoader, SetNode, LoadWanVideoT5TextEncoder, SetNode, WanVideoBlockSwap, LoadWanVideoClipTextEncoder, SetNode, WanVideoLoraSelect, WanVideoModelLoader, Mute / Bypass Repeater (rgthree), Any Switch (rgthree), SetNode, VHS_VideoCombine, PrimitiveString, WanVideoTextEncodeSingle, WanVideoSampler, WanVideoApplyNAG, Any Switch (rgthree), WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoSLG, WanVideoExperimentalArgs, WanVideoDecode, SetNode, SetNode]
patterns: []
missing: []
---

# 视频生成/文生视频/wan2.1 FusionX 文图生视频_1936768190418685954.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1936768190418685954.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（66 个）：
- `SetNode`
- `PrimitiveString`
- `StringConcatenate`
- `StringConcatenate`
- `PrimitiveString`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Mute / Bypass Relay (rgthree)`
- `WanVideoEmptyEmbeds`
- `Mute / Bypass Relay (rgthree)`
- `easy seed`
- `Note`
- `Mute / Bypass Repeater (rgthree)`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `SetNode`
- `Fast Groups Muter (rgthree)`
- `WanVideoImageClipEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy int`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `LoadImage`
- `easy int`
- `SetNode`
- `WanVideoTextEncodeSingle`
- `PrimitiveStringMultiline`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `WanVideoBlockSwap`
- `LoadWanVideoClipTextEncoder` ★核心
- `SetNode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `Mute / Bypass Repeater (rgthree)`
- `Any Switch (rgthree)`
- `SetNode`
- `VHS_VideoCombine`
- `PrimitiveString`
- `WanVideoTextEncodeSingle`
- `WanVideoSampler` ★核心
- `WanVideoApplyNAG`
- `Any Switch (rgthree)`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoDecode`
- `SetNode`
- `SetNode`

## 知识

覆盖率 **48%**（32/66）

**有卡**：`StringConcatenate`、`Mute / Bypass Relay (rgthree)`、`WanVideoEmptyEmbeds`、`easy seed`、`Mute / Bypass Repeater (rgthree)`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoImageClipEncode`、`easy int`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`WanVideoTextEncodeSingle`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`LoadWanVideoClipTextEncoder`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoApplyNAG`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoDecode`

**用到的条目**：LoadImage、WanVideoSampler、easy seed、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoVAELoader
