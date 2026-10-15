---
key: 视频生成/文生视频/Wan2.2  文生视频-3D漫画风格_1999323128973193217.json
name: Wan2.2  文生视频-3D漫画风格_1999323128973193217
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2  文生视频-3D漫画风格_1999323128973193217.json
hash: 17b099a5cc8ebca6
coverage: 0.823529
learned_at: 2026-10-15 22:47:08
nodes: [WanVideoVAELoader, WanVideoSetLoRAs, CreateCFGScheduleFloatList, WanVideoSetLoRAs, easy cleanGpuUsed, WanVideoSampler, MathExpression|pysssss, WanVideoSampler, WanVideoModelLoader, WanVideoDecode, LoadWanVideoT5TextEncoder, WanVideoEmptyEmbeds, WanVideoTextEncode, Note, easy cleanGpuUsed, JWInteger, JjkText, WanVideoModelLoader, Int, Int, WanVideoLoraSelect, WanVideoLoraSelect, TextCombinerTwo, TextCombinerTwo, RH_Prompter, PrimitiveNode, VHS_VideoCombine, WanVideoLoraSelect, WanVideoLoraSelect, easy showAnything, JjkText, TextCombinerTwo, JjkText, easy anythingIndexSwitch]
patterns: []
missing: []
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

覆盖率 **82%**（28/34）

**有卡**：`WanVideoVAELoader`、`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`easy cleanGpuUsed`、`WanVideoSampler`、`MathExpression|pysssss`、`WanVideoModelLoader`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoEmptyEmbeds`、`WanVideoTextEncode`、`JWInteger`、`Int`、`WanVideoLoraSelect`、`TextCombinerTwo`、`RH_Prompter`、`VHS_VideoCombine`、`easy anythingIndexSwitch`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
