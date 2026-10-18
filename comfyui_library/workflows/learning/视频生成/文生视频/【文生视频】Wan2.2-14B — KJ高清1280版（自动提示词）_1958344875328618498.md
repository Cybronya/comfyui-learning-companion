---
key: 视频生成/文生视频/【文生视频】Wan2.2-14B — KJ高清1280版（自动提示词）_1958344875328618498.json
name: 【文生视频】Wan2.2-14B — KJ高清1280版（自动提示词）_1958344875328618498.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【文生视频】Wan2.2-14B — KJ高清1280版（自动提示词）_1958344875328618498.json
hash: 01673ba920ad3494
coverage: 0.871795
learned_at: 2026-10-15 22:43:42
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSampler, WanVideoSampler, WanVideoBlockSwap, WanVideoDecode, LayerColor: Brightness & Contrast, ImageFromBatch+, WanVideoVAELoader, easy showAnything, JWInteger, JWInteger, JWInteger, WanVideoEmptyEmbeds, MathExpression|pysssss, CR Prompt Text, CR Prompt Text, TextConcat, ShowText|pysssss, easy showAnything, JWStringConcat, easy showAnything, CR Prompt Text, WanVideoTextEncode, RHHiddenNodes, WanVideoModelLoader, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, WanVideoSetLoRAs, CreateCFGScheduleFloatList, WanVideoSetLoRAs, PrimitiveNode, LoadWanVideoT5TextEncoder, LoadImage, Wan22PromptSelector, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/【文生视频】Wan2.2-14B — KJ高清1280版（自动提示词）_1958344875328618498.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1958344875328618498.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `LayerColor: Brightness & Contrast`
- `ImageFromBatch+`
- `WanVideoVAELoader`
- `easy showAnything`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `WanVideoEmptyEmbeds`
- `MathExpression|pysssss`
- `CR Prompt Text`
- `CR Prompt Text`
- `TextConcat`
- `ShowText|pysssss`
- `easy showAnything`
- `JWStringConcat`
- `easy showAnything`
- `CR Prompt Text`
- `WanVideoTextEncode`
- `RHHiddenNodes`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `WanVideoSetLoRAs`
- `PrimitiveNode`
- `LoadWanVideoT5TextEncoder`
- `LoadImage`
- `Wan22PromptSelector`
- `VHS_VideoCombine`

## 知识

覆盖率 **87%**（34/39）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoBlockSwap`、`WanVideoDecode`、`LayerColor: Brightness & Contrast`、`ImageFromBatch+`、`WanVideoVAELoader`、`JWInteger`、`WanVideoEmptyEmbeds`、`MathExpression|pysssss`、`CR Prompt Text`、`TextConcat`、`JWStringConcat`、`WanVideoTextEncode`、`RHHiddenNodes`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`LoadWanVideoT5TextEncoder`、`LoadImage`、`Wan22PromptSelector`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect
