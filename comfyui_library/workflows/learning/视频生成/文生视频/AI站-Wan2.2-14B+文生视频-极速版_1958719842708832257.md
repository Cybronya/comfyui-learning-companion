---
key: 视频生成/文生视频/AI站-Wan2.2-14B+文生视频-极速版_1958719842708832257.json
name: AI站-Wan2.2-14B+文生视频-极速版_1958719842708832257.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1958719842708832257.json
hash: cc916a8c99791b23
coverage: 0.782609
learned_at: 2026-10-15 22:43:42
nodes: [WanVideoLoraSelect, TextCombinerTwo, JWInteger, WanVideoVAELoader, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoSampler, easy cleanGpuUsed, LoadWanVideoT5TextEncoder, TextCombinerTwo, WanVideoDecode, WanVideoTextEncode, LayerColor: Brightness & Contrast, ImpactSwitch, MathExpression|pysssss, WanVideoSampler, ImpactSwitch, WanVideoEmptyEmbeds, Int, Int, Int, Int, Int, Int, Int, Int, Int, Int, ImageFromBatch+, VHS_VideoCombine, easy anythingIndexSwitch, RH_Prompter, RH_Prompter, JjkText, JjkText, Note, easy showAnything, easy showAnything, JjkText, JjkText, WanVideoSetLoRAs, easy cleanGpuUsed, PrimitiveNode, CreateCFGScheduleFloatList, WanVideoModelLoader, WanVideoModelLoader]
patterns: []
missing: []
---

# 视频生成/文生视频/AI站-Wan2.2-14B+文生视频-极速版_1958719842708832257.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1958719842708832257.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（46 个）：
- `WanVideoLoraSelect`
- `TextCombinerTwo`
- `JWInteger`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `LoadWanVideoT5TextEncoder`
- `TextCombinerTwo`
- `WanVideoDecode`
- `WanVideoTextEncode`
- `LayerColor: Brightness & Contrast`
- `ImpactSwitch`
- `MathExpression|pysssss`
- `WanVideoSampler` ★核心
- `ImpactSwitch`
- `WanVideoEmptyEmbeds`
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
- `ImageFromBatch+`
- `VHS_VideoCombine`
- `easy anythingIndexSwitch`
- `RH_Prompter`
- `RH_Prompter`
- `JjkText`
- `JjkText`
- `Note`
- `easy showAnything`
- `easy showAnything`
- `JjkText`
- `JjkText`
- `WanVideoSetLoRAs`
- `easy cleanGpuUsed`
- `PrimitiveNode`
- `CreateCFGScheduleFloatList`
- `WanVideoModelLoader`
- `WanVideoModelLoader`

## 知识

覆盖率 **78%**（36/46）

**有卡**：`WanVideoLoraSelect`、`TextCombinerTwo`、`JWInteger`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoSampler`、`easy cleanGpuUsed`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`WanVideoTextEncode`、`LayerColor: Brightness & Contrast`、`MathExpression|pysssss`、`WanVideoEmptyEmbeds`、`Int`、`ImageFromBatch+`、`VHS_VideoCombine`、`easy anythingIndexSwitch`、`RH_Prompter`、`CreateCFGScheduleFloatList`、`WanVideoModelLoader`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
