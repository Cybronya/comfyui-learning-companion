---
key: 视频生成/文生视频/CN-Wan2.2-14B 文生视频-极速版_1959814515066089473.json
name: CN-Wan2.2-14B 文生视频-极速版_1959814515066089473
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/CN-Wan2.2-14B 文生视频-极速版_1959814515066089473.json
hash: f4fb7a28a8bec8c9
coverage: 0.709091
learned_at: 2026-10-10 22:58:46
nodes: [TextCombinerTwo, JWInteger, JjkText, WanVideoVAELoader, WanVideoLoraSelect, easy cleanGpuUsed, RH_Prompter, TextCombinerTwo, WanVideoDecode, RH_Prompter, LayerColor: Brightness & Contrast, MathExpression|pysssss, WanVideoEmptyEmbeds, Note, WanVideoLoraSelect, WanVideoSetBlockSwap, easy cleanGpuUsed, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSampler, WanVideoSampler, WanVideoSetLoRAs, easy anythingIndexSwitch, WanVideoTextEncode, WanVideoModelLoader, WanVideoModelLoader, PrimitiveNode, WanVideoBlockSwap, WanVideoBlockSwap, CreateCFGScheduleFloatList, WanVideoBlockSwap, Int, Int, Int, Int, JjkText, easy showAnything, easy showAnything, JjkText, JjkText, VHS_VideoCombine, ImageFromBatch+, ImpactSwitch, Int, Int, Int, Int, Int, Int, Int, Int, ImpactSwitch, LoadWanVideoT5TextEncoder, Int, Int]
patterns: []
missing: [ImageFromBatch+, LayerColor: Brightness & Contrast, MathExpression|pysssss, easy anythingIndexSwitch, easy cleanGpuUsed, easy cleanGpuUsed]
discoveries: [次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerColor: Brightness & Contrast` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/CN-Wan2.2-14B 文生视频-极速版_1959814515066089473.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/CN-Wan2.2-14B 文生视频-极速版_1959814515066089473.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（55 个）：
- `TextCombinerTwo`
- `JWInteger`
- `JjkText`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `easy cleanGpuUsed`
- `RH_Prompter`
- `TextCombinerTwo`
- `WanVideoDecode`
- `RH_Prompter`
- `LayerColor: Brightness & Contrast`
- `MathExpression|pysssss`
- `WanVideoEmptyEmbeds`
- `Note`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `easy cleanGpuUsed`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `easy anythingIndexSwitch`
- `WanVideoTextEncode`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `PrimitiveNode`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `CreateCFGScheduleFloatList`
- `WanVideoBlockSwap`
- `Int`
- `Int`
- `Int`
- `Int`
- `JjkText`
- `easy showAnything`
- `easy showAnything`
- `JjkText`
- `JjkText`
- `VHS_VideoCombine`
- `ImageFromBatch+`
- `ImpactSwitch`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `ImpactSwitch`
- `LoadWanVideoT5TextEncoder`
- `Int`
- `Int`

## 知识

覆盖率 **71%**（39/55）

**有卡**：`TextCombinerTwo`、`JWInteger`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`RH_Prompter`、`WanVideoDecode`、`WanVideoEmptyEmbeds`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSampler`、`WanVideoTextEncode`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`CreateCFGScheduleFloatList`、`Int`、`VHS_VideoCombine`、`LoadWanVideoT5TextEncoder`

**缺卡**（6）：`ImageFromBatch+`、`LayerColor: Brightness & Contrast`、`MathExpression|pysssss`、`easy anythingIndexSwitch`、`easy cleanGpuUsed`、`easy cleanGpuUsed`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs

## 学习发现

- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerColor: Brightness & Contrast` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
