---
key: 视频生成/图生视频/Wan2.2手势舞（取材于T8）_1953073108568764418.json
name: Wan2.2手势舞（取材于T8）_1953073108568764418.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2手势舞（取材于T8）_1953073108568764418.json
hash: 24d99e82220a3b20
coverage: 0.830508
learned_at: 2026-10-15 22:31:04
nodes: [WanVideoLoraSelect, WanVideoVAELoader, WanVideoBlockSwap, WanVideoSetLoRAs, CreateCFGScheduleFloatList, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSampler, WanVideoSampler, LoadWanVideoT5TextEncoder, WanVideoDecode, PrimitiveNode, easy mathInt, String, String, ImpactSwitch, ImpactSwitch, easy mathInt, FluxResolutionNode, RH_LLMAPI_NODE, easy showAnything, JjkShowText, RH_LLMAPI_NODE, CreateVideo, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, RunningHub ThinkSound, WanVideoSetLoRAs, ImageFromBatch+, ImageFromBatch+, VHS_VideoCombine, LayerColor: Brightness & Contrast, WanVideoBlockSwap, ImpactSwitch, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoModelLoader, SaveVideo, WanVideoTextEncode, WanVideoLoraSelect, WanVideoLoraSelect, MathExpression|pysssss, WanVideoEmptyEmbeds, JWInteger, CR Prompt Text, ShowText|pysssss, CR Prompt Text, TextConcat, easy showAnything, RH_LLMAPI_NODE, JWStringConcat, easy showAnything, easy showAnything, CR Prompt Text, PrimitiveStringMultiline, Wan22PromptSelector]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2手势舞（取材于T8）_1953073108568764418.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1953073108568764418.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（59 个）：
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `LoadWanVideoT5TextEncoder`
- `WanVideoDecode`
- `PrimitiveNode`
- `easy mathInt`
- `String`
- `String`
- `ImpactSwitch`
- `ImpactSwitch`
- `easy mathInt`
- `FluxResolutionNode`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `JjkShowText`
- `RH_LLMAPI_NODE`
- `CreateVideo`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `RunningHub ThinkSound`
- `WanVideoSetLoRAs`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `VHS_VideoCombine`
- `LayerColor: Brightness & Contrast`
- `WanVideoBlockSwap`
- `ImpactSwitch`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `SaveVideo`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `MathExpression|pysssss`
- `WanVideoEmptyEmbeds`
- `JWInteger`
- `CR Prompt Text`
- `ShowText|pysssss`
- `CR Prompt Text`
- `TextConcat`
- `easy showAnything`
- `RH_LLMAPI_NODE`
- `JWStringConcat`
- `easy showAnything`
- `easy showAnything`
- `CR Prompt Text`
- `PrimitiveStringMultiline`
- `Wan22PromptSelector`

## 知识

覆盖率 **83%**（49/59）

**有卡**：`WanVideoLoraSelect`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`easy mathInt`、`String`、`FluxResolutionNode`、`RH_LLMAPI_NODE`、`JjkShowText`、`CreateVideo`、`MathExpression|pysssss`、`RunningHub ThinkSound`、`ImageFromBatch+`、`VHS_VideoCombine`、`LayerColor: Brightness & Contrast`、`SaveVideo`、`WanVideoTextEncode`、`WanVideoEmptyEmbeds`、`JWInteger`、`CR Prompt Text`、`TextConcat`、`JWStringConcat`、`Wan22PromptSelector`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
