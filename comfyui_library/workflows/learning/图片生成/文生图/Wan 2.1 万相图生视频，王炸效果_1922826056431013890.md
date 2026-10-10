---
key: Wan 2.1 万相图生视频，王炸效果_1922826056431013890.json
name: Wan 2.1 万相图生视频，王炸效果_1922826056431013890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan 2.1 万相图生视频，王炸效果_1922826056431013890.json
hash: 00b31599e6b08b64
coverage: 0.517241
learned_at: 2026-10-10 20:59:13
nodes: [easy cleanGpuUsed, easy cleanGpuUsed, ImageUpscaleWithModel, FILM VFI, ImageResizeKJ, UpscaleModelLoader, VHS_VideoCombine, JjkText, easy cleanGpuUsed, ImageUpscaleWithModel, JjkText, JjkText, JjkText, ImpactSwitch, UpscaleModelLoader, ImageResizeAdvanced, WD14Tagger|pysssss, ShowText|pysssss, easy textSwitch, Int, Int, ImageResizeAdvanced, MathExpression|pysssss, easy showAnything, CM_IntToNumber, MathExpression|pysssss, CR String To Number, MathExpression|pysssss, easy showAnything, CM_IntToNumber, CM_NumberToInt, MathExpression|pysssss, PrimitiveInt, PrimitiveInt, CM_NumberToInt, LoadImage, WanVideoBlockSwap, easy cleanGpuUsed, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTeaCache, WanVideoEnhanceAVideo, VHS_VideoCombine, WanVideoSampler, easy cleanGpuUsed, WanVideoTextEncode, WanVideoSLG, WanVideoExperimentalArgs, WanVideoDecode, WanVideoLoraSelect, LoadWanVideoClipTextEncoder, Fast Groups Bypasser (rgthree), easy cleanGpuUsed, WanVideoModelLoader, WanVideoImageClipEncode, ImageResize+, Fast Muter (rgthree), Label (rgthree)]
patterns: []
missing: [CR String To Number, FILM VFI, Fast Muter (rgthree), Label (rgthree), MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, WD14Tagger|pysssss, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy textSwitch, ImageResize+]
discoveries: [次要节点 `CR String To Number` 知识库中没有该节点类型的任何知识, 次要节点 `FILM VFI` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Muter (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `WD14Tagger|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# Wan 2.1 万相图生视频，王炸效果_1922826056431013890.json

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

覆盖率 **52%**（30/58）

**有卡**：`ImageUpscaleWithModel`、`ImageResizeKJ`、`UpscaleModelLoader`、`VHS_VideoCombine`、`ImageResizeAdvanced`、`Int`、`CM_IntToNumber`、`CM_NumberToInt`、`LoadImage`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTeaCache`、`WanVideoEnhanceAVideo`、`WanVideoSampler`、`WanVideoTextEncode`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoDecode`、`WanVideoLoraSelect`、`LoadWanVideoClipTextEncoder`、`WanVideoModelLoader`、`WanVideoImageClipEncode`

**缺卡**（17）：`CR String To Number`、`FILM VFI`、`Fast Muter (rgthree)`、`Label (rgthree)`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`WD14Tagger|pysssss`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy textSwitch`、`ImageResize+`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode、WanVideoTextEncode、WanVideoVAELoader

## 学习发现

- 次要节点 `CR String To Number` 知识库中没有该节点类型的任何知识
- 次要节点 `FILM VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Muter (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `WD14Tagger|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
