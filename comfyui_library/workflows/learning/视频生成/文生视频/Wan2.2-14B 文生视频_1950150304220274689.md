---
key: 视频生成/文生视频/Wan2.2-14B 文生视频_1950150304220274689.json
name: Wan2.2-14B 文生视频_1950150304220274689.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1950150304220274689.json
hash: 63ae026e325f11d6
coverage: 0.736842
learned_at: 2026-10-15 22:43:34
nodes: [WanVideoLoraSelect, WanVideoVAELoader, WanVideoLoraSelect, WanVideoSampler, WanVideoSampler, WanVideoDecode, PrimitiveNode, TextCombinerTwo, RH_Prompter, RH_LLMAPI_NODE, easy showAnything, JjkShowText, RH_LLMAPI_NODE, CreateVideo, RunningHub ThinkSound, JjkText, CR Text Concatenate, WanVideoSetLoRAs, ImageFromBatch+, ImageFromBatch+, SaveVideo, VHS_VideoCombine, LayerColor: Brightness & Contrast, easy showAnything, RH_Prompter, easy showAnything, easy showAnything, Note, ImpactSwitch, WanVideoTextEncode, Int, Int, Int, Int, Int, Int, Int, Int, Int, Int, Int, Int, ImpactSwitch, Bjornulf_ShowInt, Int, Int, Int, Int, ImpactSwitch, Int, Int, Int, Int, Note, Bjornulf_ShowInt, MathExpression|pysssss, WanVideoEmptyEmbeds, JWInteger, ImpactSwitch, String, String, ImpactSwitch, ImpactSwitch, ImpactSwitch, ImpactSwitch, CR Text Concatenate, ShowText, JjkText, JjkText, JjkText, WanVideoSetLoRAs, CreateCFGScheduleFloatList, WanVideoModelLoader, WanVideoModelLoader, LoadWanVideoT5TextEncoder, JjkText]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2-14B 文生视频_1950150304220274689.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950150304220274689.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（76 个）：
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `PrimitiveNode`
- `TextCombinerTwo`
- `RH_Prompter`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `JjkShowText`
- `RH_LLMAPI_NODE`
- `CreateVideo`
- `RunningHub ThinkSound`
- `JjkText`
- `CR Text Concatenate`
- `WanVideoSetLoRAs`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `SaveVideo`
- `VHS_VideoCombine`
- `LayerColor: Brightness & Contrast`
- `easy showAnything`
- `RH_Prompter`
- `easy showAnything`
- `easy showAnything`
- `Note`
- `ImpactSwitch`
- `WanVideoTextEncode`
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
- `Int`
- `Int`
- `ImpactSwitch`
- `Bjornulf_ShowInt`
- `Int`
- `Int`
- `Int`
- `Int`
- `ImpactSwitch`
- `Int`
- `Int`
- `Int`
- `Int`
- `Note`
- `Bjornulf_ShowInt`
- `MathExpression|pysssss`
- `WanVideoEmptyEmbeds`
- `JWInteger`
- `ImpactSwitch`
- `String`
- `String`
- `ImpactSwitch`
- `ImpactSwitch`
- `ImpactSwitch`
- `ImpactSwitch`
- `CR Text Concatenate`
- `ShowText`
- `JjkText`
- `JjkText`
- `JjkText`
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `JjkText`

## 知识

覆盖率 **74%**（56/76）

**有卡**：`WanVideoLoraSelect`、`WanVideoVAELoader`、`WanVideoSampler`、`WanVideoDecode`、`TextCombinerTwo`、`RH_Prompter`、`RH_LLMAPI_NODE`、`JjkShowText`、`CreateVideo`、`RunningHub ThinkSound`、`CR Text Concatenate`、`WanVideoSetLoRAs`、`ImageFromBatch+`、`SaveVideo`、`VHS_VideoCombine`、`LayerColor: Brightness & Contrast`、`WanVideoTextEncode`、`Int`、`Bjornulf_ShowInt`、`MathExpression|pysssss`、`WanVideoEmptyEmbeds`、`JWInteger`、`String`、`ShowText`、`CreateCFGScheduleFloatList`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
