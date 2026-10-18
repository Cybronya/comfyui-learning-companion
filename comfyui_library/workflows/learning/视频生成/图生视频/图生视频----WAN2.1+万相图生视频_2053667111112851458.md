---
key: 视频生成/图生视频/图生视频----WAN2.1+万相图生视频_2053667111112851458.json
name: 图生视频----WAN2.1+万相图生视频_2053667111112851458.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频----WAN2.1+万相图生视频_2053667111112851458.json
hash: 99923730e5bcded7
coverage: 0.824561
learned_at: 2026-10-15 22:37:42
nodes: [WanVideoModelLoader, easy cleanGpuUsed, LoadWanVideoT5TextEncoder, ImageResizeAdvanced, JjkText, RH_Captioner, Bjornulf_ShowStringText, JjkText, JjkText, Note _O, Int, easy cleanGpuUsed, LoadWanVideoClipTextEncoder, WanVideoVAELoader, WanVideoEnhanceAVideo, WanVideoTextEncode, easy textSwitch, Reroute, WanVideoTeaCache, WanVideoExperimentalArgs, WanVideoSLG, easy cleanGpuUsed, WanVideoSampler, FILM VFI, WanVideoDecode, WanVideoBlockSwap, MathExpression|pysssss, ImageResizeKJ, WanVideoImageClipEncode, PrimitiveInt, MathExpression|pysssss, MathExpression|pysssss, easy showAnything, PrimitiveInt, CM_NumberToInt, CM_IntToNumber, easy showAnything, CM_IntToNumber, MathExpression|pysssss, UpscaleModelLoader, easy cleanGpuUsed, ImageUpscaleWithModel, ImageUpscaleWithModel, easy cleanGpuUsed, easy cleanGpuUsed, LoadImage, ImpactSwitch, Int, Note _O, CR String To Number, ImageResizeAdvanced, CM_NumberToInt, VHS_VideoCombine, ImageResize+, UpscaleModelLoader, VHS_VideoCombine, JjkText]
patterns: []
missing: []
---

# 视频生成/图生视频/图生视频----WAN2.1+万相图生视频_2053667111112851458.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2053667111112851458.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（57 个）：
- `WanVideoModelLoader`
- `easy cleanGpuUsed`
- `LoadWanVideoT5TextEncoder`
- `ImageResizeAdvanced`
- `JjkText`
- `RH_Captioner`
- `Bjornulf_ShowStringText`
- `JjkText`
- `JjkText`
- `Note _O`
- `Int`
- `easy cleanGpuUsed`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `WanVideoEnhanceAVideo`
- `WanVideoTextEncode`
- `easy textSwitch`
- `Reroute`
- `WanVideoTeaCache`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `FILM VFI`
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `MathExpression|pysssss`
- `ImageResizeKJ`
- `WanVideoImageClipEncode`
- `PrimitiveInt`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `easy showAnything`
- `PrimitiveInt`
- `CM_NumberToInt`
- `CM_IntToNumber`
- `easy showAnything`
- `CM_IntToNumber`
- `MathExpression|pysssss`
- `UpscaleModelLoader`
- `easy cleanGpuUsed`
- `ImageUpscaleWithModel`
- `ImageUpscaleWithModel`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LoadImage`
- `ImpactSwitch`
- `Int`
- `Note _O`
- `CR String To Number`
- `ImageResizeAdvanced`
- `CM_NumberToInt`
- `VHS_VideoCombine`
- `ImageResize+`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `JjkText`

## 知识

覆盖率 **82%**（47/57）

**有卡**：`WanVideoModelLoader`、`easy cleanGpuUsed`、`LoadWanVideoT5TextEncoder`、`ImageResizeAdvanced`、`RH_Captioner`、`Bjornulf_ShowStringText`、`Note _O`、`Int`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`WanVideoEnhanceAVideo`、`WanVideoTextEncode`、`easy textSwitch`、`WanVideoTeaCache`、`WanVideoExperimentalArgs`、`WanVideoSLG`、`WanVideoSampler`、`FILM VFI`、`WanVideoDecode`、`WanVideoBlockSwap`、`MathExpression|pysssss`、`ImageResizeKJ`、`WanVideoImageClipEncode`、`CM_NumberToInt`、`CM_IntToNumber`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`LoadImage`、`CR String To Number`、`VHS_VideoCombine`、`ImageResize+`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
