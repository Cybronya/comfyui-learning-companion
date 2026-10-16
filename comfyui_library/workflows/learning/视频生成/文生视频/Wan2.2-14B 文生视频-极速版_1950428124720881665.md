---
key: 视频生成/文生视频/Wan2.2-14B 文生视频-极速版_1950428124720881665.json
name: Wan2.2-14B 文生视频-极速版_1950428124720881665.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1950428124720881665.json
hash: af469210e8524eb2
coverage: 0.807692
learned_at: 2026-10-15 22:43:35
nodes: [WanVideoLoraSelect, TextCombinerTwo, JWInteger, JjkText, WanVideoVAELoader, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoSetLoRAs, CreateCFGScheduleFloatList, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, easy cleanGpuUsed, WanVideoSampler, easy cleanGpuUsed, WanVideoSampler, LoadWanVideoT5TextEncoder, RH_Prompter, TextCombinerTwo, WanVideoDecode, PrimitiveNode, easy showAnything, Note, easy showAnything, RH_Prompter, JjkText, JjkText, JjkText, easy anythingIndexSwitch, WanVideoTextEncode, VHS_VideoCombine, LayerColor: Brightness & Contrast, ImageFromBatch+, Int, Int, Int, Int, Int, Int, Int, Int, ImpactSwitch, Int, Int, MathExpression|pysssss, WanVideoEmptyEmbeds, ImpactSwitch]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2-14B 文生视频-极速版_1950428124720881665.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950428124720881665.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（52 个）：
- `WanVideoLoraSelect`
- `TextCombinerTwo`
- `JWInteger`
- `JjkText`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `LoadWanVideoT5TextEncoder`
- `RH_Prompter`
- `TextCombinerTwo`
- `WanVideoDecode`
- `PrimitiveNode`
- `easy showAnything`
- `Note`
- `easy showAnything`
- `RH_Prompter`
- `JjkText`
- `JjkText`
- `JjkText`
- `easy anythingIndexSwitch`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `LayerColor: Brightness & Contrast`
- `ImageFromBatch+`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `Int`
- `ImpactSwitch`
- `Int`
- `Int`
- `MathExpression|pysssss`
- `WanVideoEmptyEmbeds`
- `ImpactSwitch`

## 知识

覆盖率 **81%**（42/52）

**有卡**：`WanVideoLoraSelect`、`TextCombinerTwo`、`JWInteger`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`easy cleanGpuUsed`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`RH_Prompter`、`WanVideoDecode`、`easy anythingIndexSwitch`、`WanVideoTextEncode`、`VHS_VideoCombine`、`LayerColor: Brightness & Contrast`、`ImageFromBatch+`、`Int`、`MathExpression|pysssss`、`WanVideoEmptyEmbeds`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
