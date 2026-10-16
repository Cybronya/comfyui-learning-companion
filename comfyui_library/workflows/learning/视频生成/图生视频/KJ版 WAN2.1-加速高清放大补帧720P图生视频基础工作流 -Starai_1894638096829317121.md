---
key: 视频生成/图生视频/KJ版 WAN2.1-加速高清放大补帧720P图生视频基础工作流 -Starai_1894638096829317121.json
name: KJ版 WAN2.1-加速高清放大补帧720P图生视频基础工作流 -Starai_1894638096829317121.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1894638096829317121.json
hash: ecc4f4b989a8b6a9
coverage: 0.813559
learned_at: 2026-10-15 22:29:16
nodes: [ImageResizeAdvanced, MathExpression|pysssss, CM_IntToNumber, CM_NumberToInt, MathExpression|pysssss, CM_IntToNumber, CM_NumberToInt, MathExpression|pysssss, MathExpression|pysssss, ImageResizeAdvanced, RH_Captioner, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoSampler, WanVideoDecode, WanVideoTorchCompileSettings, WanVideoTextEncode, PrimitiveInt, PrimitiveInt, ImageResize+, easy imageSize, ImpactSwitch, UpscaleModelLoader, easy cleanGpuUsed, LayerUtility: PurgeVRAM, FILM VFI, easy cleanGpuUsed, ImageResizeKJ, ImageUpscaleWithModel, UpscaleModelLoader, easy cleanGpuUsed, ImageUpscaleWithModel, WanVideoImageClipEncode, WanVideoVAELoader, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, Int, JjkText, Int, Note Plus (mtb), Note, easy textSwitch, Note, LoadImage, JjkText, JjkText, JjkText, JjkText, ShowText|pysssss, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoTeaCache, WanVideoModelLoader, CR String To Number, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/KJ版 WAN2.1-加速高清放大补帧720P图生视频基础工作流 -Starai_1894638096829317121.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1894638096829317121.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（59 个）：
- `ImageResizeAdvanced`
- `MathExpression|pysssss`
- `CM_IntToNumber`
- `CM_NumberToInt`
- `MathExpression|pysssss`
- `CM_IntToNumber`
- `CM_NumberToInt`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `ImageResizeAdvanced`
- `RH_Captioner`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoTorchCompileSettings`
- `WanVideoTextEncode`
- `PrimitiveInt`
- `PrimitiveInt`
- `ImageResize+`
- `easy imageSize`
- `ImpactSwitch`
- `UpscaleModelLoader`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM`
- `FILM VFI`
- `easy cleanGpuUsed`
- `ImageResizeKJ`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `easy cleanGpuUsed`
- `ImageUpscaleWithModel`
- `WanVideoImageClipEncode`
- `WanVideoVAELoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `Int`
- `JjkText`
- `Int`
- `Note Plus (mtb)`
- `Note`
- `easy textSwitch`
- `Note`
- `LoadImage`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `ShowText|pysssss`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoTeaCache`
- `WanVideoModelLoader`
- `CR String To Number`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **81%**（48/59）

**有卡**：`ImageResizeAdvanced`、`MathExpression|pysssss`、`CM_IntToNumber`、`CM_NumberToInt`、`RH_Captioner`、`easy cleanGpuUsed`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoTorchCompileSettings`、`WanVideoTextEncode`、`ImageResize+`、`easy imageSize`、`UpscaleModelLoader`、`LayerUtility: PurgeVRAM`、`FILM VFI`、`ImageResizeKJ`、`ImageUpscaleWithModel`、`WanVideoImageClipEncode`、`WanVideoVAELoader`、`LoadWanVideoClipTextEncoder`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`Int`、`Note Plus (mtb)`、`easy textSwitch`、`LoadImage`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoTeaCache`、`WanVideoModelLoader`、`CR String To Number`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
