---
key: 视频生成/文生视频/【美女背影】wan2.1 I2V 14Bi2v 走路背影_1929716786508500994.json
name: 【美女背影】wan2.1 I2V 14Bi2v 走路背影_1929716786508500994.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1929716786508500994.json
hash: 276124b6d841154a
coverage: 0.818182
learned_at: 2026-10-15 22:43:25
nodes: [easy cleanGpuUsed, UpscaleModelLoader, easy cleanGpuUsed, ImageUpscaleWithModel, JjkText, JjkText, JjkText, ImpactSwitch, ImageResizeAdvanced, Int, easy textSwitch, JjkText, MathExpression|pysssss, CR String To Number, easy showAnything, CM_IntToNumber, MathExpression|pysssss, CM_NumberToInt, PrimitiveInt, easy showAnything, MathExpression|pysssss, CM_NumberToInt, MathExpression|pysssss, PrimitiveInt, ImageResizeAdvanced, CM_IntToNumber, Int, easy cleanGpuUsed, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoTextEncode, easy cleanGpuUsed, LoadWanVideoClipTextEncoder, WanVideoVAELoader, WanVideoImageClipEncode, ImageResize+, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoExperimentalArgs, WanVideoSLG, WanVideoSampler, WanVideoDecode, VHS_VideoCombine, easy cleanGpuUsed, FILM VFI, VHS_VideoCombine, ImageResizeKJ, easy cleanGpuUsed, ImageUpscaleWithModel, Fast Groups Bypasser (rgthree), UpscaleModelLoader, WD14Tagger|pysssss, WanVideoLoraSelect, LoadImage]
patterns: []
missing: []
---

# 视频生成/文生视频/【美女背影】wan2.1 I2V 14Bi2v 走路背影_1929716786508500994.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1929716786508500994.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（55 个）：
- `easy cleanGpuUsed`
- `UpscaleModelLoader`
- `easy cleanGpuUsed`
- `ImageUpscaleWithModel`
- `JjkText`
- `JjkText`
- `JjkText`
- `ImpactSwitch`
- `ImageResizeAdvanced`
- `Int`
- `easy textSwitch`
- `JjkText`
- `MathExpression|pysssss`
- `CR String To Number`
- `easy showAnything`
- `CM_IntToNumber`
- `MathExpression|pysssss`
- `CM_NumberToInt`
- `PrimitiveInt`
- `easy showAnything`
- `MathExpression|pysssss`
- `CM_NumberToInt`
- `MathExpression|pysssss`
- `PrimitiveInt`
- `ImageResizeAdvanced`
- `CM_IntToNumber`
- `Int`
- `easy cleanGpuUsed`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `easy cleanGpuUsed`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `WanVideoImageClipEncode`
- `ImageResize+`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `FILM VFI`
- `VHS_VideoCombine`
- `ImageResizeKJ`
- `easy cleanGpuUsed`
- `ImageUpscaleWithModel`
- `Fast Groups Bypasser (rgthree)`
- `UpscaleModelLoader`
- `WD14Tagger|pysssss`
- `WanVideoLoraSelect`
- `LoadImage`

## 知识

覆盖率 **82%**（45/55）

**有卡**：`easy cleanGpuUsed`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`ImageResizeAdvanced`、`Int`、`easy textSwitch`、`MathExpression|pysssss`、`CR String To Number`、`CM_IntToNumber`、`CM_NumberToInt`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoTextEncode`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`WanVideoImageClipEncode`、`ImageResize+`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoExperimentalArgs`、`WanVideoSLG`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`、`FILM VFI`、`ImageResizeKJ`、`WD14Tagger|pysssss`、`WanVideoLoraSelect`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
