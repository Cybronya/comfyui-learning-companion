---
key: 视频生成/文生视频/Wan2.2-14B 文生视频 KJ高清1280版（自动提示词）_1955159900055900162.json
name: Wan2.2-14B 文生视频 KJ高清1280版（自动提示词）_1955159900055900162.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1955159900055900162.json
hash: 06e4d651c3ea03f9
coverage: 0.868421
learned_at: 2026-10-15 22:43:40
nodes: [WanVideoVAELoader, WanVideoSetLoRAs, CreateCFGScheduleFloatList, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSampler, WanVideoSampler, LoadWanVideoT5TextEncoder, PrimitiveNode, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoBlockSwap, TextConcat, easy showAnything, JWStringConcat, easy showAnything, Wan22PromptSelector, WanVideoTextEncode, CR Prompt Text, ShowText|pysssss, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoLoraSelect, LayerColor: Brightness & Contrast, ImageFromBatch+, WanVideoDecode, VHS_VideoCombine, WanVideoModelLoader, MathExpression|pysssss, WanVideoEmptyEmbeds, JWInteger, JWInteger, JWInteger, CR Prompt Text, CR Prompt Text, easy showAnything, RHHiddenNodes]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2-14B 文生视频 KJ高清1280版（自动提示词）_1955159900055900162.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1955159900055900162.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（38 个）：
- `WanVideoVAELoader`
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `LoadWanVideoT5TextEncoder`
- `PrimitiveNode`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `TextConcat`
- `easy showAnything`
- `JWStringConcat`
- `easy showAnything`
- `Wan22PromptSelector`
- `WanVideoTextEncode`
- `CR Prompt Text`
- `ShowText|pysssss`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `LayerColor: Brightness & Contrast`
- `ImageFromBatch+`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `MathExpression|pysssss`
- `WanVideoEmptyEmbeds`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `CR Prompt Text`
- `CR Prompt Text`
- `easy showAnything`
- `RHHiddenNodes`

## 知识

覆盖率 **87%**（33/38）

**有卡**：`WanVideoVAELoader`、`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`TextConcat`、`JWStringConcat`、`Wan22PromptSelector`、`WanVideoTextEncode`、`CR Prompt Text`、`WanVideoLoraSelect`、`LayerColor: Brightness & Contrast`、`ImageFromBatch+`、`WanVideoDecode`、`VHS_VideoCombine`、`MathExpression|pysssss`、`WanVideoEmptyEmbeds`、`JWInteger`、`RHHiddenNodes`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
