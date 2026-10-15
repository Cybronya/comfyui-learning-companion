---
key: 图片生成/文生图/Wan 2.1 万相图生视频，王炸效果_1922826056431013890.json
name: Wan 2.1 万相图生视频，王炸效果_1922826056431013890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan 2.1 万相图生视频，王炸效果_1922826056431013890.json
hash: 00b31599e6b08b64
coverage: 0.810345
learned_at: 2026-10-15 22:27:34
nodes: [easy cleanGpuUsed, easy cleanGpuUsed, ImageUpscaleWithModel, FILM VFI, ImageResizeKJ, UpscaleModelLoader, VHS_VideoCombine, JjkText, easy cleanGpuUsed, ImageUpscaleWithModel, JjkText, JjkText, JjkText, ImpactSwitch, UpscaleModelLoader, ImageResizeAdvanced, WD14Tagger|pysssss, ShowText|pysssss, easy textSwitch, Int, Int, ImageResizeAdvanced, MathExpression|pysssss, easy showAnything, CM_IntToNumber, MathExpression|pysssss, CR String To Number, MathExpression|pysssss, easy showAnything, CM_IntToNumber, CM_NumberToInt, MathExpression|pysssss, PrimitiveInt, PrimitiveInt, CM_NumberToInt, LoadImage, WanVideoBlockSwap, easy cleanGpuUsed, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTeaCache, WanVideoEnhanceAVideo, VHS_VideoCombine, WanVideoSampler, easy cleanGpuUsed, WanVideoTextEncode, WanVideoSLG, WanVideoExperimentalArgs, WanVideoDecode, WanVideoLoraSelect, LoadWanVideoClipTextEncoder, Fast Groups Bypasser (rgthree), easy cleanGpuUsed, WanVideoModelLoader, WanVideoImageClipEncode, ImageResize+, Fast Muter (rgthree), Label (rgthree)]
patterns: []
missing: []
---

# 图片生成/文生图/Wan 2.1 万相图生视频，王炸效果_1922826056431013890.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan 2.1 万相图生视频，王炸效果_1922826056431013890.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（58 个）：
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ImageUpscaleWithModel`
- `FILM VFI`
- `ImageResizeKJ`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `JjkText`
- `easy cleanGpuUsed`
- `ImageUpscaleWithModel`
- `JjkText`
- `JjkText`
- `JjkText`
- `ImpactSwitch`
- `UpscaleModelLoader`
- `ImageResizeAdvanced`
- `WD14Tagger|pysssss`
- `ShowText|pysssss`
- `easy textSwitch`
- `Int`
- `Int`
- `ImageResizeAdvanced`
- `MathExpression|pysssss`
- `easy showAnything`
- `CM_IntToNumber`
- `MathExpression|pysssss`
- `CR String To Number`
- `MathExpression|pysssss`
- `easy showAnything`
- `CM_IntToNumber`
- `CM_NumberToInt`
- `MathExpression|pysssss`
- `PrimitiveInt`
- `PrimitiveInt`
- `CM_NumberToInt`
- `LoadImage`
- `WanVideoBlockSwap`
- `easy cleanGpuUsed`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoTeaCache`
- `WanVideoEnhanceAVideo`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `WanVideoTextEncode`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `LoadWanVideoClipTextEncoder` ★核心
- `Fast Groups Bypasser (rgthree)`
- `easy cleanGpuUsed`
- `WanVideoModelLoader`
- `WanVideoImageClipEncode`
- `ImageResize+`
- `Fast Muter (rgthree)`
- `Label (rgthree)`

## 知识

覆盖率 **81%**（47/58）

**有卡**：`easy cleanGpuUsed`、`ImageUpscaleWithModel`、`FILM VFI`、`ImageResizeKJ`、`UpscaleModelLoader`、`VHS_VideoCombine`、`ImageResizeAdvanced`、`WD14Tagger|pysssss`、`easy textSwitch`、`Int`、`MathExpression|pysssss`、`CM_IntToNumber`、`CR String To Number`、`CM_NumberToInt`、`LoadImage`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTeaCache`、`WanVideoEnhanceAVideo`、`WanVideoSampler`、`WanVideoTextEncode`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoDecode`、`WanVideoLoraSelect`、`LoadWanVideoClipTextEncoder`、`WanVideoModelLoader`、`WanVideoImageClipEncode`、`ImageResize+`、`Fast Muter (rgthree)`、`Label (rgthree)`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader
