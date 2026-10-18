---
key: 视频生成/文生视频/Wan2.2-14B 文生视频_自动提示词_1950420829684285441.json
name: Wan2.2-14B 文生视频_自动提示词_1950420829684285441.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-14B 文生视频_自动提示词_1950420829684285441.json
hash: 8a22761fb7e0572a
coverage: 0.836735
learned_at: 2026-10-15 22:43:35
nodes: [WanVideoLoraSelect, JWInteger, MathExpression|pysssss, WanVideoVAELoader, CreateCFGScheduleFloatList, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, easy cleanGpuUsed, WanVideoSampler, WanVideoTextEncode, WanVideoEmptyEmbeds, WanVideoTorchCompileSettings, easy cleanGpuUsed, WanVideoSampler, LoadWanVideoT5TextEncoder, WanVideoDecode, PrimitiveNode, VHS_VideoCombine, JjkText, TextCombinerTwo, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoBlockSwap, LayerColor: Brightness & Contrast, Note, RH_Prompter, FluxResolutionNode, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, WanVideoSetLoRAs, WanVideoSetLoRAs, JjkText, JjkText, TextCombinerTwo, easy anythingIndexSwitch, CR Text Concatenate, JjkText, easy showAnything, Wan22PromptSelector, RH_Prompter, easy showAnything, CreateVideo, PreViewVideo]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2-14B 文生视频_自动提示词_1950420829684285441.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950420829684285441.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（49 个）：
- `WanVideoLoraSelect`
- `JWInteger`
- `MathExpression|pysssss`
- `WanVideoVAELoader`
- `CreateCFGScheduleFloatList`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `WanVideoEmptyEmbeds`
- `WanVideoTorchCompileSettings`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `LoadWanVideoT5TextEncoder`
- `WanVideoDecode`
- `PrimitiveNode`
- `VHS_VideoCombine`
- `JjkText`
- `TextCombinerTwo`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `LayerColor: Brightness & Contrast`
- `Note`
- `RH_Prompter`
- `FluxResolutionNode`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `JjkText`
- `JjkText`
- `TextCombinerTwo`
- `easy anythingIndexSwitch`
- `CR Text Concatenate`
- `JjkText`
- `easy showAnything`
- `Wan22PromptSelector`
- `RH_Prompter`
- `easy showAnything`
- `CreateVideo`
- `PreViewVideo`

## 知识

覆盖率 **84%**（41/49）

**有卡**：`WanVideoLoraSelect`、`JWInteger`、`MathExpression|pysssss`、`WanVideoVAELoader`、`CreateCFGScheduleFloatList`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`easy cleanGpuUsed`、`WanVideoSampler`、`WanVideoTextEncode`、`WanVideoEmptyEmbeds`、`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`VHS_VideoCombine`、`TextCombinerTwo`、`LayerColor: Brightness & Contrast`、`RH_Prompter`、`FluxResolutionNode`、`WanVideoSetLoRAs`、`easy anythingIndexSwitch`、`CR Text Concatenate`、`Wan22PromptSelector`、`CreateVideo`、`PreViewVideo`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
