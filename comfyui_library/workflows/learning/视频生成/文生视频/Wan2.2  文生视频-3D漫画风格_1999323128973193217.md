---
key: 视频生成/文生视频/Wan2.2  文生视频-3D漫画风格_1999323128973193217.json
name: Wan2.2  文生视频-3D漫画风格_1999323128973193217
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2  文生视频-3D漫画风格_1999323128973193217.json
hash: 17b099a5cc8ebca6
coverage: 0.705882
learned_at: 2026-10-11 02:57:38
nodes: [WanVideoVAELoader, WanVideoSetLoRAs, CreateCFGScheduleFloatList, WanVideoSetLoRAs, easy cleanGpuUsed, WanVideoSampler, MathExpression|pysssss, WanVideoSampler, WanVideoModelLoader, WanVideoDecode, LoadWanVideoT5TextEncoder, WanVideoEmptyEmbeds, WanVideoTextEncode, Note, easy cleanGpuUsed, JWInteger, JjkText, WanVideoModelLoader, Int, Int, WanVideoLoraSelect, WanVideoLoraSelect, TextCombinerTwo, TextCombinerTwo, RH_Prompter, PrimitiveNode, VHS_VideoCombine, WanVideoLoraSelect, WanVideoLoraSelect, easy showAnything, JjkText, TextCombinerTwo, JjkText, easy anythingIndexSwitch]
patterns: []
missing: [MathExpression|pysssss, easy anythingIndexSwitch, easy cleanGpuUsed, easy cleanGpuUsed]
discoveries: [次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.2  文生视频-3D漫画风格_1999323128973193217.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2  文生视频-3D漫画风格_1999323128973193217.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（34 个）：
- `WanVideoVAELoader`
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `WanVideoSetLoRAs`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `MathExpression|pysssss`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoDecode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoEmptyEmbeds`
- `WanVideoTextEncode`
- `Note`
- `easy cleanGpuUsed`
- `JWInteger`
- `JjkText`
- `WanVideoModelLoader`
- `Int`
- `Int`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `TextCombinerTwo`
- `TextCombinerTwo`
- `RH_Prompter`
- `PrimitiveNode`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `easy showAnything`
- `JjkText`
- `TextCombinerTwo`
- `JjkText`
- `easy anythingIndexSwitch`

## 知识

覆盖率 **71%**（24/34）

**有卡**：`WanVideoVAELoader`、`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoEmptyEmbeds`、`WanVideoTextEncode`、`JWInteger`、`Int`、`WanVideoLoraSelect`、`TextCombinerTwo`、`RH_Prompter`、`VHS_VideoCombine`

**缺卡**（4）：`MathExpression|pysssss`、`easy anythingIndexSwitch`、`easy cleanGpuUsed`、`easy cleanGpuUsed`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs

## 学习发现

- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
