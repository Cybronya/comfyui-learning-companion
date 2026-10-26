---
key: 数字人/数字人/「HM」图生视频（wan2.2优化）_1985522827342323713.json
name: 「HM」图生视频（wan2.2优化）_1985522827342323713
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/「HM」图生视频（wan2.2优化）_1985522827342323713.json
hash: dfdeef5f3b02337d
coverage: 0.782609
learned_at: 2026-10-26 01:59:40
nodes: [Anything Everywhere3, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoTextEncode, Anything Everywhere3, LayerUtility: PurgeVRAM V2, Seed (rgthree), WanVideoSampler, WanVideoSampler, Reroute, Reroute, Reroute, WanVideoLoraSelect, WanVideoModelLoader, Anything Everywhere, Int, Int, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, VHS_VideoCombine, WanVideoDecode, Reroute, Reroute, CreateCFGScheduleFloatList, Int, WanVideoModelLoader, WanVideoExperimentalArgs, MathExpression|pysssss, MathExpression|pysssss, WanVideoBlockSwap, WanVideoImageToVideoEncode, Int, CLIPVisionLoader, Reroute, WanVideoClipVisionEncode, ImageResizeKJv2, Int, MathExpression|pysssss, Int, Int, PreviewImage, LoadImage, CR Text]
patterns: []
missing: []
---

# 数字人/数字人/「HM」图生视频（wan2.2优化）_1985522827342323713.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/「HM」图生视频（wan2.2优化）_1985522827342323713.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（46 个）：
- `Anything Everywhere3`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `Anything Everywhere3`
- `LayerUtility: PurgeVRAM V2`
- `Seed (rgthree)`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `Anything Everywhere`
- `Int`
- `Int`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `Reroute`
- `Reroute`
- `CreateCFGScheduleFloatList`
- `Int`
- `WanVideoModelLoader`
- `WanVideoExperimentalArgs`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `WanVideoBlockSwap`
- `WanVideoImageToVideoEncode`
- `Int`
- `CLIPVisionLoader`
- `Reroute`
- `WanVideoClipVisionEncode`
- `ImageResizeKJv2`
- `Int`
- `MathExpression|pysssss`
- `Int`
- `Int`
- `PreviewImage`
- `LoadImage`
- `CR Text`

## 知识

覆盖率 **78%**（36/46）

**有卡**：`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`LayerUtility: PurgeVRAM V2`、`Seed (rgthree)`、`WanVideoSampler`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`Int`、`MathExpression|pysssss`、`VHS_VideoCombine`、`WanVideoDecode`、`CreateCFGScheduleFloatList`、`WanVideoExperimentalArgs`、`WanVideoBlockSwap`、`WanVideoImageToVideoEncode`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`ImageResizeKJv2`、`LoadImage`、`CR Text`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、Seed (rgthree)、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
