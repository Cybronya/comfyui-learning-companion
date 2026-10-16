---
key: 视频生成/图生视频/Wan 2.1_14B首尾帧图生视频超详细基础工作流_1935669711310872577.json
name: Wan 2.1_14B首尾帧图生视频超详细基础工作流_1935669711310872577.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1935669711310872577.json
hash: ba563af2b947b8bc
coverage: 0.53125
learned_at: 2026-10-15 22:30:23
nodes: [SetNode, WanVideoTextEncode, Note, LoadWanVideoT5TextEncoder, GetNode, SetNode, SetNode, Note, Note, WanVideoTorchCompileSettings, VHS_VideoCombine, Note, Note, Int, WanVideoVACEModelSelect, Note, Int, UpscaleModelLoader, WanVideoExperimentalArgs, WanVideoEnhanceAVideo, Note, GetNode, WanVideoSLG, Note, WanVideoSampler, GetNode, GetNode, WanVideoDecode, ImageUpscaleWithModel, GetNode, MathExpression|pysssss, WanVideoBlockSwap, WanVideoModelLoader, WanVideoVAELoader, VHS_VideoCombine, Note, Note, WanVideoTeaCache, Note, LoadImage, LoadImage, Note, Int, WanVideoVACEEncode, GetImageSize+, WanVideoVACEStartToEndFrame, GetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, RH_OneShot_Prompter, easy cleanGpuUsed, easy showAnything, SetNode, Note, Text, SetNode, SetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, ImageConcanate, ImageConcanate, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan 2.1_14B首尾帧图生视频超详细基础工作流_1935669711310872577.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1935669711310872577.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（64 个）：
- `SetNode`
- `WanVideoTextEncode`
- `Note`
- `LoadWanVideoT5TextEncoder`
- `GetNode`
- `SetNode`
- `SetNode`
- `Note`
- `Note`
- `WanVideoTorchCompileSettings`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `Int`
- `WanVideoVACEModelSelect`
- `Note`
- `Int`
- `UpscaleModelLoader`
- `WanVideoExperimentalArgs`
- `WanVideoEnhanceAVideo`
- `Note`
- `GetNode`
- `WanVideoSLG`
- `Note`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `ImageUpscaleWithModel`
- `GetNode`
- `MathExpression|pysssss`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `WanVideoTeaCache`
- `Note`
- `LoadImage`
- `LoadImage`
- `Note`
- `Int`
- `WanVideoVACEEncode`
- `GetImageSize+`
- `WanVideoVACEStartToEndFrame`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RH_OneShot_Prompter`
- `easy cleanGpuUsed`
- `easy showAnything`
- `SetNode`
- `Note`
- `Text`
- `SetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `ImageConcanate`
- `ImageConcanate`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **53%**（34/64）

**有卡**：`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoTorchCompileSettings`、`VHS_VideoCombine`、`Int`、`WanVideoVACEModelSelect`、`UpscaleModelLoader`、`WanVideoExperimentalArgs`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoSampler`、`WanVideoDecode`、`ImageUpscaleWithModel`、`MathExpression|pysssss`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoTeaCache`、`LoadImage`、`WanVideoVACEEncode`、`GetImageSize+`、`WanVideoVACEStartToEndFrame`、`LayerUtility: ImageScaleByAspectRatio V2`、`RH_OneShot_Prompter`、`easy cleanGpuUsed`、`Text`、`ImageConcanate`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、ImageUpscaleWithModel
