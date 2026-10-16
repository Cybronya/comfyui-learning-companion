---
key: 视频生成/图生视频/全能图生视频 Wan2.2 I2V 可以9分钟200R_2044763237136211969.json
name: 全能图生视频 Wan2.2 I2V 可以9分钟200R_2044763237136211969.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2044763237136211969.json
hash: a504c8aded2221b5
coverage: 0.6875
learned_at: 2026-10-15 22:36:40
nodes: [SetNode, SetNode, SetNode, easy int, WanVideoBlockSwap, MathExpression|pysssss, WanVideoImageToVideoEncode, WanVideoBlockSwap, INTConstant, SimpleMath+, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, GetNode, GetNode, GetNode, LoadWanVideoT5TextEncoder, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, CreateCFGScheduleFloatList, GetNode, WanVideoSampler, WanVideoLoraSelect, WanVideoSetLoRAs, GetNode, Pipe to/edit any [Crystools], WanVideoSetBlockSwap, WanVideoLoraSelect, Pipe from any [Crystools], WanVideoModelLoader, Pipe from any [Crystools], WanVideoSampler, Seed Everywhere, Anything Everywhere, WanVideoVAELoader, SetNode, MarkdownNote, WanVideoTextEncode, WanVideoDecode, MarkdownNote, LoadImage, Textbox, TextCombinerTwo, easy int, easy int, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/全能图生视频 Wan2.2 I2V 可以9分钟200R_2044763237136211969.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044763237136211969.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（48 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `easy int`
- `WanVideoBlockSwap`
- `MathExpression|pysssss`
- `WanVideoImageToVideoEncode`
- `WanVideoBlockSwap`
- `INTConstant`
- `SimpleMath+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `CreateCFGScheduleFloatList`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `GetNode`
- `Pipe to/edit any [Crystools]`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `Pipe from any [Crystools]`
- `WanVideoModelLoader`
- `Pipe from any [Crystools]`
- `WanVideoSampler` ★核心
- `Seed Everywhere`
- `Anything Everywhere`
- `WanVideoVAELoader`
- `SetNode`
- `MarkdownNote`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `MarkdownNote`
- `LoadImage`
- `Textbox`
- `TextCombinerTwo`
- `easy int`
- `easy int`
- `VHS_VideoCombine`

## 知识

覆盖率 **69%**（33/48）

**有卡**：`easy int`、`WanVideoBlockSwap`、`MathExpression|pysssss`、`WanVideoImageToVideoEncode`、`INTConstant`、`SimpleMath+`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`WanVideoLoraSelect`、`Pipe to/edit any [Crystools]`、`Pipe from any [Crystools]`、`Seed Everywhere`、`WanVideoVAELoader`、`WanVideoTextEncode`、`WanVideoDecode`、`LoadImage`、`Textbox`、`TextCombinerTwo`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、Seed Everywhere、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
