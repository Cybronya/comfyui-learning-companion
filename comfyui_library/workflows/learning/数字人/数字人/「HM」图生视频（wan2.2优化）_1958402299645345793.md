---
key: 数字人/数字人/「HM」图生视频（wan2.2优化）_1958402299645345793.json
name: 「HM」图生视频（wan2.2优化）_1958402299645345793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/「HM」图生视频（wan2.2优化）_1958402299645345793.json
hash: 23fc7b5167672484
coverage: 0.769231
learned_at: 2026-10-26 01:59:40
nodes: [Anything Everywhere3, WanVideoSLG, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoTextEncode, Anything Everywhere3, WanVideoDecode, LayerUtility: PurgeVRAM V2, Seed (rgthree), CreateCFGScheduleFloatList, WanVideoSampler, WanVideoSampler, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoModelLoader, WanVideoModelLoader, WanVideoImageToVideoEncode, Anything Everywhere, Int, Int, CLIPVisionLoader, WanVideoClipVisionEncode, Int, MathExpression|pysssss, Int, Int, ImageResizeKJv2, Int, LoadImage, CR Text, VHS_VideoCombine]
patterns: []
missing: []
---

# 数字人/数字人/「HM」图生视频（wan2.2优化）_1958402299645345793.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/「HM」图生视频（wan2.2优化）_1958402299645345793.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `Anything Everywhere3`
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `Anything Everywhere3`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM V2`
- `Seed (rgthree)`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoImageToVideoEncode`
- `Anything Everywhere`
- `Int`
- `Int`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `Int`
- `MathExpression|pysssss`
- `Int`
- `Int`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `CR Text`
- `VHS_VideoCombine`

## 知识

覆盖率 **77%**（30/39）

**有卡**：`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoDecode`、`LayerUtility: PurgeVRAM V2`、`Seed (rgthree)`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoImageToVideoEncode`、`Int`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`MathExpression|pysssss`、`ImageResizeKJv2`、`LoadImage`、`CR Text`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、Seed (rgthree)、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
