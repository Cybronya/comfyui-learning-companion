---
key: 视频生成/文生视频/Wan2.2-14B 图生视频-123_2001306225730088961.json
name: Wan2.2-14B 图生视频-123_2001306225730088961
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-14B 图生视频-123_2001306225730088961.json
hash: 031e1c913d870b7e
coverage: 0.714286
learned_at: 2026-10-11 02:57:38
nodes: [JWInteger, PreviewImage, RH_Translator, MathExpression|pysssss, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, CreateCFGScheduleFloatList, PrimitiveNode, WanVideoDecode, WanVideoSampler, WanVideoVAELoader, easy showAnything, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoSampler, easy showAnything, RH_Captioner, easy showAnything, TextCombinerTwo, JjkText, TextCombinerTwo, TextCombinerTwo, JjkText, ImageResize+, ImpactSwitch, Int, Int, Int, Int, Int, Int, Int, Int, Int, Int, WanVideoImageToVideoEncode, VHS_VideoCombine, ImpactSwitch, PreviewImage, ImageResize+, easy anythingIndexSwitch, Note, RH_Prompter, TextCombinerTwo, WanVideoModelLoader, WanVideoModelLoader, JjkText, LoadImage]
patterns: []
missing: [MathExpression|pysssss, easy anythingIndexSwitch, ImageResize+, ImageResize+]
discoveries: [次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan2.2-14B 图生视频-123_2001306225730088961.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2-14B 图生视频-123_2001306225730088961.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（56 个）：
- `JWInteger`
- `PreviewImage`
- `RH_Translator`
- `MathExpression|pysssss`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `CreateCFGScheduleFloatList`
- `PrimitiveNode`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `easy showAnything`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `easy showAnything`
- `RH_Captioner`
- `easy showAnything`
- `TextCombinerTwo`
- `JjkText`
- `TextCombinerTwo`
- `TextCombinerTwo`
- `JjkText`
- `ImageResize+`
- `ImpactSwitch`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `WanVideoImageToVideoEncode`
- `VHS_VideoCombine`
- `ImpactSwitch`
- `PreviewImage`
- `ImageResize+`
- `easy anythingIndexSwitch`
- `Note`
- `RH_Prompter`
- `TextCombinerTwo`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `JjkText`
- `LoadImage`

## 知识

覆盖率 **71%**（40/56）

**有卡**：`JWInteger`、`RH_Translator`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`CreateCFGScheduleFloatList`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoTextEncode`、`RH_Captioner`、`TextCombinerTwo`、`Int`、`WanVideoImageToVideoEncode`、`VHS_VideoCombine`、`RH_Prompter`、`WanVideoModelLoader`、`LoadImage`

**缺卡**（4）：`MathExpression|pysssss`、`easy anythingIndexSwitch`、`ImageResize+`、`ImageResize+`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode

## 学习发现

- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
