---
key: 视频生成/图生视频/全能图生视频（时长可控 无水印）Wan2.2 I2V_2011322262611304450.json
name: 全能图生视频（时长可控 无水印）Wan2.2 I2V_2011322262611304450.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2011322262611304450.json
hash: 98e1d72e3ffd2a3c
coverage: 0.6875
learned_at: 2026-10-15 22:34:22
nodes: [easy int, SetNode, SetNode, SetNode, easy int, easy int, WanVideoBlockSwap, MathExpression|pysssss, WanVideoImageToVideoEncode, WanVideoBlockSwap, INTConstant, SimpleMath+, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, GetNode, GetNode, GetNode, LoadWanVideoT5TextEncoder, SetNode, TextCombinerTwo, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, CreateCFGScheduleFloatList, GetNode, WanVideoSampler, WanVideoLoraSelect, WanVideoSetLoRAs, GetNode, Pipe to/edit any [Crystools], WanVideoSetBlockSwap, WanVideoLoraSelect, Pipe from any [Crystools], WanVideoModelLoader, Pipe from any [Crystools], WanVideoSampler, Seed Everywhere, Anything Everywhere, WanVideoVAELoader, SetNode, MarkdownNote, WanVideoTextEncode, VHS_VideoCombine, WanVideoDecode, MarkdownNote, LoadImage, Textbox]
patterns: []
missing: []
---

# 视频生成/图生视频/全能图生视频（时长可控 无水印）Wan2.2 I2V_2011322262611304450.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2011322262611304450.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（48 个）：
- `easy int`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy int`
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
- `TextCombinerTwo`
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
- `VHS_VideoCombine`
- `WanVideoDecode`
- `MarkdownNote`
- `LoadImage`
- `Textbox`

## 知识

覆盖率 **69%**（33/48）

**有卡**：`easy int`、`WanVideoBlockSwap`、`MathExpression|pysssss`、`WanVideoImageToVideoEncode`、`INTConstant`、`SimpleMath+`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`TextCombinerTwo`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`WanVideoLoraSelect`、`Pipe to/edit any [Crystools]`、`Pipe from any [Crystools]`、`Seed Everywhere`、`WanVideoVAELoader`、`WanVideoTextEncode`、`VHS_VideoCombine`、`WanVideoDecode`、`LoadImage`、`Textbox`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、Seed Everywhere、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
