---
key: 视频生成/图生视频/图生视频-水流冲脱效果wan2.2 Image 2 Video_2011435103129444353.json
name: 图生视频-水流冲脱效果wan2.2 Image 2 Video_2011435103129444353.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频-水流冲脱效果wan2.2 Image 2 Video_2011435103129444353.json
hash: 3e967d29556559ab
coverage: 0.786885
learned_at: 2026-10-15 22:34:22
nodes: [Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), easy int, SetNode, SetNode, SetNode, easy int, easy int, SetNode, WanVideoBlockSwap, MathExpression|pysssss, WanVideoImageToVideoEncode, WanVideoBlockSwap, INTConstant, WanVideoTextEncode, SimpleMath+, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, GetNode, GetNode, GetNode, LoadWanVideoT5TextEncoder, SetNode, TextCombinerTwo, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, CreateCFGScheduleFloatList, GetNode, WanVideoSampler, WanVideoLoraSelect, WanVideoSetLoRAs, GetNode, Pipe to/edit any [Crystools], WanVideoSetBlockSwap, WanVideoLoraSelect, Pipe from any [Crystools], WanVideoModelLoader, Pipe from any [Crystools], WanVideoSampler, Seed Everywhere, Anything Everywhere, WanVideoVAELoader, VHS_VideoCombine, WanVideoDecode, WanVideoVAELoader, WanVideoDecode, VHS_VideoCombine, LoadLatent, Label (rgthree), Label (rgthree), Label (rgthree), SaveLatent, Label (rgthree), Label (rgthree), Label (rgthree), LoadImage, Textbox]
patterns: []
missing: []
---

# 视频生成/图生视频/图生视频-水流冲脱效果wan2.2 Image 2 Video_2011435103129444353.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2011435103129444353.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（61 个）：
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `easy int`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy int`
- `easy int`
- `SetNode`
- `WanVideoBlockSwap`
- `MathExpression|pysssss`
- `WanVideoImageToVideoEncode`
- `WanVideoBlockSwap`
- `INTConstant`
- `WanVideoTextEncode`
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
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `LoadLatent`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `SaveLatent`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `LoadImage`
- `Textbox`

## 知识

覆盖率 **79%**（48/61）

**有卡**：`Label (rgthree)`、`easy int`、`WanVideoBlockSwap`、`MathExpression|pysssss`、`WanVideoImageToVideoEncode`、`INTConstant`、`WanVideoTextEncode`、`SimpleMath+`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadWanVideoT5TextEncoder`、`TextCombinerTwo`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`WanVideoLoraSelect`、`Pipe to/edit any [Crystools]`、`Pipe from any [Crystools]`、`Seed Everywhere`、`WanVideoVAELoader`、`VHS_VideoCombine`、`WanVideoDecode`、`LoadLatent`、`SaveLatent`、`LoadImage`、`Textbox`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、Seed Everywhere、SaveLatent、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
