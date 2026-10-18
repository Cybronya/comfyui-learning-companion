---
key: 视频生成/图生视频/Wan2.2-14B 图生视频_1950542819607891970.json
name: Wan2.2-14B 图生视频_1950542819607891970.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-14B 图生视频_1950542819607891970.json
hash: 3474f66930bdadde
coverage: 0.794872
learned_at: 2026-10-15 22:30:55
nodes: [JWInteger, easy showAnything, TextCombinerTwo, RH_Prompter, easy showAnything, RH_Translator, MathExpression|pysssss, JjkText, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoTextEncode, CreateCFGScheduleFloatList, PrimitiveNode, WanVideoSampler, WanVideoDecode, WanVideoSampler, WanVideoVAELoader, easy showAnything, Note, TextCombinerTwo, RH_Captioner, JjkText, JjkText, easy anythingIndexSwitch, VHS_VideoCombine, ImageResize+, LoadImage, WanVideoImageToVideoEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-14B 图生视频_1950542819607891970.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950542819607891970.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `JWInteger`
- `easy showAnything`
- `TextCombinerTwo`
- `RH_Prompter`
- `easy showAnything`
- `RH_Translator`
- `MathExpression|pysssss`
- `JjkText`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `CreateCFGScheduleFloatList`
- `PrimitiveNode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `easy showAnything`
- `Note`
- `TextCombinerTwo`
- `RH_Captioner`
- `JjkText`
- `JjkText`
- `easy anythingIndexSwitch`
- `VHS_VideoCombine`
- `ImageResize+`
- `LoadImage`
- `WanVideoImageToVideoEncode`

## 知识

覆盖率 **79%**（31/39）

**有卡**：`JWInteger`、`TextCombinerTwo`、`RH_Prompter`、`RH_Translator`、`MathExpression|pysssss`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoVAELoader`、`RH_Captioner`、`easy anythingIndexSwitch`、`VHS_VideoCombine`、`ImageResize+`、`LoadImage`、`WanVideoImageToVideoEncode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
